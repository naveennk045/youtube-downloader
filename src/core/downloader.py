"""
YouTube downloader using yt-dlp with ffmpeg integration
"""

import yt_dlp
import os
from src.utils.logger import get_logger

logger = get_logger()


class VideoDownloader:
    def __init__(self):
        self.active_downloads = {}
        self.paused = False

    def download(self, url, download_path, quality, progress_callback=None):
        """
        Download video or playlist with specified quality

        Args:
            url: YouTube video or playlist URL
            download_path: Directory to save downloads
            quality: Video quality (e.g., "1080p", "720p")
            progress_callback: Function to call with progress updates

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Ensure download directory exists
            os.makedirs(download_path, exist_ok=True)

            # Extract height from quality (e.g., "1080p" -> "1080")
            height = quality.replace('p', '')

            # Configure yt-dlp options
            ydl_opts = {
                'format': f'bestvideo[height<={height}]+bestaudio/best[height<={height}]',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'progress_hooks': [self._progress_hook(progress_callback)],
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
            }

            # Download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                logger.info(f"Starting download: {url}")
                ydl.download([url])
                logger.info(f"Download completed: {url}")
                return True

        except Exception as e:
            logger.error(f"Download failed for {url}: {str(e)}")
            return False

    def _progress_hook(self, callback):
        """Create progress hook for yt-dlp"""

        def hook(d):
            if callback and d['status'] == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                downloaded = d.get('downloaded_bytes', 0)

                if total > 0:
                    callback({
                        'downloaded_bytes': downloaded,
                        'total_bytes': total,
                        'speed': d.get('speed', 0),
                        'eta': d.get('eta', 0)
                    })

        return hook

    def pause_all(self):
        """Pause all active downloads"""
        self.paused = True
        logger.info("All downloads paused")

    def resume_all(self):
        """Resume all paused downloads"""
        self.paused = False
        logger.info("All downloads resumed")
