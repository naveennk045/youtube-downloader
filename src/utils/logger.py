"""
Logging configuration
"""

import logging
import os
from datetime import datetime


def setup_logger():
    """Setup application logger"""
    os.makedirs("logs", exist_ok=True)

    log_file = os.path.join("logs", f"app_{datetime.now().strftime('%Y%m%d')}.log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("YouTubeDownloader")


def get_logger():
    """Get logger instance"""
    return logging.getLogger("YouTubeDownloader")
