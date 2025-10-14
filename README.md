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
```
# Using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
# Add to PATH environment variable
```

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
```

## Additional Files

### **src/__init__.py** (Empty file for package)

```python
# src package
```

### **src/ui/__init__.py**

```python
# UI package
```

### **src/core/__init__.py**

```python
# Core package
```

### **src/utils/__init__.py**

```python
# Utils package
```

***

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

This application provides a complete, production-ready YouTube downloader with modern UI, robust threading, modular architecture, and easy conversion to a Windows executable. The colorful interface uses CustomTkinter for a contemporary look, while yt-dlp handles all download operations efficiently. The multi-threaded architecture ensures smooth operation even when downloading multiple videos simultaneously.[1][2][3][4][5][6][7][8]

[1](https://ostechnix.com/yt-dlp-tutorial/)
[2](https://abdulrahmanh.com/blog/youtube-downloader)
[3](https://customtkinter.tomschimansky.com)
[4](https://www.pyinstaller.org)
[5](https://www.youtube.com/watch?v=xoOxclR3XPc)
[6](https://dev.to/niveshbansal07/download-youtube-videos-in-8k-with-python-a-beginner-friendly-guide-using-yt-dlp-33m7)
[7](https://dev.to/devasservice/customtkinter-a-complete-tutorial-4527)
[8](https://github.com/TomSchimansky/CustomTkinter)
[9](https://github.com/yt-dlp/yt-dlp)
[10](https://www.rapidseedbox.com/blog/yt-dlp-complete-guide)
[11](https://www.reddit.com/r/opensource/comments/1ia4rib/i_built_a_python_script_to_download_any_youtube/)
[12](https://www.youtube.com/watch?v=nJQh1L9Y70U)
[13](https://michael.team/ytd/)
[14](https://www.youtube.com/watch?v=1itG8q-sCGY)
[15](https://stackoverflow.com/questions/44610370/how-to-use-youtube-dl-script-to-download-starting-from-some-index-in-a-playlist)
[16](https://www.geeksforgeeks.org/python/build-a-basic-form-gui-using-customtkinter-module-in-python/)
[17](https://www.youtube.com/watch?v=mop6g-c5HEY)
[18](https://stackoverflow.com/questions/62122077/how-to-make-a-exe-from-python-script-with-pyinstaller)
[19](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/)
[20](https://pypi.org/project/pyinstaller/)