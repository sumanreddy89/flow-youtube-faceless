# ✅ Installation Checklist

Use this checklist to ensure you have everything set up correctly.

## 📥 Phase 1: Download & Prerequisites (10 minutes)

### Files Downloaded
- [ ] All project files downloaded
- [ ] Files extracted to a folder (e.g., `youtube-automation`)

### Software Installed
- [ ] Python 3.8 or higher installed
  ```bash
  python --version  # or python3 --version
  # Should show: Python 3.8.x or higher
  ```

- [ ] FFmpeg installed and in PATH
  ```bash
  ffmpeg -version
  # Should show version info
  ```
  
  **If FFmpeg not found:**
  - Windows: Download from ffmpeg.org, add to PATH
  - Mac: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`

### Python Dependencies
- [ ] Dependencies installed
  ```bash
  pip install -r requirements.txt
  # or: pip3 install -r requirements.txt
  ```

- [ ] No errors during installation
  - If errors occur, try: `pip install --upgrade pip` first

---

## 🔑 Phase 2: API Keys Setup (15 minutes)

### Anthropic (Claude)
- [ ] Account created at console.anthropic.com
- [ ] API key generated
- [ ] API key copied (starts with `sk-ant-`)
- [ ] $5 free credit visible in account

### ElevenLabs
- [ ] Account created at elevenlabs.io
- [ ] Free plan activated (10,000 chars/month)
- [ ] API key found in Profile → API Key
- [ ] API key copied
- [ ] Voice ID noted (default: `21m00Tcm4TlvDq8ikWAM`)

### Pexels (Optional but Recommended)
- [ ] Account created at pexels.com/api
- [ ] API key generated (100% free)
- [ ] API key copied

### Configuration File
- [ ] Run script once to create template:
  ```bash
  python youtube_automation.py
  ```
- [ ] config.json file created
- [ ] All API keys pasted into config.json
- [ ] Niche set in config.json
- [ ] Voice ID set in config.json

---

## 🎥 Phase 3: YouTube Setup (20 minutes)

### Google Cloud Console
- [ ] Visited console.cloud.google.com
- [ ] New project created
  - Project name: _______________
  - Project ID: _______________

### Enable API
- [ ] YouTube Data API v3 enabled
  - Path: APIs & Services → Library → YouTube Data API v3 → Enable

### OAuth Consent Screen
- [ ] Consent screen configured
  - User Type: External
  - App name: _______________
  - Support email: _______________
  - Developer email: _______________
- [ ] Scopes: Skipped (default is fine)
- [ ] Test users: Your Gmail added
- [ ] Save and continue completed

### OAuth Client
- [ ] OAuth Client ID created
  - Application type: Desktop app
  - Name: _______________
- [ ] Client ID shown
- [ ] JSON file downloaded
- [ ] JSON renamed to `client_secrets.json`
- [ ] File placed in project folder

### First Authentication
- [ ] Run script for first upload attempt
- [ ] Browser opened automatically
- [ ] Signed in to YouTube account
- [ ] Permissions granted
- [ ] `token.pickle` file created
- [ ] No more authentication needed

---

## 🧪 Phase 4: Testing (10 minutes)

### Initial Test
- [ ] Run main script:
  ```bash
  python youtube_automation.py
  ```
- [ ] Script starts without errors
- [ ] Menu appears with options

### Test Script Generation
- [ ] Option 1 or 2 selected
- [ ] Topic entered (if Option 1)
- [ ] Claude API responds
- [ ] Script generated successfully
- [ ] Title, description, tags shown

### Test Voiceover
- [ ] ElevenLabs API responds
- [ ] Audio file saved in `generated_videos/`
- [ ] Audio plays correctly (optional: test with media player)

### Test Stock Footage
- [ ] Pexels API responds (if configured)
- [ ] Video URLs found
- [ ] Videos downloaded to `generated_videos/`

### Test Video Creation
- [ ] FFmpeg processes without errors
- [ ] Final video created in `generated_videos/`
- [ ] Video plays correctly
- [ ] Audio synced with video

### Test YouTube Upload (Optional)
- [ ] Upload option selected
- [ ] OAuth authentication works (or token used)
- [ ] Upload progress shown
- [ ] Video uploaded successfully
- [ ] YouTube URL provided
- [ ] Video visible on YouTube channel

---

## 🔒 Phase 5: Security (5 minutes)

### Protected Files
- [ ] `.gitignore` file present
- [ ] Following files in .gitignore:
  - config.json
  - client_secrets.json
  - token.pickle
  - generated_videos/

### If Using Git
- [ ] Repository initialized (optional)
- [ ] Sensitive files NOT committed
- [ ] Check status:
  ```bash
  git status
  # Should NOT show config.json, client_secrets.json, token.pickle
  ```

### Backup
- [ ] Config files backed up securely
- [ ] Backup NOT in public location
- [ ] API keys stored securely

---

## 📊 Phase 6: First Real Video (15 minutes)

### Preparation
- [ ] Video topic chosen
- [ ] Target audience identified
- [ ] Keywords researched (for title/description)

### Creation
- [ ] Script reviewed and approved
- [ ] Video created successfully
- [ ] Quality checked
  - Video resolution: 1080p
  - Audio clear and natural
  - No sync issues

### Metadata
- [ ] Title optimized for SEO
- [ ] Description includes keywords
- [ ] Tags relevant and specific
- [ ] Thumbnail planned (manual for now)

### Publishing
- [ ] Video uploaded (auto or manual)
- [ ] Visibility set (public/unlisted/private)
- [ ] Thumbnail uploaded (if ready)
- [ ] Published successfully

### Verification
- [ ] Video plays on YouTube
- [ ] Audio/video quality good
- [ ] Description formatted correctly
- [ ] Tags visible

---

## 📈 Phase 7: Optimization (Ongoing)

### First Week
- [ ] Create 1 video per day
- [ ] Monitor performance
- [ ] Check YouTube Analytics
- [ ] Note what works best

### Performance Tracking
- [ ] Views tracked
- [ ] Watch time noted
- [ ] Engagement measured (likes, comments)
- [ ] Click-through rate checked

### Improvements
- [ ] Titles optimized based on data
- [ ] Thumbnails A/B tested
- [ ] Voice adjusted if needed
- [ ] Script style refined

---

## 💡 Troubleshooting Checklist

### If Script Fails
- [ ] Check internet connection
- [ ] Verify API keys in config.json
- [ ] Check API quotas/limits
- [ ] Review error messages
- [ ] Check SETUP_GUIDE.md troubleshooting section

### If FFmpeg Fails
- [ ] Verify FFmpeg installation
- [ ] Check PATH environment variable
- [ ] Test FFmpeg in terminal
- [ ] Check disk space

### If Upload Fails
- [ ] Verify client_secrets.json exists
- [ ] Delete token.pickle and re-authenticate
- [ ] Check YouTube API quota
- [ ] Verify video file isn't corrupted

### If Audio Quality Poor
- [ ] Check ElevenLabs settings
- [ ] Try different voice
- [ ] Adjust stability/similarity settings
- [ ] Verify script text quality

---

## 📋 Quick Reference

### Key Files Location
```
youtube-automation/
├── youtube_automation.py      # Main script
├── youtube_uploader.py        # Upload module
├── config.json               # YOUR KEYS HERE
├── client_secrets.json       # YOUTUBE OAUTH
├── token.pickle              # AUTO-GENERATED
└── generated_videos/         # OUTPUT FOLDER
```

### Essential Commands
```bash
# Create video
python youtube_automation.py

