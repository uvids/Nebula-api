from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import requests
import re
from cachetools import TTLCache

app = FastAPI(title="Nebula Video API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

# 1. CACHING: Ek video ka result 2 ghante (7200 sec) tak save rahega
# Agar 100 log ek hi video download karenge, toh server sirf 1 baar process karega.
video_cache = TTLCache(maxsize=1000, ttl=7200)

COBALT_INSTANCES = [
    "https://api.cobalt.tools/",
    "https://cobalt-api.kwiatekmiki.com/",
    "https://co.wuk.sh/"
]

@app.get("/")
def home():
    return {"status": "success", "message": "Nebula Super API is Live!"}

@app.post("/download")
def download_video(req: VideoRequest):
    # Check Cache First
    if req.url in video_cache:
        print("Serving from Cache!")
        return video_cache[req.url]

    title = "Video Download"
    thumbnail = ""
    
    # Metadata (Title & Thumbnail) nikalne ki koshish
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        html = requests.get(req.url, headers=headers, timeout=10).text
        title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        if title_match: title = title_match.group(1)
        if img_match: thumbnail = img_match.group(1)
    except:
        pass

    video_url = None
    audio_url = None

    # --- LAYER 1: yt-dlp TRY KAREIN ---
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'extractor_args': {'youtube': {'player_client': ['tv', 'ios']}},
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(req.url, download=False)
            video_url = info.get('url')
            if not video_url and 'formats' in info:
                formats = [f for f in info['formats'] if f.get('vcodec') != 'none' and f.get('url')]
                if formats:
                    video_url = formats[-1]['url'] # Best quality
            if not title or title == "Video Download":
                title = info.get('title', title)
    except:
        pass # Agar fail hua, toh neeche wala try karein

    # --- LAYER 2: AGAR yt-dlp FAIL HUA, TOH COBALT API TRY KAREIN ---
    if not video_url:
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        for instance in COBALT_INSTANCES:
            try:
                payload = {"url": req.url, "vQuality": "720"}
                res = requests.post(instance, json=payload, headers=headers, timeout=15)
                if res.status_code == 200:
                    data = res.json()
                    if data.get("status") in ["stream", "redirect", "tunnel"]:
                        video_url = data.get("url")
                        
                        # Audio link
                        res_aud = requests.post(instance, json={"url": req.url, "isAudioOnly": True}, headers=headers, timeout=15)
                        if res_aud.status_code == 200:
                            audio_url = res_aud.json().get("url")
                        break
            except:
                continue

    # Agar dono fail ho gaye
    if not video_url:
        raise HTTPException(status_code=400, detail="Server busy or link private. Please try another video.")

    # Result taiyar karein
    result = {
        "status": "success",
        "title": title,
        "thumbnail": thumbnail,
        "duration": 0,
        "hd_url": video_url,
        "sd_url": video_url,
        "audio_url": audio_url,
        "all_formats": [{"quality": "HD", "url": video_url}]
    }

    # Cache mein save karein
    video_cache[req.url] = result
    
    return result
