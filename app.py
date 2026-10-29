from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp

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

@app.get("/")
def home():
    return {"status": "success", "message": "Nebula API is running!"}

@app.post("/download")
def download_video(req: VideoRequest):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'best[ext=mp4]/best',
        'skip_download': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(req.url, download=False)
            video_url = info.get('url')
            if not video_url and 'formats' in info:
                formats = [f for f in info['formats'] if f.get('ext') == 'mp4' and f.get('vcodec') != 'none']
                if formats:
                    best_format = max(formats, key=lambda x: (x.get('height', 0) or 0))
                    video_url = best_format.get('url')
            if not video_url:
                raise HTTPException(status_code=404, detail="Video link not found.")
            return {"status": "success", "title": info.get('title', 'Video'), "download_url": video_url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
