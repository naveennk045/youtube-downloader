# YouTube Downloader Pro 🎬

A modern, feature-rich desktop application for downloading YouTube videos and playlists with HD quality support.

## Features ✨

- 🎥 Download single videos and entire playlists
- 🎯 Multiple quality options (360p to 4K)
- 📋 Queue management with pause/resume
- 🧵 Multi-threaded downloads
- 🎨 Modern, colorful UI
- 📊 Real-time progress tracking
- 💾 Custom download location
- 🔄 FFmpeg integration for video conversion

## Installation 🚀

### Prerequisites

1. **Python 3.8+** - [Download](https://www.python.org/downloads/)
2. **FFmpeg** - Required for video conversion

#### Installing FFmpeg:

**Windows:**

FFmpeg - [Download](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z)


**Linux:**
```
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```
brew install ffmpeg
```

### Setup Application

1. **Clone or download the project**

2. **Install dependencies:**
```
pip install -r requirements.txt
```

3. **Run the application:**
```
python main.py
```

## Converting to EXE 📦

### Using PyInstaller

1. **Install PyInstaller:**
```
pip install pyinstaller
```

2. **Create EXE (Single File):**
```
pyinstaller --onefile --windowed --name="YouTubeDownloader" --icon=icon.ico main.py
```

3. **Create EXE (With Dependencies Folder):**
```
pyinstaller --onedir --windowed --name="YouTubeDownloader" --icon=icon.ico main.py
```

### Important Notes for EXE:

- The EXE will be created in the `dist/` folder
- **Include FFmpeg**: Copy `ffmpeg.exe` to the same folder as your EXE
- For single-file EXE, use `--add-binary` option:
```
pyinstaller --onefile --windowed --add-binary "path/to/ffmpeg.exe;." main.py
```

### Advanced PyInstaller Options:

```
pyinstaller \
  --onefile \
  --windowed \
  --name="YouTubeDownloaderPro" \
  --icon=app_icon.ico \
  --add-data "src;src" \
  --hidden-import=yt_dlp \
  --hidden-import=customtkinter \
  main.py
```

## Usage Guide 📖

### Downloading a Video:

1. Copy YouTube video URL
2. Paste into the URL field
3. Select quality (360p to 4K)
4. Choose download location
5. Click "Add to Queue"
6. Click "▶ Start All"

### Downloading a Playlist:

1. Copy YouTube playlist URL
2. Paste into the URL field
3. Configure quality and location
4. Click "Add to Queue"
5. All videos will be added to queue
6. Click "▶ Start All"

### Queue Management:

- **Start All**: Begin all pending downloads
- **Pause All**: Pause active downloads
- **Clear**: Remove completed downloads
- **✕ Button**: Remove individual items

## Troubleshooting 🔧

### "FFmpeg not found" error:
- Ensure FFmpeg is installed and in PATH
- Test by running `ffmpeg -version` in terminal

### Download fails:
- Check internet connection
- Verify URL is valid
- Some videos may have restrictions

### EXE doesn't work:
- Include FFmpeg with the EXE
- Check Windows Defender/Antivirus
- Run from command prompt to see errors

## Project Structure 📁

```
youtube_downloader/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── src/
│   ├── ui/                # User interface components
│   │   ├── main_window.py
│   │   ├── download_item.py
│   │   └── styles.py
│   ├── core/              # Core functionality
│   │   ├── downloader.py
│   │   └── queue_manager.py
│   └── utils/             # Utility functions
│       ├── validators.py
│       └── logger.py
├── downloads/             # Default download folder
└── logs/                  # Application logs
```

## Dependencies 📚

- **customtkinter** - Modern UI framework
- **yt-dlp** - YouTube download engine
- **Pillow** - Image processing
- **requests** - HTTP library

## License 📄

This project is for educational purposes. Respect YouTube's Terms of Service and copyright laws.

## Credits 👏

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- UI powered by [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Video processing by [FFmpeg](https://ffmpeg.org/)

To download FFmpeg : [Download](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z)

## Quick Start Commands

### Installation:
```bash
pip install -r requirements.txt
```

### Run Application:
```bash
python main.py
```

### Build EXE:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="YouTubeDownloader" main.py
```
