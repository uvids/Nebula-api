from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import re

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

# Cobalt API v10 ke naye aur reliable instances
COBALT_INSTANCES = [
    "https://api.cobalt.tools/",
    "https://cobalt-api.kwiatekmiki.com/",
    "https://co.wuk.sh/"
]

@app.get("/")
def home():
    return {"status": "success", "message": "Nebula API is running with Cobalt V10!"}

@app.post("/download")
def download_video(req: VideoRequest):
    title = "Video Download"
    thumbnail = ""
    
    # 1. Metadata (Title & Thumbnail) nikalne ki koshish
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        html = requests.get(req.url, headers=headers, timeout=10).text
        title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        if title_match: title = title_match.group(1)
        if img_match: thumbnail = img_match.group(1)
    except:
        pass

    # 2. Cobalt API se Video aur Audio link nikalna
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    video_url = None
    audio_url = None

    # Har instance ko try karo
    for instance in COBALT_INSTANCES:
        try:
            # Video Link (720p best quality)
            payload = {"url": req.url, "vQuality": "720"}
            res = requests.post(instance, json=payload, headers=headers, timeout=15)
            
            if res.status_code == 200:
                data = res.json()
                if data.get("status") in ["stream", "redirect", "tunnel"]:
                    video_url = data.get("url")
                    
                    # Audio Link
                    payload_audio = {"url": req.url, "isAudioOnly": True}
                    res_aud = requests.post(instance, json=payload_audio, headers=headers, timeout=15)
                    if res_aud.status_code == 200:
                        audio_url = res_aud.json().get("url")
                    
                    break # Agar link mil gaya toh loop se bahar nikal jao
        except:
            continue # Agar ek server fail hua toh dusra try karo

    if not video_url:
        raise HTTPException(status_code=400, detail="Video link not found. Server is busy or link is private.")

    return {
        "status": "success",
        "title": title,
        "thumbnail": thumbnail,
        "duration": 0,
        "hd_url": video_url,
        "sd_url": video_url,
        "audio_url": audio_url,
        "all_formats": [{"quality": "HD", "url": video_url}]
    }
