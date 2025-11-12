#!/bin/bash
# Quick Start Installation Script for YouTube Automation

echo "╔═══════════════════════════════════════════════════════╗"
echo "║   YOUTUBE AUTOMATION - QUICK SETUP                   ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Check Python installation
echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+ first."
    echo "   Download from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION found"

# Check FFmpeg installation
echo ""
echo "🔍 Checking FFmpeg installation..."
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg not found"
    echo ""
    echo "Please install FFmpeg:"
    echo "  • Windows: Download from https://ffmpeg.org/download.html"
    echo "  • Mac:     brew install ffmpeg"
    echo "  • Linux:   sudo apt install ffmpeg"
    exit 1
fi

FFMPEG_VERSION=$(ffmpeg -version | head -n1 | cut -d' ' -f3)
echo "✅ FFmpeg $FFMPEG_VERSION found"

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "⚠️  Standard installation failed. Trying alternative method..."
    pip3 install -r requirements.txt --break-system-packages
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "═══════════════════════════════════════════════════════"
echo "NEXT STEPS:"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "1. Get your API keys:"
echo "   • Anthropic: https://console.anthropic.com/"
echo "   • ElevenLabs: https://elevenlabs.io/"
echo "   • Pexels: https://www.pexels.com/api/"
echo ""
echo "2. Set up YouTube API credentials:"
echo "   • Follow instructions in SETUP_GUIDE.md"
echo "   • Save as 'client_secrets.json'"
echo ""
echo "3. Run the automation:"
echo "   python3 youtube_automation.py"
echo ""
echo "📖 For detailed instructions, see: SETUP_GUIDE.md"
echo ""
