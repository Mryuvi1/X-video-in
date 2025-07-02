# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>&#9760;&#10084;&#128071;YUVI ON FIRE&#128071;&#10084;&#9760;</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    label { color: white; animation: fadeIn 1s; }
    .file { height: 30px; animation: bounce 2s infinite; }
    body {
      margin: 0;
      padding: 0;
      color: white;
      animation: fadeIn 2s;
      overflow-x: hidden;
    }
    #bg-video {
      position: fixed;
      top: 0;
      left: 0;
      min-width: 100vw;
      min-height: 100vh;
      z-index: -1;
      object-fit: cover;
    }
    .container {
      max-width: 350px; 
      height: auto;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px white;
      animation: zoomIn 2s;
    }
    .form-control {
      outline: 1px red;
      border: 1px double white;
      background: transparent;
      width: 100%;
      height: 40px;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 10px;
      color: white;
      animation: slideInLeft 1s;
    }
    .header { 
      text-align: center; 
      padding-bottom: 20px; 
      animation: bounceInDown 2s;
    }
    .btn-submit { 
      width: 100%; 
      margin-top: 10px;
      animation: pulse 2s infinite;
    }
    .footer { 
      text-align: center; 
      margin-top: 20px; 
      color: #888; 
      animation: fadeInUp 2s;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
      animation: zoomInUp 2s;
    }
    .whatsapp-link i { margin-right: 5px; }
    .stop-key-box {
      text-align: center;
      background-color: rgba(0, 0, 0, 0.7);
      border: 2px solid white;
      color: #00ff00;
      font-weight: bold;
      padding: 20px;
      margin-top: 30px;
      border-radius: 15px;
      animation: bounceInDown 1.5s;
    }

    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes bounce {
      0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
      40% { transform: translateY(-10px); }
      60% { transform: translateY(-5px); }
    }
    @keyframes zoomIn {
      from { transform: scale(0.5); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    @keyframes slideInLeft {
      from { transform: translateX(-100%); }
      to { transform: translateX(0); }
    }
    @keyframes bounceInDown {
      from { transform: translateY(-2000px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }
    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes zoomInUp {
      from { opacity: 0; transform: translateY(200px) scale(0.7); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
  </style>
</head>
<body>
  <!-- Video Background -->
  <video autoplay muted loop id="bg-video">
    <source src="https://raw.githubusercontent.com/kisan117/MR-DEVIL-VIDEO-CREATOR/main/VID-20250618-WA0211.mp4" type="video/mp4">
  </video>

  <header class="header mt-4">
    <h1 class="mt-3">☠️❤️ 👇𝐘𝐔𝐕𝐈 𝐎𝐍 𝐅𝐈𝐑𝐄 👇❤️☠️</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenOption" class="form-label">Select Token Option</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">Single Token</option>
          <option value="multiple">Token File</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">𝙀𝙉𝙏𝙀𝙍 𝙎𝙄𝙉𝙂𝙇𝙀 𝙏𝙊𝙆𝙀𝙉..⤵️</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">Choose Token File</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝙀𝙉𝙏𝙀𝙍 𝘾𝙊𝙉𝙑𝙊 𝙐𝙄𝘿...⤵️</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">𝙀𝙉𝙏𝙀𝙍 𝙃𝘼𝙏𝙀𝙍 𝙉𝘼𝙈𝙀...⤵️</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝙀𝙉𝙏𝙀𝙍 𝙎𝙋𝙀𝙀𝘿...⤵️ (seconds)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝙀𝙉𝙏𝙀𝙍 𝙂𝘼𝙇𝙄 𝙁𝙄𝙇𝙀..⤵️</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">🩷 𝙍𝙐𝙉𝙄𝙉𝙂 𝙎𝙀𝙍𝙑𝙀𝙍 🪽</button>
    </form>
    {% if stop_key %}
    <div class="stop-key-box">
      YOUR STOP KEY:<br><span style="font-size: 22px;">{{ stop_key }}</span>
    </div>
    {% endif %}
    <form method="post" action="/stop">
      <div class="mb-3 mt-4">
        <label for="taskId" class="form-label">🩷𝙀𝙉𝙏𝙀𝙍 𝙎𝙏𝙊𝙋 𝙆𝙀𝙔🪽</label>
        <input type="text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn btn-danger btn-submit mt-3">🩷 𝙎𝙏𝙊𝙋 𝙎𝙀𝙍𝙑𝙀𝙍🪽</button>
    </form>
  </div>
  <footer class="footer">
    <p>☠️❣️👇𝐘𝐔𝐕𝐈 𝐈𝐍𝐒𝐈𝐃𝐄👇❣️☠️</p>
    <p><a href="https://www.facebook.com/yuvi001x">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴇʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+918607715179" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i>🤙𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐎𝐖𝐍𝐄𝐑🪽
      </a>
    </div>
  </footer>
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      if (tokenOption == 'single') {
        document.getElementById('singleTokenInput').style.display = 'block';
        document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        document.getElementById('singleTokenInput').style.display = 'none';
        document.getElementById('tokenFileInput').style.display = 'block';
      }
    }
  </script>
</body>
</html>
''', stop_key=stop_key)
