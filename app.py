<style>
    .post-title, .entry-title, h1.title, .blog-pager, .feed-links, 
    .Attribution, #navbar-iframe, .post-footer, .post-header, .comments { 
        display: none !important; 
    }
    body { background-color: #0f111a !important; }
    .post-body { padding: 0 !important; }
    
    .nebula-container { max-width: 600px; margin: 0 auto; padding: 20px 10px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .nebula-navbar { background: #1a1d2d; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3); border-radius: 12px; margin-bottom: 25px; border: 1px solid #2d324a; }
    .nebula-logo-container { display: flex; align-items: center; gap: 10px; text-decoration: none; }
    .nebula-logo-text { font-size: 22px; font-weight: 800; letter-spacing: 1px; background: -webkit-linear-gradient(45deg, #8a2be2, #ff1493); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    .tool-card { background: #1a1d2d; padding: 35px 25px; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.4); border: 1px solid #2d324a; margin-bottom: 20px;}
    .tool-title { text-align: center; color: #ffffff; font-size: 26px; margin-bottom: 8px; font-weight: 700; }
    .tool-desc { text-align: center; color: #8b92a5; font-size: 14px; margin-bottom: 30px; }
    
    .input-group { position: relative; margin-bottom: 20px; }
    .input-field { width: 100%; padding: 16px; background: #0f111a; border: 2px solid #2d324a; border-radius: 10px; font-size: 15px; outline: none; box-sizing: border-box; color: #ffffff; transition: border 0.3s; }
    .input-field:focus { border-color: #8a2be2; box-shadow: 0 0 10px rgba(138, 43, 226, 0.2); }
    
    .submit-btn { width: 100%; padding: 16px; background: linear-gradient(45deg, #8a2be2, #ff1493); color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: 600; cursor: pointer; transition: transform 0.2s; }
    .submit-btn:disabled { background: #3a3f58; cursor: not-allowed; }
    
    /* Video Preview Card */
    .video-preview { display: none; background: #0f111a; border-radius: 12px; padding: 15px; margin-top: 20px; border: 1px solid #2d324a; }
    .preview-img { width: 100%; border-radius: 8px; margin-bottom: 15px; object-fit: cover; max-height: 250px; }
    .preview-title { color: #fff; font-size: 16px; font-weight: 600; margin-bottom: 5px; text-align: center; }
    .preview-meta { color: #8b92a5; font-size: 13px; text-align: center; margin-bottom: 15px; }
    
    /* Download Buttons */
    .dl-btn { display: block; width: 100%; padding: 14px; margin-bottom: 10px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; color: white; box-sizing: border-box; transition: 0.3s; }
    .btn-hd { background: #28a745; }
    .btn-hd:hover { background: #218838; }
    .btn-sd { background: #007bff; }
    .btn-sd:hover { background: #0069d9; }
    
    /* More Options */
    .more-options-btn { display: block; width: 100%; padding: 10px; background: transparent; border: 1px solid #2d324a; color: #a0a5b5; border-radius: 8px; cursor: pointer; margin-top: 10px; font-size: 14px; }
    .more-options-btn:hover { background: #2d324a; color: #fff; }
    .other-qualities { display: none; margin-top: 10px; background: #151825; padding: 10px; border-radius: 8px; }
    .quality-link { display: block; padding: 10px; text-align: center; color: #8a2be2; text-decoration: none; font-weight: bold; border-bottom: 1px solid #2d324a; }
    .quality-link:last-child { border-bottom: none; }
    
    /* FAQ Section */
    .faq-section { background: #1a1d2d; padding: 25px; border-radius: 16px; border: 1px solid #2d324a; margin-top: 20px; }
    .faq-title { color: #fff; font-size: 20px; margin-bottom: 15px; text-align: center; font-weight: 700; }
    details { background: #0f111a; padding: 15px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #2d324a; cursor: pointer; }
    summary { color: #fff; font-weight: 600; font-size: 15px; outline: none; }
    details p { color: #8b92a5; font-size: 14px; margin-top: 10px; line-height: 1.5; }
    
    /* Spinner */
    .loading-spinner { border: 3px solid #2d324a; border-top: 3px solid #ff1493; border-radius: 50%; width: 26px; height: 26px; animation: nebula-spin 1s linear infinite; margin: 0 auto 12px auto; }
    @keyframes nebula-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
</style>

<div class="nebula-container">
    <header class="nebula-navbar">
        <a href="/" class="nebula-logo-container">
            <span class="nebula-logo-text">Nebula Tools</span>
        </a>
    </header>

    <div class="tool-card">
        <h1 class="tool-title">Facebook Downloader</h1>
        <p class="tool-desc">Download high-quality Facebook videos instantly.</p>
        
        <div class="input-group">
            <input type="text" id="fbUrl" class="input-field" placeholder="Paste Facebook Video link here...">
        </div>
        
        <button onclick="getVideo()" id="btn" class="submit-btn">
            Download Now
        </button>

        <div id="result" style="text-align: center; margin-top: 15px;"></div>
        
        <!-- Video Preview Area -->
        <div id="video-preview" class="video-preview">
            <img id="vid-thumb" class="preview-img" src="" alt="Video Thumbnail">
            <div id="vid-title" class="preview-title"></div>
            <div id="vid-meta" class="preview-meta"></div>
            
            <a id="btn-hd" href="#" target="_blank" class="dl-btn btn-hd">Download HD Quality</a>
            <a id="btn-sd" href="#" target="_blank" class="dl-btn btn-sd">Download Normal Quality</a>
            
            <button class="more-options-btn" onclick="toggleMore()">More Options ▼</button>
            <div id="other-qualities" class="other-qualities"></div>
        </div>
    </div>

    <!-- FAQ Section -->
    <div class="faq-section">
        <h2 class="faq-title">Frequently Asked Questions</h2>
        
        <details>
            <summary>Where are videos saved after downloading?</summary>
            <p>It depends on your device. Usually, videos are saved in the "Downloads" folder of your phone or computer.</p>
        </details>
        
        <details>
            <summary>Does Nebula Tools store my downloaded videos?</summary>
            <p>No. We do not host any videos on our servers. All videos are downloaded directly from Facebook's servers.</p>
        </details>
        
        <details>
            <summary>Why is the video quality sometimes low?</summary>
            <p>We provide the best available quality for the video. If the original upload was low quality, the download will be too.</p>
        </details>
    </div>
</div>

<script>
function toggleMore() {
    const x = document.getElementById("other-qualities");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

async function getVideo() {
    const urlInput = document.getElementById('fbUrl').value;
    const resultDiv = document.getElementById('result');
    const btn = document.getElementById('btn');
    const preview = document.getElementById('video-preview');
    
    if (!urlInput) { 
        resultDiv.innerHTML = '<p style="color:#ff1493; font-size: 14px;">Please enter a valid Facebook URL.</p>'; 
        return; 
    }
    
    btn.disabled = true;
    btn.innerHTML = 'Fetching...';
    resultDiv.innerHTML = '<div class="loading-spinner"></div><p style="color:#8b92a5; font-size: 14px;">Waking up server (Takes 30-50s)...</p>';
    preview.style.display = 'none';
    
    try {
        const myApiUrl = 'https://nebula-api-6cc6.onrender.com/download'; 
        
        const response = await fetch(myApiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: urlInput })
        });
        
        const data = await response.json();
        
        if (data.status === "success") {
            resultDiv.innerHTML = ''; // clear loader
            
            // Populate Preview Card
            document.getElementById('vid-thumb').src = data.thumbnail || 'https://via.placeholder.com/400x200?text=No+Thumbnail';
            document.getElementById('vid-title').innerText = data.title;
            
            // Format Duration (e.g. 13 seconds -> 00:13)
            let mins = Math.floor(data.duration / 60);
            let secs = data.duration % 60;
            document.getElementById('vid-meta').innerText = `Duration: ${mins}:${secs < 10 ? '0'+secs : secs}`;
            
            // Set HD and SD buttons
            if (data.hd_url) {
                document.getElementById('btn-hd').href = data.hd_url;
                document.getElementById('btn-hd').style.display = 'block';
            } else {
                document.getElementById('btn-hd').style.display = 'none';
            }
            
            if (data.sd_url) {
                document.getElementById('btn-sd').href = data.sd_url;
                document.getElementById('btn-sd').style.display = 'block';
            } else {
                document.getElementById('btn-sd').style.display = 'none';
            }
            
            // Populate other qualities
            let otherHTML = '';
            if (data.all_formats && data.all_formats.length > 0) {
                data.all_formats.forEach(f => {
                    otherHTML += `<a href="${f.url}" target="_blank" class="quality-link">Force Download ${f.quality}</a>`;
                });
            } else {
                 otherHTML = '<p style="color:#8b92a5; text-align:center; font-size:13px;">No other formats available.</p>';
            }
            document.getElementById('other-qualities').innerHTML = otherHTML;
            
            // Show preview
            preview.style.display = 'block';
            
        } else {
            resultDiv.innerHTML = '<p style="color:#ff1493; font-size: 14px;">Error: Video not found or is private.</p>';
        }
    } catch (e) {
        resultDiv.innerHTML = '<p style="color:#ff1493; font-size: 14px;">Network Error: Server might be waking up. Try again in 10 seconds.</p>';
    } finally {
        btn.disabled = false;
        btn.innerHTML = 'Download Now';
    }
}
</script>
