"""
YouTube Downloader - Main Entry Point
A modern desktop application for downloading YouTube videos and playlists
"""

import customtkinter as ctk
from src.ui.main_window import MainWindow
from src.utils.logger import setup_logger
import os


def main():
    # Setup logging
    logger = setup_logger()
    logger.info("Starting YouTube Downloader Application")

    # Create necessary directories
    os.makedirs("downloads", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    # Set appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Launch application
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
