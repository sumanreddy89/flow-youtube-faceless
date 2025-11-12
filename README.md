
⸻

Faceless YouTube Video Automation (Local)

Generate and upload short, faceless YouTube videos  automatically using AI-generated scripts, AI voiceovers, and free stock footage.
Runs entirely on your local machine. No n8n, no cloud setup, no paid automation tools.

⸻

🚀 Overview

This project automates the creation of YouTube videos from start to finish using Python and open APIs.

Pipeline:
	1.	Generate a video script using Claude (Anthropic API)￼.
	2.	Create a voiceover using ElevenLabs￼.
	3.	Fetch royalty-free stock footage from Pexels API￼.
	4.	Merge video + audio using FFmpeg.
	5.	Optionally upload directly to YouTube (via OAuth credentials).

The goal: make it easy for anyone to run a faceless YouTube channel — no manual editing, no paid automation platforms.

⸻

🧩 Features

✅ Generate complete YouTube scripts (title, tags, description, keywords, body)
✅ Convert text-to-speech using realistic AI voices
✅ Fetch relevant stock video footage automatically
✅ Auto-stitch video + audio via FFmpeg
✅ Manual or automated upload to YouTube
✅ Fully local — your data and API keys stay with you

⸻

📦 Prerequisites

You’ll need:
	•	Python 3.8+
	•	FFmpeg (installed and in PATH)
	•	Free API keys for:
	•	Anthropic (Claude)￼
	•	ElevenLabs￼
	•	Pexels￼
	•	(Optional) Google API credentials for YouTube upload

⸻

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/<your-username>/faceless-youtube-automation.git
cd faceless-youtube-automation

2️⃣ Install dependencies

pip install requests anthropic

(Add YouTube upload dependencies if you plan to enable it later)

pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

3️⃣ Install FFmpeg

macOS

brew install ffmpeg

Windows
	•	Download from ffmpeg.org/download.html￼
	•	Extract → add the /bin folder to your PATH

Linux

sudo apt install ffmpeg

4️⃣ First Run (to generate config file)

python youtube_automation.py

This will create a config.json file.
Edit it and fill in your API keys.

⸻

🧠 Configuration Example

{
  "api_keys": {
    "anthropic": "sk-ant-xxxxxxxxxxxxxxxx",
    "elevenlabs": "xxxxxxxxxxxxxxxxxxxx",
    "pexels": "xxxxxxxxxxxxxxxxxxxx"
  },
  "youtube": {
    "credentials_file": "youtube_credentials.json",
    "channel_id": "YOUR_CHANNEL_ID"
  },
  "video_settings": {
    "niche": "technology",
    "voice_id": "21m00Tcm4TlvDq8ikWAM",
    "video_length": 60,
    "resolution": "1920x1080",
    "fps": 30
  }
}


⸻

🧩 How to Use

python youtube_automation.py

Then select an option:

1. Create video with specific topic
2. Create video with AI-suggested topic

The automation will:
	1.	Generate a script via Claude
	2.	Generate a voiceover (MP3) via ElevenLabs
	3.	Download 2–3 stock clips via Pexels
	4.	Merge them into a short MP4 video

All outputs are saved in:

generated_videos/
(Please create a folder for this before executing your scripts!)


⸻

🎥 Example Output

generated_videos/
├── audio_1719934258.mp3
├── stock_1719934261_0.mp4
├── stock_1719934263_1.mp4
└── video_20250721_153022.mp4


⸻

🧰 Troubleshooting

Issue	Fix
ffmpeg: command not found	Install FFmpeg and add it to PATH
anthropic.error.AuthenticationError	Check your API key in config.json
Voice sounds robotic	Try another voice_id from your ElevenLabs dashboard
No stock videos found	Check your Pexels API key or keywords
Upload fails	You can upload manually via YouTube Studio


⸻

🧱 Project Structure

.
├── youtube_automation.py      # Main script
├── config.json                # Your API keys & settings
├── generated_videos/          # Output folder
└── README.md                  # Documentation


⸻

🪄 Coming Soon
	•	Smarter visual selection (scene-based)
	•	AI image fallback for abstract topics
	•	Automated upload to YouTube
	•	Background scheduling for daily posting
	•	GUI version (no command line required)

⸻

📝 License

MIT License © 2025 [Suman Reddy]
Feel free to modify, improve, and share!

⸻
