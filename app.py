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
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(req.url, download=False)
            
            # Agar video hi nahi hai (sirf photo ya text post hai)
            if 'formats' not in info and 'url' not in info:
                raise HTTPException(status_code=400, detail="Is link par koi video nahi mili. Yeh photo ya text post ho sakta hai.")

            formats = info.get('formats', [])
            video_formats = []
            seen_urls = set()
            
            hd_link = None
            sd_link = None
            
            for f in formats:
                if f.get('url') and f.get('url') not in seen_urls:
                    vcodec = f.get('vcodec', 'none')
                    height = f.get('height') or 0
                    
                    # Sirf video formats uthayein (audio ignore karein)
                    if vcodec != 'none' or height > 0:
                        seen_urls.add(f.get('url'))
                        quality_name = f"{height}p" if height else "Video"
                        
                        video_formats.append({
                            "quality": quality_name,
                            "url": f.get('url')
                        })
                        
                        if height >= 720 and not hd_link:
                            hd_link = f.get('url')
                        elif height > 0 and height < 720 and not sd_link:
                            sd_link = f.get('url')
            
            # Fallback: Agar list khali hai par direct url mila hai
            if not video_formats and info.get('url'):
                video_formats.append({"quality": "Default", "url": info.get('url')})
                if not hd_link: hd_link = info.get('url')
                if not sd_link: sd_link = info.get('url')

            # Agar phir bhi kuch na mile toh error dein
            if not video_formats:
                raise HTTPException(status_code=404, detail="Video download link nahi mil paya. Private video ho sakti hai.")

            # Duration aur Thumbnail handle karein
            duration = info.get('duration')
            if not duration:
                duration = 0
                
            thumbnail = info.get('thumbnail')
            if not thumbnail and 'thumbnails' in info and len(info['thumbnails']) > 0:
                thumbnail = info['thumbnails'][-1].get('url', '')

            return {
                "status": "success", 
                "title": info.get('title', 'Facebook Video'), 
                "thumbnail": thumbnail,
                "duration": duration,
                "hd_url": hd_link,
                "sd_url": sd_link,
                "all_formats": video_formats
            }
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
