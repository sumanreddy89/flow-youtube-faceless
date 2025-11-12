#!/usr/bin/env python3
"""
YouTube Upload Module
Handles authentication and uploading videos to YouTube
"""

import os
import pickle
import json
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

class YouTubeUploader:
    def __init__(self, credentials_file='client_secrets.json'):
        self.credentials_file = credentials_file
        self.token_file = 'token.pickle'
        self.youtube = None
        
    def authenticate(self):
        """Authenticate with YouTube API"""
        creds = None
        
        # Token file stores the user's access and refresh tokens
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)
        
        # If no valid credentials, let user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    print(f"\n❌ OAuth credentials file not found: {self.credentials_file}")
                    print("\n📝 To get your credentials:")
                    print("1. Go to https://console.cloud.google.com/")
                    print("2. Create a new project (or select existing)")
                    print("3. Enable YouTube Data API v3")
                    print("4. Create OAuth 2.0 credentials (Desktop app)")
                    print("5. Download JSON and save as 'client_secrets.json'")
                    return False
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for next run
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)
        
        self.youtube = build('youtube', 'v3', credentials=creds)
        return True
    
    def upload_video(self, video_file, title, description, tags, category='22', 
                    privacy='public', notify_subscribers=True):
        """
        Upload video to YouTube
        
        Args:
            video_file: Path to video file
            title: Video title
            description: Video description
            tags: List of tags
            category: YouTube category ID (22 = People & Blogs)
            privacy: 'public', 'private', or 'unlisted'
            notify_subscribers: Whether to notify subscribers
        
        Returns:
            Video ID if successful, None otherwise
        """
        if not self.youtube:
            if not self.authenticate():
                return None
        
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': category
            },
            'status': {
                'privacyStatus': privacy,
                'selfDeclaredMadeForKids': False,
            },
            'notifySubscribers': notify_subscribers
        }
        
        # Create media upload object
        media = MediaFileUpload(
            video_file,
            mimetype='video/*',
            resumable=True,
            chunksize=1024*1024  # 1MB chunks
        )
        
        try:
            print(f"\n📤 Uploading video: {title}")
            print("This may take a few minutes...")
            
            # Call the API's videos.insert method
            request = self.youtube.videos().insert(
                part=','.join(body.keys()),
                body=body,
                media_body=media
            )
            
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    progress = int(status.progress() * 100)
                    print(f"Upload progress: {progress}%", end='\r')
            
            video_id = response['id']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            print(f"\n✅ Video uploaded successfully!")
            print(f"🔗 Video URL: {video_url}")
            print(f"📊 Video ID: {video_id}")
            
            return video_id
            
        except HttpError as e:
            print(f"\n❌ An HTTP error occurred: {e}")
            return None
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            return None
    
    def update_thumbnail(self, video_id, thumbnail_file):
        """Upload custom thumbnail for video"""
        if not self.youtube:
            if not self.authenticate():
                return False
        
        try:
            self.youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_file)
            ).execute()
            print(f"✅ Thumbnail updated for video {video_id}")
            return True
        except HttpError as e:
            print(f"❌ Error updating thumbnail: {e}")
            return False


def setup_youtube_credentials():
    """Interactive setup for YouTube credentials"""
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║         YOUTUBE API CREDENTIALS SETUP                ║
    ╚═══════════════════════════════════════════════════════╝
    
    To upload videos to YouTube, you need OAuth 2.0 credentials.
    
    📝 Step-by-step guide:
    
    1. Go to: https://console.cloud.google.com/
    
    2. Create a new project:
       - Click "Select a project" → "New Project"
       - Name it (e.g., "YouTube Automation")
       - Click "Create"
    
    3. Enable YouTube Data API v3:
       - Go to "APIs & Services" → "Library"
       - Search for "YouTube Data API v3"
       - Click on it and press "Enable"
    
    4. Create OAuth credentials:
       - Go to "APIs & Services" → "Credentials"
       - Click "Create Credentials" → "OAuth client ID"
       - Choose "Desktop app" as application type
       - Name it (e.g., "YouTube Uploader")
       - Click "Create"
    
    5. Download credentials:
       - Click the download button (⬇️) next to your new OAuth client
       - Save the JSON file as 'client_secrets.json'
       - Place it in the same folder as this script
    
    6. First-time authorization:
       - Run the script again
       - A browser window will open
       - Sign in to your YouTube account
       - Grant the requested permissions
       - The script will save your token for future use
    
    ⚠️  IMPORTANT:
    - Keep client_secrets.json and token.pickle private
    - Never commit these files to public repositories
    - Add them to your .gitignore file
    """)


if __name__ == "__main__":
    # Test the uploader
    setup_youtube_credentials()
