# 🚀 QUICK START CARD

## Installation (5 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create config
python youtube_automation.py
# This creates config.json template

# 3. Add your API keys to config.json
# Get keys from:
# - Anthropic: console.anthropic.com
# - ElevenLabs: elevenlabs.io
# - Pexels: pexels.com/api

# 4. Set up YouTube OAuth
# See SETUP_GUIDE.md for detailed steps
# Save as client_secrets.json
```

## First Video (2 minutes)

```bash
python youtube_automation.py
```

Select option → Enter topic → Wait for magic! ✨

## 📝 File Checklist

- [ ] `youtube_automation.py` - Main script
- [ ] `youtube_uploader.py` - Upload handler
- [ ] `requirements.txt` - Dependencies
- [ ] `config.json` - YOUR API keys (create from template)
- [ ] `client_secrets.json` - YOUR YouTube OAuth (download from Google)

## 🔑 Required API Keys

| Service | Link | Free Tier |
|---------|------|-----------|
| Anthropic | console.anthropic.com | $5 credit |
| ElevenLabs | elevenlabs.io | 10k chars/month |
| Pexels | pexels.com/api | FREE forever |
| YouTube | Google Cloud Console | FREE |

## 💰 Cost Per Video

- **Within free tiers**: $0
- **After free tiers**: $0.035 - $0.22

**Way cheaper than n8n Cloud ($20-50/month)!**

## ⚡ Quick Commands

```bash
# Create video
python youtube_automation.py

# Test YouTube auth
python youtube_uploader.py

# Check FFmpeg
ffmpeg -version
```

## 🐛 Common Issues

**FFmpeg not found?**
- Windows: Download + add to PATH
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

**Python errors?**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

**YouTube upload fails?**
1. Check `client_secrets.json` exists
2. Delete `token.pickle`
3. Re-run script to re-authenticate

## 📊 Workflow Overview

```
1. Generate Script (Claude AI)
   ↓
2. Create Voiceover (ElevenLabs)
   ↓
3. Fetch Stock Footage (Pexels)
   ↓
4. Combine into Video (FFmpeg)
   ↓
5. Upload to YouTube (Google API)
   ↓
6. Done! 🎉
```

## 🎯 Tips for Success

✅ Start with 1 video/day
✅ Stick to one niche
✅ Check YouTube Analytics
✅ Optimize based on data
✅ Scale gradually

## 🔒 Security Reminder

**NEVER commit these files:**
- `config.json`
- `client_secrets.json`
- `token.pickle`

Add to `.gitignore` (already included!)

## 📚 Need Help?

1. Check `README.md` for overview
2. Read `SETUP_GUIDE.md` for details
3. Review API documentation

## 🎬 That's It!

You now have a fully automated YouTube video creation system running locally on your machine!

**No monthly fees. Complete control. Total privacy.**

Run `python youtube_automation.py` to start! 🚀
