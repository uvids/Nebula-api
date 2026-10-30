from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import urllib.request
import re
import os

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
    return {"status": "success", "message": "Nebula API is running with Cookies!"}

@app.post("/download")
def download_video(req: VideoRequest):
    title = "Video Download"
    thumbnail = ""
    
    # 1. Title aur Thumbnail nikalne ki koshish
    try:
        req_obj = urllib.request.Request(req.url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req_obj, timeout=10).read().decode('utf-8')
        title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        img_match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        if title_match: title = title_match.group(1)
        if img_match: thumbnail = img_match.group(1)
    except:
        pass

    # 2. URL ke hisaab se Cookies file check karna
    cookie_file = None
    if "youtube.com" in req.url or "youtu.be" in req.url:
        if os.path.exists("youtube_cookies.txt"):
            cookie_file = "youtube_cookies.txt"
    elif "instagram.com" in req.url:
        if os.path.exists("instagram_cookies.txt"):
            cookie_file = "instagram_cookies.txt"

    # 3. yt-dlp ki settings
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'extractor_args': {
            'youtube': {'player_client': ['android', 'ios', 'tv']}
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
    }
    
    # Agar cookies file mil gayi toh use karo
    if cookie_file:
        ydl_opts['cookiefile'] = cookie_file

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(req.url, download=False)

            formats = info.get('formats', [])
            video_formats = []
            seen_heights = set()
            hd_link = None
            sd_link = None
            audio_link = None

            # Audio link nikalna
            for f in formats:
                if f.get('vcodec') == 'none' and f.get('acodec') != 'none' and f.get('url'):
                    audio_link = f.get('url')
                    break
            
            # Video links nikalna (Best quality pehle)
            valid_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('height') and f.get('url')]
            valid_formats.sort(key=lambda x: x.get('height', 0), reverse=True)

            for f in valid_formats:
                height = f.get('height')
                if height not in seen_heights:
                    seen_heights.add(height)
                    link = f.get('url')
                    video_formats.append({"quality": f"{height}p", "url": link})
                    if height >= 720 and not hd_link: 
                        hd_link = link
                    elif height < 720 and not sd_link: 
                        sd_link = link

            # Fallbacks agar koi format na mile
            if not hd_link and video_formats: hd_link = video_formats[0]['url']
            if not sd_link and video_formats: sd_link = video_formats[-1]['url']
            if not hd_link and info.get('url'): hd_link = info.get('url')
            if not sd_link and info.get('url'): sd_link = info.get('url')

            duration = int(info.get('duration', 0)) if info.get('duration') else 0
            if info.get('thumbnail'): thumbnail = info.get('thumbnail')
            if not title or title == "Video Download": title = info.get('title', title)

            return {
                "status": "success", 
                "title": title, 
                "thumbnail": thumbnail,
                "duration": duration,
                "hd_url": hd_link,
                "sd_url": sd_link,
                "audio_url": audio_link,
                "all_formats": video_formats
            }
    except Exception as e:
        # Asli error message return karega taaki pata chale kya problem hai
        raise HTTPException(status_code=400, detail=f"Downloader Error: {str(e)}")
