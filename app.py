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

# Cobalt API ke public instances (Agar ek fail hota hai, dusra try karega)
COBALT_INSTANCES = [
    "https://api.cobalt.tools/api/json",
    "https://co.wuk.sh/api/json",
    "https://cobalt-api.kwiatekmiki.com/api/json"
]

@app.get("/")
def home():
    return {"status": "success", "message": "Nebula API is running with Cobalt!"}

@app.post("/download")
def download_video(req: VideoRequest):
    # 1. Pehle page se Title aur Thumbnail nikalne ki koshish karte hain (Social Media Scraping)
    title = "Video Download"
    thumbnail = ""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        html = requests.get(req.url, headers=headers, timeout=10).text
        title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        if title_match: title = title_match.group(1)
        if img_match: thumbnail = img_match.group(1)
    except:
        pass # Agar metadata na mile toh default rahega

    # 2. Cobalt API se Download link nikalte hain
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Video Quality (720p default)
    payload_video = {"url": req.url, "vQuality": "720"}
    # Audio MP3
    payload_audio = {"url": req.url, "isAudioOnly": True}

    video_url = None
    audio_url = None

    for instance in COBALT_INSTANCES:
        try:
            # Video link fetch
            res_vid = requests.post(instance, json=payload_video, headers=headers, timeout=15)
            if res_vid.status_code == 200:
                data_vid = res_vid.json()
                if data_vid.get("status") == "stream" or data_vid.get("status") == "redirect":
                    video_url = data_vid.get("url")
                    
                    # Audio link fetch
                    res_aud = requests.post(instance, json=payload_audio, headers=headers, timeout=15)
                    if res_aud.status_code == 200:
                        data_aud = res_aud.json()
                        audio_url = data_aud.get("url")
                    
                    break # Agar link mil gaya toh loop rok do
        except:
            continue # Agar ek instance fail hua toh dusra try karo

    if not video_url:
        raise HTTPException(status_code=400, detail="Could not fetch video link. The video might be private or the servers are busy.")

    # Frontend ko wahi format mein data bhej rahe hain jaisa woh expect karta hai
    return {
        "status": "success",
        "title": title,
        "thumbnail": thumbnail,
        "duration": 0, # Cobalt duration nahi deta, frontend handle kar lega
        "hd_url": video_url,
        "sd_url": video_url, # Cobalt best quality deta hai
        "audio_url": audio_url,
        "all_formats": [{"quality": "HD", "url": video_url}]
    }
