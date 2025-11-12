#!/usr/bin/env python3
"""
Faceless YouTube Video Automation - Local Version
No n8n required - runs completely on your local machine
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
import requests
from anthropic import Anthropic
import subprocess
import tempfile

# Configuration
CONFIG_FILE = "config.json"
VIDEOS_DIR = Path("generated_videos")
VIDEOS_DIR.mkdir(exist_ok=True)

class YouTubeAutomation:
    def __init__(self):
        self.config = self.load_config()
        self.anthropic_client = Anthropic(api_key=self.config['api_keys']['anthropic'])
        
    def load_config(self):
        """Load configuration from config.json"""
        if not os.path.exists(CONFIG_FILE):
            print(f"❌ {CONFIG_FILE} not found. Creating template...")
            self.create_config_template()
            print(f"✅ Please edit {CONFIG_FILE} with your API keys and settings")
            exit(1)
        
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    
    def create_config_template(self):
        """Create a config template file"""
        template = {
            "api_keys": {
                "anthropic": "YOUR_ANTHROPIC_API_KEY",
                "elevenlabs": "YOUR_ELEVENLABS_API_KEY",
                "pexels": "YOUR_PEXELS_API_KEY"
            },
            "youtube": {
                "credentials_file": "youtube_credentials.json",
                "channel_id": "YOUR_CHANNEL_ID"
            },
            "video_settings": {
                "niche": "technology",
                "voice_id": "21m00Tcm4TlvDq8ikWAM",
                "video_length": 30,
                "resolution": "1920x1080",
                "fps": 30
            },
            "schedule": {
                "enabled": False,
                "time": "09:00",
                "days": ["monday", "wednesday", "friday"]
            }
        }
        
        with open(CONFIG_FILE, 'w') as f:
            json.dump(template, f, indent=2)
    
    def generate_script(self, topic=None):
        """Generate video script using Claude"""
        print("\n📝 Generating video script...")
        
        if not topic:
            topic = input("Enter video topic (or press Enter for AI suggestion): ").strip()
        
        prompt = f"""Create a compelling YouTube SHORT video script about: {topic if topic else 'a trending topic in ' + self.config['video_settings']['niche']}

CRITICAL REQUIREMENTS:
- Length: 150-200 words MAXIMUM (for ~30 seconds of natural speech)
- Style: Direct, conversational, factual - speak naturally as if talking to a friend
- NO meta-language: Never say "title", "description", "keywords", "script", "this video", "today we'll discuss"
- Start immediately with the CONTENT - no preamble or introduction
- Be SPECIFIC and FACTUAL - include real data, statistics, concrete benefits, or examples
- End with a strong value statement - summarize what they just learned
- NO generic CTAs like "subscribe", "hit the bell", or "comment below"

