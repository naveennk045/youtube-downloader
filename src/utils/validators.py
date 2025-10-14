"""
URL validation utilities
"""

import re


def validate_url(url):
    """
    Validate YouTube URL (video or playlist)

    Args:
        url: URL string to validate

    Returns:
        bool: True if valid YouTube URL
    """
    youtube_patterns = [
        r'^https?://(www\.)?youtube\.com/watch\?v=[\w-]+',
        r'^https?://(www\.)?youtube\.com/playlist\?list=[\w-]+',
        r'^https?://youtu\.be/[\w-]+',
        r'^https?://(www\.)?youtube\.com/shorts/[\w-]+'
    ]

    return any(re.match(pattern, url) for pattern in youtube_patterns)


def is_playlist(url):
    """Check if URL is a playlist"""
    return 'playlist?list=' in url
