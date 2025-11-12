@echo off
REM Quick Start Installation Script for YouTube Automation (Windows)

echo ╔═══════════════════════════════════════════════════════╗
echo ║   YOUTUBE AUTOMATION - QUICK SETUP (WINDOWS)         ║
echo ╚═══════════════════════════════════════════════════════╝
echo.

REM Check Python installation
echo 🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    echo    Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% found
echo.

REM Check FFmpeg installation
echo 🔍 Checking FFmpeg installation...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo ❌ FFmpeg not found
    echo.
    echo Please install FFmpeg:
    echo   1. Download from: https://ffmpeg.org/download.html
    echo   2. Extract to C:\ffmpeg
    echo   3. Add C:\ffmpeg\bin to your PATH
    echo.
    pause
    exit /b 1
)

echo ✅ FFmpeg found
echo.

REM Install Python dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ⚠️  Standard installation failed. Trying alternative method...
    pip install -r requirements.txt --user
)

echo.
echo ✅ Installation complete!
echo.
echo ═══════════════════════════════════════════════════════
echo NEXT STEPS:
echo ═══════════════════════════════════════════════════════
echo.
echo 1. Get your API keys:
echo    • Anthropic: https://console.anthropic.com/
echo    • ElevenLabs: https://elevenlabs.io/
echo    • Pexels: https://www.pexels.com/api/
echo.
echo 2. Set up YouTube API credentials:
echo    • Follow instructions in SETUP_GUIDE.md
echo    • Save as 'client_secrets.json'
echo.
echo 3. Run the automation:
echo    python youtube_automation.py
echo.
echo 📖 For detailed instructions, see: SETUP_GUIDE.md
echo.
pause
