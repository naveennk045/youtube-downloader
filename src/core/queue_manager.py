"""
Download queue manager
"""

import uuid
from datetime import datetime
from src.utils.logger import get_logger

logger = get_logger()


class QueueManager:
    def __init__(self):
        self.queue = []
        self.completed = []

    def add_item(self, url, quality, download_path):
        """Add item to queue"""
        item = {
            'id': str(uuid.uuid4()),
            'url': url,
            'quality': quality,
            'download_path': download_path,
            'status': 'pending',
            'added_at': datetime.now(),
            'progress': 0
        }
        self.queue.append(item)
        logger.info(f"Added to queue: {url}")
        return item['id']

    def remove_item(self, item_id):
        """Remove item from queue"""
        self.queue = [item for item in self.queue if item['id'] != item_id]
        self.completed = [item for item in self.completed if item['id'] != item_id]
        logger.info(f"Removed from queue: {item_id}")

    def get_pending_items(self):
        """Get all pending items"""
        return [item for item in self.queue if item['status'] == 'pending']

    def mark_completed(self, item_id):
        """Mark item as completed"""
        for item in self.queue:
            if item['id'] == item_id:
                item['status'] = 'completed'
                self.completed.append(item)
                logger.info(f"Marked completed: {item_id}")
                break

    def get_completed_ids(self):
        """Get all completed item IDs"""
        return [item['id'] for item in self.queue if item['status'] == 'completed']

    def clear_completed(self):
        """Clear all completed items"""
        self.queue = [item for item in self.queue if item['status'] != 'completed']
        count = len(self.completed)
        self.completed = []
        logger.info(f"Cleared {count} completed items")
        return count