# Test YouTube auth
python youtube_uploader.py

# Install dependencies
pip install -r requirements.txt

# Check versions
python --version
ffmpeg -version
```

### Cost Reminder
- First month: $0 (free tiers)
- After: $1-7/month for 30 videos
- Way cheaper than n8n ($20-50/month)

---

## ✅ Final Verification

Before considering setup complete:
- [ ] Created at least 1 test video successfully
- [ ] Video uploaded to YouTube (or ready for manual upload)
- [ ] All API keys working
- [ ] No error messages
- [ ] File structure correct
- [ ] Security measures in place
- [ ] Documentation reviewed

### You're Ready When:
- ✅ Can create video with one command
- ✅ Process completes without errors
- ✅ Output quality is acceptable
- ✅ Upload works (auto or manual)
- ✅ Understand the workflow
- ✅ Know where to get help (SETUP_GUIDE.md)

---

## 🎉 Congratulations!

If all items are checked, you now have a fully functional YouTube automation system!

### Next Steps:
1. Create your first real video
2. Publish to your channel
3. Monitor analytics
4. Optimize based on data
5. Scale gradually

### Need Help?
- Check SETUP_GUIDE.md for detailed instructions
- Review README.md for troubleshooting
- See QUICKSTART.md for quick commands
- Read API documentation if needed

---

**Total Setup Time: ~60-70 minutes**
**Time Per Video After Setup: ~5-10 minutes**

**Good luck with your automated YouTube channel! 🚀**

---

*Save this checklist and refer back to it when setting up on a new machine or helping others get started.*
