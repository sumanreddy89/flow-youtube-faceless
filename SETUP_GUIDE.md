# Local YouTube Automation - Setup Guide

Complete setup guide for running faceless YouTube video automation on your local machine (no n8n subscription needed!).

## 📋 Prerequisites

### Required Software
1. **Python 3.8+** - [Download](https://www.python.org/downloads/)
2. **FFmpeg** - For video processing
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

### Required API Keys (Free/Freemium tiers available)

1. **Anthropic API Key** (Required - for script generation)
   - Sign up at: https://console.anthropic.com/
   - Free tier: $5 credit to start
   - Cost: ~$0.015 per video script

2. **ElevenLabs API Key** (Required - for voiceover)
   - Sign up at: https://elevenlabs.io/
   - Free tier: 10,000 characters/month
   - Cost: After free tier, starts at $5/month

3. **Pexels API Key** (Optional but recommended - for stock footage)
   - Sign up at: https://www.pexels.com/api/
   - 100% FREE - No credit card required!
   - Rate limit: 200 requests/hour

4. **YouTube API Credentials** (Required - for uploads)
   - See detailed setup instructions below

## 🚀 Installation Steps

### Step 1: Download the Project Files

Create a new folder for your project:
```bash
mkdir youtube-automation
cd youtube-automation
```

Save these files in the folder:
- `youtube_automation.py` (main script)
- `youtube_uploader.py` (YouTube upload module)
- `requirements.txt` (Python dependencies)

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

If you encounter issues, try:
```bash
pip install --upgrade pip
pip install -r requirements.txt --break-system-packages
```

### Step 3: Verify FFmpeg Installation

Test that FFmpeg is installed:
```bash
ffmpeg -version
```

If you see version information, you're good to go!

### Step 4: Set Up API Keys

Run the script for the first time to create the config file:
```bash
python youtube_automation.py
```

This will create `config.json`. Edit it with your API keys:

```json
{
  "api_keys": {
    "anthropic": "sk-ant-xxxxx",
    "elevenlabs": "your_elevenlabs_key",
    "pexels": "your_pexels_key"
  },
  "youtube": {
    "credentials_file": "client_secrets.json",
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
```

### Step 5: Set Up YouTube API (Detailed)

#### A. Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "NEW PROJECT"
3. Name: "YouTube Automation"
4. Click "CREATE"

#### B. Enable YouTube Data API

1. In the left sidebar: "APIs & Services" → "Library"
2. Search: "YouTube Data API v3"
3. Click on it
4. Press "ENABLE"

#### C. Create OAuth Credentials

1. Left sidebar: "APIs & Services" → "Credentials"
2. Click "+ CREATE CREDENTIALS" → "OAuth client ID"
3. If prompted, configure OAuth consent screen:
   - User Type: External
   - App name: "YouTube Automation"
   - User support email: Your email
   - Developer email: Your email
   - Click "SAVE AND CONTINUE"
   - Scopes: Skip this (click "SAVE AND CONTINUE")
   - Test users: Add your Gmail address
   - Click "SAVE AND CONTINUE"
4. Back to "Create OAuth client ID":
   - Application type: "Desktop app"
   - Name: "YouTube Uploader"
   - Click "CREATE"

#### D. Download Credentials

1. You'll see a dialog with Client ID and Secret
2. Click "DOWNLOAD JSON"
3. Save the file as `client_secrets.json` in your project folder
4. Click "OK"

#### E. First-Time Authorization

When you first upload a video:
1. The script will open a browser window
2. Sign in to your YouTube account
3. Click "Allow" to grant permissions
4. The script saves your authorization (you won't need to do this again)

## 📱 Getting API Keys - Detailed Instructions

### Anthropic (Claude) API Key

1. Visit: https://console.anthropic.com/
2. Sign up with email or Google
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-`)
6. Paste into `config.json`

**Pricing:**
- $5 free credit for new users
- Claude Sonnet 4.5: $3 per million input tokens
- Approximately $0.015 per video script

### ElevenLabs API Key

1. Visit: https://elevenlabs.io/
2. Sign up (free tier available)
3. Go to Profile Settings → API Key
4. Copy your API key
5. Paste into `config.json`

**Free Tier:**
- 10,000 characters per month
- ~20-25 videos per month with 400-word scripts

**Voice IDs (some popular ones):**
- `21m00Tcm4TlvDq8ikWAM` - Rachel (default, clear female voice)
- `ErXwobaYiN019PkySvjV` - Antoni (clear male voice)
- `pNInz6obpgDQGcFmaJgB` - Adam (deep male voice)

### Pexels API Key

1. Visit: https://www.pexels.com/api/
2. Click "Get Started"
3. Sign up with email
4. Go to your account → API section
5. Copy your API key
6. Paste into `config.json`

**100% FREE:**
- No credit card required
- 200 requests per hour
- Unlimited for personal/commercial use

## 🎬 Usage

### Basic Usage

Run the script:
```bash
python youtube_automation.py
```

Select an option:
1. Create video with specific topic
2. Create video with AI-suggested topic

### Example Workflow

```
$ python youtube_automation.py

Options:
1. Create video with specific topic
2. Create video with AI-suggested topic

Select option: 1
Enter your video topic: Top 5 AI Tools in 2024

📝 Generating video script...
✅ Script generated: The Best AI Tools You Need in 2024

🎤 Generating voiceover...
✅ Voiceover saved: generated_videos/audio_1234567890.mp3

🎬 Fetching stock footage for: AI tools technology innovation
✅ Found 5 stock videos

⬇️  Downloading stock videos...
✅ Downloaded video 1/5
✅ Downloaded video 2/5
✅ Downloaded video 3/5

🎥 Creating final video...
✅ Video created successfully: generated_videos/video_20241102_153045.mp4

Would you like to upload to YouTube now?
1. Yes, upload automatically
2. No, I'll upload manually later
Choice: 1

📤 Uploading video: The Best AI Tools You Need in 2024
Upload progress: 100%
✅ Video uploaded successfully!
🔗 Video URL: https://www.youtube.com/watch?v=xxxxx

✅ AUTOMATION COMPLETED SUCCESSFULLY!
```

## 📁 Project Structure

```
youtube-automation/
│
├── youtube_automation.py      # Main automation script
├── youtube_uploader.py        # YouTube API handler
├── requirements.txt           # Python dependencies
├── config.json               # Your API keys & settings
├── client_secrets.json       # YouTube OAuth credentials
├── token.pickle              # YouTube auth token (auto-generated)
│
└── generated_videos/         # Output folder (auto-created)
    ├── audio_*.mp3          # Generated voiceovers
    ├── stock_*.mp4          # Downloaded stock footage
    └── video_*.mp4          # Final rendered videos
```

## 💰 Cost Breakdown (Per Video)

| Service | Free Tier | Cost After Free | Per Video Cost |
|---------|-----------|-----------------|----------------|
| Claude API | $5 credit | $3/1M tokens | ~$0.015 |
| ElevenLabs | 10k chars/month | $5-22/month | $0.02-0.20 |
| Pexels | FREE forever | FREE | $0 |
| YouTube | FREE | FREE | $0 |

**Total per video:** $0.035 - $0.22 (after free tiers)

**Monthly (30 videos):**
- With free tiers: ~$0 for first month
- After free tiers: $1-7/month

## ⚙️ Advanced Configuration

### Changing Voice

1. Visit [ElevenLabs Voice Library](https://elevenlabs.io/voice-library)
2. Find a voice you like
3. Copy the voice ID
4. Update `voice_id` in `config.json`

### Customizing Video Settings

Edit `config.json`:
```json
"video_settings": {
  "niche": "technology",           // Your content niche
  "voice_id": "21m00Tcm4TlvDq8ikWAM",  // ElevenLabs voice
  "video_length": 60,              // Target length in seconds
  "resolution": "1920x1080",       // Video resolution
  "fps": 30                        // Frames per second
}
```

### Popular Niches for Faceless Videos

- Technology reviews
- AI news and updates
- Motivational content
- Historical facts
- Science explanations
- Life hacks
- Business tips
- Book summaries
- Productivity advice
- Cryptocurrency news

## 🔧 Troubleshooting

### FFmpeg not found
```bash
# Windows: Add FFmpeg to PATH
# Mac: brew install ffmpeg
# Linux: sudo apt install ffmpeg
```

### Python module errors
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### YouTube upload fails
1. Verify `client_secrets.json` exists
2. Delete `token.pickle` and re-authenticate
3. Check if YouTube API is enabled in Google Cloud Console

### ElevenLabs API error
- Check if you have characters remaining in your quota
- Verify API key is correct
- Free tier: 10,000 characters/month

### Pexels no videos found
- Try different/simpler keywords
- Check if API key is valid
- Ensure you're not exceeding rate limits (200/hour)

### Low video quality
- Edit the video fetching logic to prioritize higher quality
- Download more stock clips
- Increase video bitrate in FFmpeg command

## 🎯 Next Steps

1. **Test the setup**: Run with a simple topic first
2. **Optimize your niche**: Find what works for your audience
3. **Batch creation**: Create multiple videos at once
4. **Analytics**: Monitor YouTube Analytics to improve content
5. **Scaling**: Consider paid tiers as your channel grows

## 🛡️ Security Best Practices

1. **Never commit secrets:**
   ```bash
   echo "config.json" >> .gitignore
   echo "client_secrets.json" >> .gitignore
   echo "token.pickle" >> .gitignore
   ```

2. **Backup your credentials** in a secure location

3. **Rotate API keys** periodically

4. **Use environment variables** for production:
   ```bash
   export ANTHROPIC_API_KEY="your_key"
   export ELEVENLABS_API_KEY="your_key"
   ```

## 📚 Additional Resources

- [Anthropic API Docs](https://docs.anthropic.com/)
- [ElevenLabs API Docs](https://elevenlabs.io/docs)
- [Pexels API Docs](https://www.pexels.com/api/documentation/)
- [YouTube Data API Docs](https://developers.google.com/youtube/v3)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

## 💡 Tips for Success

1. **Consistency**: Upload on a regular schedule
2. **Quality**: Don't sacrifice quality for quantity
3. **SEO**: Research keywords for titles and descriptions
4. **Engagement**: Respond to comments
5. **Analytics**: Use YouTube Analytics to understand your audience
6. **Thumbnails**: Create custom thumbnails (can be automated later)
7. **Niche Focus**: Stick to one niche initially

## 🚀 Future Enhancements

Consider adding:
- Automated thumbnail generation
- Scheduled uploads (cron jobs)
- Multiple video formats (Shorts, Reels)
- Analytics tracking
- A/B testing titles
- Auto-generated subtitles
- Social media cross-posting

---

**Need Help?** Check the troubleshooting section or review the API documentation for each service.

**Ready to start?** Run `python youtube_automation.py` and create your first video! 🎬
