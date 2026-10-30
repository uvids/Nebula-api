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
        'skip_download': True,
        'extractor_args': {
            'youtube': {'player_client': ['android', 'web']},
            'instagram': {'api': ['graphql']}
        },
        'geo_bypass': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(req.url, download=False)

            if 'formats' not in info and 'url' not in info:
                raise HTTPException(status_code=400, detail="No video found in this link.")

            formats = info.get('formats', [])
            video_formats = []
            seen_heights = set()
            hd_link = None
            sd_link = None

            valid_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('height')]
            valid_formats.sort(key=lambda x: x.get('height', 0), reverse=True)

            for f in valid_formats:
                height = f.get('height')
                if height not in seen_heights:
                    seen_heights.add(height)
                    link = f.get('url')
                    video_formats.append({"quality": f"{height}p", "url": link})
                    if height >= 720 and not hd_link: hd_link = link
                    elif height < 720 and not sd_link: sd_link = link

            if not hd_link and video_formats: hd_link = video_formats[0]['url']
            if not sd_link and video_formats: sd_link = video_formats[-1]['url']

            duration = int(info.get('duration', 0)) if info.get('duration') else 0
            thumbnail = info.get('thumbnail')
            if not thumbnail and 'thumbnails' in info and len(info['thumbnails']) > 0:
                thumbnail = info['thumbnails'][-1].get('url', '')

            return {
                "status": "success", 
                "title": info.get('title', 'Video'), 
                "thumbnail": thumbnail,
                "duration": duration,
                "hd_url": hd_link,
                "sd_url": sd_link,
                "all_formats": video_formats
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
