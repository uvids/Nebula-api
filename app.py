# 2. URL ke hisaab se Cookies file check karna
cookie_file = None
if "youtube.com" in req.url or "youtu.be" in req.url:
    if os.path.exists("youtube_cookies.txt"):
        cookie_file = "youtube_cookies.txt"
elif "instagram.com" in req.url:
    if os.path.exists("instagram_cookies.txt"):
        cookie_file = "instagram_cookies.txt"
elif "facebook.com" in req.url or "fb.watch" in req.url: # YE NAYA ADD KARO
    if os.path.exists("facebook_cookies.txt"):
        cookie_file = "facebook_cookies.txt"