FORMAT (use these exact labels):
TITLE: [Compelling, curiosity-driven title under 60 characters]
DESCRIPTION: [2-3 sentences with key points, include relevant #hashtags]
TAGS: [8-10 relevant single-word tags separated by commas]
KEYWORDS: [3-5 descriptive phrases for stock footage - be specific like "person meditating peaceful nature sunset" not just "meditation"]
SCRIPT:
[Direct narration only - NO labels, NO meta-talk, just pure content]

GOOD EXAMPLE (meditation topic):
"Meditation reduces cortisol by 30% in just 8 weeks. It physically increases gray matter in your brain, boosting memory and emotional control. Even 10 minutes daily lowers blood pressure and anxiety significantly. Your brain literally rewires itself to handle stress better."

BAD EXAMPLE (avoid this):
"Hey everyone, today's video is about meditation. Let me tell you why meditation matters. First, meditation has benefits. It's really important for your health. Thanks for watching, don't forget to subscribe!"

Now create the script following the GOOD example style:

Example of what the SCRIPT section should look like:
Did you know that just 10 minutes of meditation can change your entire day? Today I'm sharing five powerful meditation techniques that actually work...

[Continue with 400-500 words of engaging narration]
"""
        
        message = self.anthropic_client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        content = message.content[0].text
        script_data = self.parse_script(content)
        
        print(f"✅ Script generated: {script_data['title']}")
        print(f"   Keywords: {script_data['keywords']}")
        print(f"   Script length: {len(script_data['script'])} characters")
        return script_data
    
    def parse_script(self, content):
        """Parse the Claude response into structured data"""
        lines = content.split('\n')
        data = {
            'title': '',
            'description': '',
            'tags': [],
            'keywords': '',
            'script': ''
        }
        
        script_started = False
        script_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('TITLE:'):
                data['title'] = line.replace('TITLE:', '').strip()
            elif line.startswith('DESCRIPTION:'):
                data['description'] = line.replace('DESCRIPTION:', '').strip()
            elif line.startswith('TAGS:'):
                tags_str = line.replace('TAGS:', '').strip()
                data['tags'] = [t.strip() for t in tags_str.split(',')]
            elif line.startswith('KEYWORDS:'):
                data['keywords'] = line.replace('KEYWORDS:', '').strip()
            elif line.startswith('SCRIPT:'):
                script_started = True
            elif script_started:
                script_lines.append(line)
        
        data['script'] = '\n'.join(script_lines).strip()
        
        # Fallback: if no structured data found, try to extract from content
        if not data['title'] or not data['script']:
            # Just use the whole content as script if parsing failed
            data['script'] = content.strip()
            # Generate basic metadata
            data['title'] = content[:100].strip().split('\n')[0] if content else "AI Generated Video"
            data['keywords'] = "ai content technology"
            data['tags'] = ["AI", "Technology", "Education"]
            data['description'] = content[:200].strip() if len(content) > 200 else content.strip()
        
        return data
    
    def generate_voiceover(self, script_text):
        """Generate voiceover using ElevenLabs API"""
        print("\n🎤 Generating voiceover...")
        
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.config['video_settings']['voice_id']}"
        
        headers = {
            "xi-api-key": self.config['api_keys']['elevenlabs'],
            "Content-Type": "application/json"
        }
        
        data = {
            "text": script_text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            audio_path = VIDEOS_DIR / f"audio_{int(time.time())}.mp3"
            with open(audio_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ Voiceover saved: {audio_path}")
            return audio_path
        else:
            print(f"❌ Error generating voiceover: {response.status_code}")
            print(response.text)
            return None
    
    def fetch_stock_footage(self, keywords, num_videos=5):
        """Fetch stock videos from Pexels"""
        print(f"\n🎬 Fetching stock footage for: {keywords}")
        
        url = "https://api.pexels.com/videos/search"
        headers = {
            "Authorization": self.config['api_keys']['pexels']
        }
        params = {
            "query": keywords,
            "per_page": num_videos,
            "orientation": "landscape"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            videos = response.json().get('videos', [])
            video_urls = []
            
            for video in videos:
                # Get highest quality video file
                video_files = video.get('video_files', [])
                if video_files:
                    # Sort by quality (width)
                    best_quality = max(video_files, key=lambda x: x.get('width', 0))
                    video_urls.append(best_quality['link'])
            
            print(f"✅ Found {len(video_urls)} stock videos")
            return video_urls
        else:
            print(f"❌ Error fetching stock footage: {response.status_code}")
            return []
    
    def download_videos(self, urls):
        """Download stock videos"""
        print("\n⬇️  Downloading stock videos...")
        downloaded_files = []
        
        # Download more videos for variety (5 instead of 3)
        for i, url in enumerate(urls[:5]):
            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    # Use timestamp to ensure unique filenames
                    video_path = VIDEOS_DIR / f"stock_{int(time.time())}_{i}_{hash(url) % 10000}.mp4"
                    with open(video_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    downloaded_files.append(video_path)
                    print(f"✅ Downloaded video {i+1}/{min(len(urls), 5)}")
                time.sleep(0.5)  # Shorter delay
            except Exception as e:
                print(f"⚠️  Failed to download video {i+1}: {e}")
        
        return downloaded_files
    
    def create_video(self, audio_path, video_files, script_data):
        """Create final video using FFmpeg"""
        print("\n🎥 Creating final video...")
        
        output_filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        output_path = VIDEOS_DIR / output_filename
        
        # Get audio duration
        duration_cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{audio_path}"'
        duration = float(subprocess.check_output(duration_cmd, shell=True).decode().strip())
        
        if not video_files:
            print("⚠️  No video files available, creating video with solid background...")
            # Create video with solid color background and text
            cmd = f'''ffmpeg -f lavfi -i color=c=black:s=1920x1080:d={duration} -i "{audio_path}" \
                -c:v libx264 -c:a aac -shortest -y "{output_path}"'''
        else:
            # Create concat file for multiple videos
            concat_file = VIDEOS_DIR / "concat_list.txt"
            with open(concat_file, 'w') as f:
                for video_file in video_files:
                    f.write(f"file '{video_file.absolute()}'\n")
            
            # Concatenate videos and add audio
            temp_video = VIDEOS_DIR / "temp_concat.mp4"
            
            # First, concatenate videos
            concat_cmd = f'ffmpeg -f concat -safe 0 -i "{concat_file}" -c copy -y "{temp_video}"'
            subprocess.run(concat_cmd, shell=True, check=True)
            
            # Then, trim to audio length and add audio
            cmd = f'''ffmpeg -i "{temp_video}" -i "{audio_path}" \
                -t {duration} -c:v libx264 -c:a aac -shortest -y "{output_path}"'''
        
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"✅ Video created successfully: {output_path}")
            
            # Cleanup
            if video_files:
                temp_video.unlink(missing_ok=True)
                concat_file.unlink(missing_ok=True)
            
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"❌ Error creating video: {e}")
            return None
    
    def upload_to_youtube(self, video_path, script_data):
        """Upload video to YouTube using official Google API"""
        print("\n📤 Uploading to YouTube...")
        
        try:
            from youtube_uploader import YouTubeUploader
            
            uploader = YouTubeUploader(self.config['youtube']['credentials_file'])
            
            video_id = uploader.upload_video(
                video_file=str(video_path),
                title=script_data['title'],
                description=script_data['description'],
                tags=script_data['tags'],
                category='22',  # People & Blogs
                privacy='public'
            )
            
            if video_id:
                return f"https://youtube.com/watch?v={video_id}"
            return None
            
        except ImportError:
            print("❌ youtube_uploader module not found")
            print(f"\nVideo ready for manual upload:")
            print(f"   File: {video_path}")
            print(f"   Title: {script_data['title']}")
            print(f"   Description: {script_data['description']}")
            print(f"   Tags: {', '.join(script_data['tags'])}")
            return None
        except Exception as e:
            print(f"❌ Error uploading to YouTube: {e}")
            print(f"\nVideo ready for manual upload:")
            print(f"   File: {video_path}")
            return None
    
    def run_full_automation(self, topic=None):
        """Run the complete automation pipeline"""
        print("=" * 60)
        print("🤖 YOUTUBE AUTOMATION PIPELINE STARTED")
        print("=" * 60)
        
        try:
            # Step 1: Generate script
            script_data = self.generate_script(topic)
            
            # Step 2: Generate voiceover
            audio_path = self.generate_voiceover(script_data['script'])
            if not audio_path:
                return False
            
            # Step 3: Fetch stock footage
            video_urls = self.fetch_stock_footage(script_data['keywords'])
            
            # Step 4: Download videos
            video_files = self.download_videos(video_urls) if video_urls else []
            
            # Step 5: Create final video
            final_video = self.create_video(audio_path, video_files, script_data)
            if not final_video:
                return False
            
            # Step 6: Upload to YouTube
            print("\n" + "=" * 60)
            print("Would you like to upload to YouTube now?")
            print("1. Yes, upload automatically")
            print("2. No, I'll upload manually later")
            choice = input("Choice (1/2): ").strip()
            
            if choice == '1':
                self.upload_to_youtube(final_video, script_data)
            else:
                print(f"\n✅ Video ready for manual upload:")
                print(f"   File: {final_video}")
                print(f"   Title: {script_data['title']}")
                print(f"   Description: {script_data['description']}")
                print(f"   Tags: {', '.join(script_data['tags'])}")
            
            print("\n" + "=" * 60)
            print("✅ AUTOMATION COMPLETED SUCCESSFULLY!")
            print("=" * 60)
            return True
            
        except Exception as e:
            print(f"\n❌ Error in automation pipeline: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main entry point"""
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║   FACELESS YOUTUBE VIDEO AUTOMATION (LOCAL)          ║
    ║   No n8n required - Runs on your machine!           ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    
    automation = YouTubeAutomation()
    
    print("\nOptions:")
    print("1. Create video with specific topic")
    print("2. Create video with AI-suggested topic")
    print("3. Run scheduled automation (coming soon)")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == '1':
        topic = input("Enter your video topic: ").strip()
        automation.run_full_automation(topic)
    elif choice == '2':
        automation.run_full_automation()
    elif choice == '3':
        print("⏰ Scheduled automation will be available in the next version!")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()