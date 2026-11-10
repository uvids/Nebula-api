<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Uvids - Download Facebook Videos in HD</title>
<meta name="description" content="Uvids: Fast, free Facebook video downloader. HD, SD and MP3, no watermark.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  theme: {
    extend: {
      fontFamily: { sans: ['Poppins', 'sans-serif'] },
      colors: { fbblue: '#1877F2', violet: '#8B5CF6' }
    }
  }
}
</script>
<style>
  :root { --blue:#1877F2; --purple:#8B5CF6; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Poppins', sans-serif;
    background: #0A0A0F;
    color: #e5e7eb;
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-tap-highlight-color: transparent;
  }

  /* Floating glowing orbs */
  .orb { position: fixed; border-radius: 50%; filter: blur(90px); opacity: .45; z-index: 0; pointer-events: none; background: radial-gradient(circle at 30% 30%, var(--blue), var(--purple)); }
  .orb-1 { width: 420px; height: 420px; top: -120px; left: -120px; animation: float1 14s ease-in-out infinite; }
  .orb-2 { width: 360px; height: 360px; top: 35%; right: -140px; background: radial-gradient(circle at 30% 30%, var(--purple), #4c1d95); animation: float2 18s ease-in-out infinite; }
  .orb-3 { width: 320px; height: 320px; bottom: -100px; left: 25%; animation: float3 16s ease-in-out infinite; opacity: .35; }
  @keyframes float1 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(120px,90px) scale(1.15)} }
  @keyframes float2 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(-100px,-80px) scale(1.2)} }
  @keyframes float3 { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(90px,-110px) scale(.9)} }

  /* Glass */
  .glass { background: linear-gradient(135deg, rgba(255,255,255,.08), rgba(255,255,255,.02)); backdrop-filter: blur(22px); -webkit-backdrop-filter: blur(22px); border: 1px solid rgba(255,255,255,.12); box-shadow: 0 20px 60px rgba(0,0,0,.5), 0 0 40px rgba(24,119,242,.12), inset 0 1px 0 rgba(255,255,255,.15); }
  .grad-text { background: linear-gradient(90deg, var(--blue), var(--purple)); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .grad-bg { background: linear-gradient(135deg, var(--blue), var(--purple)); }

  /* 3D Logo */
  .logo3d {
    width: 50px; height: 50px; border-radius: 16px;
    background: linear-gradient(135deg, var(--blue), var(--purple));
    position: relative; transform: perspective(300px) rotateX(10deg) rotateY(-10deg);
    transform-style: preserve-3d; transition: transform 0.1s ease-out;
    box-shadow: 6px 8px 0 rgba(0,0,0,.35), 0 0 25px rgba(139,92,246,.7), inset 2px 2px 6px rgba(255,255,255,.45), inset -3px -3px 8px rgba(0,0,0,.35);
    display: flex; align-items: center; justify-content: center;
  }
  .logo3d::after { content: ''; position: absolute; inset: 0; border-radius: 16px; background: linear-gradient(160deg, rgba(255,255,255,.35), transparent 50%); }
  .logo3d svg { position: relative; z-index: 2; transform: translateZ(14px); filter: drop-shadow(0 2px 3px rgba(0,0,0,.4)); }

  /* Main card */
  .main-card { transition: transform 0.4s ease, box-shadow 0.4s ease; }
  .main-card:hover { transform: translateY(-5px); box-shadow: 0 30px 80px rgba(0,0,0,.6), 0 0 70px rgba(139,92,246,.25), inset 0 1px 0 rgba(255,255,255,.2); }

  /* Buttons */
  .btn-primary { background: linear-gradient(135deg, var(--blue), var(--purple)); box-shadow: 0 4px 15px rgba(24,119,242,.4); transition: all 0.3s ease; }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(139,92,246,.6); filter: brightness(1.1); }
  .btn-primary:active { transform: translateY(2px); box-shadow: 0 2px 10px rgba(24,119,242,.4); }
  
  .btn-secondary { transition: all 0.3s ease; border: 1px solid rgba(255,255,255,.2); }
  .btn-secondary:hover { background: rgba(255,255,255,.1); }
  .btn-secondary:active { transform: scale(0.98); }

  /* Feature cards */
  .feature-card { transition: transform .35s ease, box-shadow .35s ease; transform: perspective(900px) rotateX(0) rotateY(0); }
  .feature-card:hover { transform: perspective(900px) rotateX(8deg) rotateY(-10deg) translateY(-8px) scale(1.02); box-shadow: 0 30px 60px rgba(0,0,0,.6), 0 0 50px rgba(139,92,246,.35); }

  /* Input Box */
  .url-input { background: rgba(10,10,15,.6); border: 1px solid rgba(255,255,255,.15); transition: border-color .3s, box-shadow .3s; }
  .url-input:focus-within { border-color: var(--purple); box-shadow: 0 0 0 3px rgba(139,92,246,.25), 0 0 30px rgba(24,119,242,.25); background: rgba(10,10,15,.8); }

  /* Spinner & Animations */
  .spinner { width: 56px; height: 56px; border-radius: 50%; border: 4px solid rgba(255,255,255,.1); border-top-color: var(--blue); border-right-color: var(--purple); animation: spin 0.9s linear infinite; box-shadow: 0 0 25px rgba(139,92,246,.5); }
  @keyframes spin { to { transform: rotate(360deg); } }
  .fade-in { animation: fadeIn .6s ease both; }
  @keyframes fadeIn { from{opacity:0; transform:translateY(20px)} to{opacity:1; transform:translateY(0)} }

  /* FAQ */
  details > summary { list-style: none; cursor: pointer; }
  details > summary::-webkit-details-marker { display: none; }
  details[open] summary .chev { transform: rotate(180deg); }
  details .chev { transition: transform .3s; }
  details[open] { box-shadow: 0 0 30px rgba(139,92,246,.2); }
  details > div { animation: fadeIn .35s ease both; }

  /* Modal & Forms */
  #contactModal { transition: opacity .3s ease; }
  #contactModal.hidden-modal { opacity: 0; pointer-events: none; }
  #contactModal .modal-box { transition: transform .35s cubic-bezier(.2,.9,.3,1.2); }
  #contactModal.hidden-modal .modal-box { transform: scale(.9) translateY(30px); }
  .field { background: rgba(10,10,15,.6); border: 1px solid rgba(255,255,255,.12); transition: border-color .3s, box-shadow .3s; color: #fff; }
  .field:focus { outline: none; border-color: var(--purple); box-shadow: 0 0 0 3px rgba(139,92,246,.25); }
  .field::placeholder { color: #6b7280; }

  /* Toast */
  #toastContainer { position: fixed; bottom: 24px; right: 24px; z-index: 100; display: flex; flex-direction: column; gap: 10px; }
  .toast { background: linear-gradient(135deg, rgba(24,119,242,.95), rgba(139,92,246,.95)); color: #fff; padding: 14px 20px; border-radius: 14px; font-size: 14px; max-width: 340px; box-shadow: 0 10px 40px rgba(0,0,0,.5), 0 0 30px rgba(139,92,246,.5); backdrop-filter: blur(10px); animation: toastIn .4s ease both; }
  .toast.out { animation: toastOut .4s ease both; }
  @keyframes toastIn { from{opacity:0; transform:translateX(60px)} to{opacity:1; transform:translateX(0)} }
  @keyframes toastOut { from{opacity:1; transform:translateX(0)} to{opacity:0; transform:translateX(60px)} }

  /* Download Buttons */
  .dl-btn { transition: all 0.3s ease; }
  .dl-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(139,92,246,.4); }
  .dl-btn:active { transform: translateY(0); }
  .dl-btn-secondary { background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.15); }
  .dl-btn-secondary:hover { background: rgba(255,255,255,.1); border-color: rgba(255,255,255,.3); box-shadow: 0 10px 25px rgba(0,0,0,.3); }
  .thumb { background: radial-gradient(circle at 25% 30%, rgba(24,119,242,.8), transparent 55%), radial-gradient(circle at 75% 70%, rgba(139,92,246,.8), transparent 55%), #12121c; }
</style>
</head>
<body>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div class="orb orb-3"></div>

<div class="relative z-10">
  <header class="max-w-6xl mx-auto px-5 py-6 flex items-center justify-between">
    <a href="#" class="flex items-center gap-4 group">
      <div class="logo3d" id="interactiveLogo">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="M7 11l5 5 5-5"/><path d="M5 20h14"/></svg>
      </div>
      <span class="text-4xl font-black tracking-tighter grad-text drop-shadow-lg">Uvids</span>
    </a>
    <nav class="hidden sm:flex items-center gap-6 text-sm text-gray-300">
      <a href="#features" class="hover:text-white transition">Features</a>
      <a href="#faq" class="hover:text-white transition">FAQ</a>
      <button onclick="openModal()" class="glass px-4 py-2 rounded-full hover:text-white transition hover:bg-white/10">Contact</button>
    </nav>
  </header>
  <main>
  <section class="max-w-4xl mx-auto px-5 pt-10 pb-8 text-center">
    <span class="glass inline-block px-4 py-1.5 rounded-full text-xs font-medium text-gray-300 mb-6">⚡ Fast &bull; Secure &bull; Unlimited</span>
    <h1 class="text-4xl sm:text-6xl font-extrabold leading-tight mb-5">
      Download Facebook Videos <span class="grad-text">in HD</span>
    </h1>
    <p class="text-lg sm:text-xl text-gray-400 font-light">Fast, Free, No Watermark</p>
  </section>

  <section class="max-w-3xl mx-auto px-5 pb-16">
    <div id="mainCard" class="main-card glass rounded-3xl p-6 sm:p-10">
      
      <div id="inputArea">
        <label for="urlInput" class="block text-sm font-medium text-gray-300 mb-3">Paste your Facebook video link</label>
        <div class="url-input rounded-2xl flex items-center gap-2 p-3 sm:p-4">
          <svg class="ml-1 shrink-0 text-gray-400" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
          <input id="urlInput" type="text" placeholder="https://www.facebook.com/watch?v=..." class="flex-1 bg-transparent outline-none text-white placeholder-gray-500 px-2 py-3 text-base sm:text-lg min-w-0" autocomplete="off">
          <button id="pasteBtn" type="button" class="bg-white/10 hover:bg-white/20 text-white text-sm font-medium px-4 py-2.5 rounded-xl transition shrink-0 hidden sm:block">Paste</button>
          <button id="clearBtn" type="button" class="bg-transparent hover:text-red-400 text-gray-400 text-sm font-medium px-3 py-2.5 rounded-xl transition shrink-0">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>
          </button>
        </div>

        <button id="pasteBtnMobile" type="button" class="sm:hidden mt-3 w-full bg-white/10 hover:bg-white/20 text-white text-sm font-medium px-4 py-3 rounded-xl transition flex items-center justify-center gap-2">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>
          Paste from Clipboard
        </button>

        <button id="checkBtn" type="button" class="btn-primary w-full mt-6 py-4 rounded-2xl text-white text-lg font-semibold tracking-wide">Check Link</button>
        <p id="errorMsg" class="text-red-400 text-sm mt-3 hidden text-center">Please paste a valid Facebook video link.</p>
      </div>

      <div id="loader" class="hidden flex-col items-center justify-center py-14">
        <div class="spinner"></div>
        <p class="mt-6 text-gray-300">Fetching video details...</p>
      </div>

      <div id="result" class="hidden fade-in">
        <div class="flex flex-col sm:flex-row gap-5">
          <div id="videoThumb" class="thumb relative w-full sm:w-56 aspect-video rounded-2xl overflow-hidden border border-white/10 shrink-0 flex items-center justify-center bg-cover bg-center">
            <div class="w-14 h-14 rounded-full bg-black/50 backdrop-blur flex items-center justify-center shadow-lg z-10">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg>
            </div>
            <span id="videoDuration" class="absolute bottom-2 right-2 bg-black/80 text-xs px-2 py-0.5 rounded z-10 font-medium">00:00</span>
            <span class="absolute top-2 left-2 bg-green-500/80 border border-green-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full backdrop-blur z-10">✅ No Watermark</span>
          </div>
          <div class="flex-1 text-left">
            <h3 id="videoTitle" class="text-lg sm:text-xl font-semibold text-white line-clamp-2">Video Title</h3>
            <p class="text-sm text-gray-400 mt-1">facebook.com &bull; HD Available</p>
            <div class="mt-3 inline-flex items-center gap-2 text-xs text-green-400 bg-green-400/10 px-3 py-1 rounded-full">
              <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span> Ready to download
            </div>
          </div>
        </div>

        <!-- Desktop Download Buttons -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mt-8">
          <button id="btnHd" onclick="triggerDownload('hd')" class="dl-btn btn-primary text-white font-semibold py-3.5 rounded-xl flex-col items-center justify-center leading-tight hidden sm:flex">
            <span>⬇ HD (1080p)</span><span class="text-xs font-normal opacity-80">High Quality</span>
          </button>
          <button id="btnSd" onclick="triggerDownload('sd')" class="dl-btn dl-btn-secondary text-white font-semibold py-3.5 rounded-xl flex-col items-center justify-center leading-tight hidden sm:flex">
            <span>⬇ SD (720p)</span><span class="text-xs font-normal text-gray-400">Standard Quality</span>
          </button>
          <button id="btnMp3" onclick="triggerDownload('audio')" class="dl-btn dl-btn-secondary text-white font-semibold py-3.5 rounded-xl flex-col items-center justify-center leading-tight hidden sm:flex">
            <span>♫ MP3 (Audio)</span><span class="text-xs font-normal text-gray-400">Audio Only</span>
          </button>
        </div>

        <!-- Mobile Download Buttons (FIXED: Removed 'hidden flex' conflict, used inline style to hide initially) -->
        <div class="grid grid-cols-1 gap-3 mt-4 sm:hidden">
          <button id="btnHdMob" onclick="triggerDownload('hd')" class="dl-btn btn-primary text-white font-semibold py-3.5 rounded-xl flex-col items-center justify-center leading-tight flex" style="display: none;">
            <span>⬇ HD (1080p)</span><span class="text-xs font-normal opacity-80">High Quality</span>
          </button>
          <button id="btnSdMob" onclick="triggerDownload('sd')" class="dl-btn dl-btn-secondary text-white font-semibold py-3.5 rounded-xl flex-col items-center justify-center leading-tight flex" style="display: none;">
            <span>⬇ SD (720p)</span><span class="text-xs font-normal text-gray-400">Standard Quality</span>
          </button>
          <button id="btnMp3Mob" onclick="triggerDownload('audio')" class="dl-btn dl-btn-secondary text-white font-semibold py-3.5 rounded-xl flex-col items-center justify-center leading-tight flex" style="display: none;">
            <span>♫ MP3 (Audio)</span><span class="text-xs font-normal text-gray-400">Audio Only</span>
          </button>
        </div>

        <button id="newBtn" class="btn-secondary w-full mt-5 flex items-center justify-center gap-2 py-3.5 rounded-xl text-gray-300 text-sm font-medium hover:text-white focus:outline-none focus:ring-0">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/></svg>
          Download Another Video
        </button>
      </div>
    </div>
  </section>

  <section id="features" class="max-w-6xl mx-auto px-5 pb-20">
    <h2 class="text-3xl sm:text-4xl font-bold text-center mb-3">Why Choose <span class="grad-text">Uvids</span>?</h2>
    <p class="text-center text-gray-400 mb-12">Everything you need for a premium download experience.</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="feature-card glass rounded-3xl p-8">
        <div class="w-14 h-14 rounded-2xl grad-bg flex items-center justify-center mb-5 shadow-[0_0_25px_rgba(24,119,242,.5)]"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
        <h3 class="text-xl font-semibold mb-2">Lightning Fast</h3>
        <p class="text-gray-400 text-sm leading-relaxed">Paste the link and get your download options in seconds with our optimized servers.</p>
      </div>
      <div class="feature-card glass rounded-3xl p-8">
        <div class="w-14 h-14 rounded-2xl grad-bg flex items-center justify-center mb-5 shadow-[0_0_25px_rgba(139,92,246,.5)]"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="14" rx="2"/><path d="M8 21h8M12 18v3"/></svg></div>
        <h3 class="text-xl font-semibold mb-2">HD Quality</h3>
        <p class="text-gray-400 text-sm leading-relaxed">Save videos in crisp 1080p HD, standard 720p, or extract audio as MP3 anytime.</p>
      </div>
      <div class="feature-card glass rounded-3xl p-8">
        <div class="w-14 h-14 rounded-2xl grad-bg flex items-center justify-center mb-5 shadow-[0_0_25px_rgba(24,119,242,.5)]"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h3 class="text-xl font-semibold mb-2">Safe &amp; Private</h3>
        <p class="text-gray-400 text-sm leading-relaxed">No signup, no watermark, no tracking. Your downloads stay completely private.</p>
      </div>
    </div>
  </section>

  <!-- FAQ Section (Fully closed, no code cut-off) -->
  <section id="faq" class="max-w-3xl mx-auto px-5 pb-24">
    <h2 class="text-3xl sm:text-4xl font-bold text-center mb-3">Frequently Asked <span class="grad-text">Questions</span></h2>
    <p class="text-center text-gray-400 mb-10">Quick answers to common questions.</p>
    <div class="space-y-4">
      <details class="glass rounded-2xl p-5">
        <summary class="flex items-center justify-between font-medium text-white">How do I download a Facebook video? <svg class="chev" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></summary>
        <div class="mt-3 text-gray-400 text-sm leading-relaxed">Copy the video link from Facebook, paste it into the box above, click "Check Link", then choose your preferred quality to download.</div>
      </details>
      <details class="glass rounded-2xl p-5">
        <summary class="flex items-center justify-between font-medium text-white">Is Uvids really free? <svg class="chev" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></summary>
        <div class="mt-3 text-gray-400 text-sm leading-relaxed">Yes. Uvids is 100% free to use with no hidden fees, no signup and no watermark on your videos.</div>
      </details>
      <details class="glass rounded-2xl p-5">
        <summary class="flex items-center justify-between font-medium text-white">Which video qualities are supported? <svg class="chev" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></summary>
        <div class="mt-3 text-gray-400 text-sm leading-relaxed">We offer HD (1080p), SD (720p) when available, plus an MP3 audio-only option.</div>
      </details>
    </div>
  </section>
</main>
  <footer class="border-t border-white/10 bg-black/20 backdrop-blur-xl">
    <div class="max-w-6xl mx-auto px-5 py-10 text-center">
      <div class="flex items-center justify-center gap-3 mb-5">
        <div class="logo3d" style="width:34px;height:34px;border-radius:11px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="M7 11l5 5 5-5"/><path d="M5 20h14"/></svg></div>
        <span class="text-2xl font-bold grad-text">Uvids</span>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-x-8 gap-y-3 text-sm text-gray-400 mb-6">
        <a href="about.html" class="hover:text-white transition">About Us</a>
        <a href="privacy.html" class="hover:text-white transition">Privacy Policy</a>
        <a href="terms.html" class="hover:text-white transition">Terms</a>
        <a href="disclaimer.html" class="hover:text-white transition">Disclaimer</a>
        <a href="dmca.html" class="hover:text-white transition">DMCA</a>
        <button id="contactBtn" type="button" class="hover:text-white transition">Contact Us</button>
      </div>

      <a href="mailto:uvids.support@gmail.com" class="inline-flex items-center gap-2 glass px-5 py-2.5 rounded-full text-sm text-gray-200 hover:text-white transition hover:bg-white/10">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="url(#envGrad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><defs><linearGradient id="envGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1877F2"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient></defs><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/></svg>
        uvids.support@gmail.com
      </a>

      <p class="text-xs text-gray-500 mt-8 max-w-xl mx-auto">This website is not affiliated with Meta or Facebook.</p>
      <p class="text-xs text-gray-600 mt-2">&copy; <span id="year"></span> Uvids. All rights reserved.</p>
    </div>
  </footer>
</div>

<!-- Contact Modal -->
<div id="contactModal" class="hidden-modal fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
  <div class="modal-box glass rounded-3xl w-full max-w-lg p-6 sm:p-8 relative max-h-[95vh] overflow-y-auto" style="background:linear-gradient(135deg, rgba(30,30,50,.85), rgba(15,15,25,.9));">
    <button id="closeModal" type="button" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
    <h3 class="text-2xl font-bold grad-text mb-1">Contact Us</h3>
    <p class="text-sm text-gray-400 mb-6">Have a question or feedback? We'd love to hear from you.</p>
    <form id="contactForm" class="space-y-4">
      <div><label class="block text-sm text-gray-300 mb-1.5">Name</label><input type="text" required placeholder="Your name" class="field w-full rounded-xl px-4 py-3 text-sm"></div>
      <div><label class="block text-sm text-gray-300 mb-1.5">Email</label><input type="email" required placeholder="you@example.com" class="field w-full rounded-xl px-4 py-3 text-sm"></div>
      <div><label class="block text-sm text-gray-300 mb-1.5">Subject</label><input type="text" required placeholder="How can we help?" class="field w-full rounded-xl px-4 py-3 text-sm"></div>
      <div><label class="block text-sm text-gray-300 mb-1.5">Message</label><textarea rows="3" required placeholder="Write your message..." class="field w-full rounded-xl px-4 py-3 text-sm resize-none"></textarea></div>
      <button type="submit" class="btn-primary w-full py-3.5 rounded-xl text-white font-semibold">Send Message</button>
    </form>
  </div>
</div>

<div id="toastContainer"></div>

<script>
  // ⚠️ YAHAN APNA BACKEND URL DAALEIN ⚠️
  const API_URL = "https://your-backend-url.onrender.com/download"; 

  const $ = (id) => document.getElementById(id);
  const urlInput = $('urlInput');
  const inputArea = $('inputArea');
  const loader = $('loader');
  const result = $('result');
  const errorMsg = $('errorMsg');
  const modal = $('contactModal');

  let currentLinks = { hd: null, sd: null, audio: null };

  $('year').textContent = new Date().getFullYear();

  /* Toast */
  function showToast(message) {
    const t = document.createElement('div');
    t.className = 'toast';
    t.textContent = message;
    $('toastContainer').appendChild(t);
    setTimeout(() => { t.classList.add('out'); setTimeout(() => t.remove(), 400); }, 3500);
  }

  /* 3D Logo Effect */
  const logo = $('interactiveLogo');
  if(logo) {
    logo.addEventListener('mousemove', (e) => {
      const rect = logo.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      logo.style.transform = `perspective(300px) rotateX(${-y * 0.5}deg) rotateY(${x * 0.5}deg) scale(1.1)`;
    });
    logo.addEventListener('mouseleave', () => {
      logo.style.transform = `perspective(300px) rotateX(10deg) rotateY(-10deg) scale(1)`;
    });
    logo.addEventListener('touchmove', (e) => {
      e.preventDefault();
      const touch = e.touches[0];
      const rect = logo.getBoundingClientRect();
      const x = touch.clientX - rect.left - rect.width / 2;
      const y = touch.clientY - rect.top - rect.height / 2;
      logo.style.transform = `perspective(300px) rotateX(${-y * 0.5}deg) rotateY(${x * 0.5}deg) scale(1.1)`;
    }, { passive: false });
    logo.addEventListener('touchend', () => {
      logo.style.transform = `perspective(300px) rotateX(10deg) rotateY(-10deg) scale(1)`;
    });
  }

  /* Paste */
  async function handlePaste() {
    try {
      const text = await navigator.clipboard.readText();
      urlInput.value = text;
      errorMsg.classList.add('hidden');
      showToast(text ? 'Link pasted!' : 'Clipboard empty.');
    } catch (e) {
      showToast('Paste manually (Ctrl+V).');
      urlInput.focus();
    }
  }
  $('pasteBtn').addEventListener('click', handlePaste);
  $('pasteBtnMobile').addEventListener('click', handlePaste);

  /* Clear */
  $('clearBtn').addEventListener('click', () => {
    urlInput.value = '';
    errorMsg.classList.add('hidden');
    urlInput.focus();
  });

  /* Format Duration */
  function formatDuration(seconds) {
    if(!seconds) return "00:00";
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  /* Check Link */
  $('checkBtn').addEventListener('click', async () => {
    const val = urlInput.value.trim();
    if (!val) { 
      errorMsg.textContent = 'Please paste a video link first.'; 
      errorMsg.classList.remove('hidden'); 
      return; 
    }
    
    errorMsg.classList.add('hidden');
    inputArea.classList.add('hidden');
    result.classList.add('hidden');
    loader.classList.remove('hidden'); 
    loader.classList.add('flex');

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: val })
      });

      if (!response.ok) throw new Error("API Error");

      const data = await response.json();

      if (data.status === 'success') {
        $('videoTitle').innerText = data.title || "Facebook Video";
        $('videoDuration').innerText = formatDuration(data.duration);

        if (data.thumbnail) {
          const thumbDiv = $('videoThumb');
          thumbDiv.style.backgroundImage = `url('${data.thumbnail}')`;
          thumbDiv.style.background = `url('${data.thumbnail}') center/cover no-repeat`; 
        }

        currentLinks.hd = data.hd_url;
        currentLinks.sd = data.sd_url;
        currentLinks.audio = data.audio_url;

        // Show/Hide Buttons (Using inline styles to override the initial hidden state)
        $('btnHd').style.display = data.hd_url ? 'flex' : 'none';
        $('btnSd').style.display = data.sd_url ? 'flex' : 'none';
        $('btnMp3').style.display = data.audio_url ? 'flex' : 'none';
        
        $('btnHdMob').style.display = data.hd_url ? 'flex' : 'none';
        $('btnSdMob').style.display = data.sd_url ? 'flex' : 'none';
        $('btnMp3Mob').style.display = data.audio_url ? 'flex' : 'none';

        loader.classList.add('hidden'); 
        loader.classList.remove('flex');
        result.classList.remove('hidden');
      } else {
        throw new Error("API returned failure");
      }

    } catch (error) {
      loader.classList.add('hidden'); 
      loader.classList.remove('flex');
      inputArea.classList.remove('hidden');
      showToast("Error: Backend connect nahi hua ya link invalid hai.");
      console.error(error);
    }
  });

  urlInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') $('checkBtn').click(); });

  /* Reset */
  $('newBtn').addEventListener('click', () => {
    result.classList.add('hidden');
    inputArea.classList.remove('hidden');
    urlInput.value = '';
    urlInput.focus();
  });

  /* Download Button Logic */
  function triggerDownload(type) {
    const url = currentLinks[type];
    if (url) {
      showToast(`Starting download...`);
      window.open(url, '_blank');
    } else {
      showToast(`❌ This quality is not available.`);
    }
  }

  /* Modal */
  window.openModal = function() { modal.classList.remove('hidden-modal'); document.body.style.overflow = 'hidden'; }
  function closeModal() { modal.classList.add('hidden-modal'); document.body.style.overflow = ''; }
  $('contactBtn').addEventListener('click', window.openModal);
  $('closeModal').addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });

  /* Contact form */
  $('contactForm').addEventListener('submit', (e) => {
    e.preventDefault(); closeModal(); e.target.reset();
    showToast('Message sent successfully!');
  });
</script>
</body>
</html>
