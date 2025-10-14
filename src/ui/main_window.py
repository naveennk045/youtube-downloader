"""
Main application window with modern UI
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
from src.ui.styles import ColorScheme, Fonts
from src.core.downloader import VideoDownloader
from src.core.queue_manager import QueueManager
from src.utils.validators import validate_url
from src.ui.download_item import DownloadItemWidget


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("YouTube Downloader Pro")
        self.geometry("1000x700")
        self.minsize(900, 600)

        # Initialize managers
        self.queue_manager = QueueManager()
        self.downloader = VideoDownloader()
        self.download_widgets = {}

        # Setup UI
        self.setup_ui()

        # Configure grid weights
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def setup_ui(self):
        """Create all UI components"""
        self._create_header()
        self._create_input_section()
        self._create_options_section()
        self._create_queue_section()
        self._create_status_bar()

    def _create_header(self):
        """Create application header"""
        header_frame = ctk.CTkFrame(self, fg_color=ColorScheme.DARK_SECONDARY, corner_radius=0)
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

        title = ctk.CTkLabel(
            header_frame,
            text="🎬 YouTube Downloader Pro",
            font=Fonts.TITLE,
            text_color=ColorScheme.PRIMARY
        )
        title.pack(pady=20)

    def _create_input_section(self):
        """Create URL input section"""
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(10, 0))
        input_frame.grid_columnconfigure(0, weight=1)

        # URL Entry
        self.url_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="🔗 Paste YouTube video or playlist URL here...",
            font=Fonts.BODY,
            height=40,
            border_width=2,
            border_color=ColorScheme.PRIMARY
        )
        self.url_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.url_entry.bind("<Return>", lambda e: self.add_to_queue())

        # Add button
        self.add_btn = ctk.CTkButton(
            input_frame,
            text="Add to Queue",
            font=Fonts.SUBHEADING,
            height=40,
            width=150,
            command=self.add_to_queue,
            fg_color=ColorScheme.PRIMARY,
            hover_color=ColorScheme.BUTTON_HOVER
        )
        self.add_btn.grid(row=0, column=1)

    def _create_options_section(self):
        """Create download options section"""
        options_frame = ctk.CTkFrame(self, fg_color=ColorScheme.DARK_SECONDARY)
        options_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
        options_frame.grid_columnconfigure(1, weight=1)

        # Quality selection
        quality_label = ctk.CTkLabel(
            options_frame,
            text="Quality:",
            font=Fonts.SUBHEADING
        )
        quality_label.grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.quality_var = ctk.StringVar(value="1080p")
        quality_options = ["2160p (4K)", "1440p (2K)", "1080p (HD)", "720p", "480p", "360p"]
        self.quality_menu = ctk.CTkOptionMenu(
            options_frame,
            values=quality_options,
            variable=self.quality_var,
            font=Fonts.BODY,
            fg_color=ColorScheme.PRIMARY,
            button_color=ColorScheme.PRIMARY,
            button_hover_color=ColorScheme.BUTTON_HOVER
        )
        self.quality_menu.grid(row=0, column=1, padx=10, pady=15, sticky="w")

        # Download path
        path_label = ctk.CTkLabel(
            options_frame,
            text="Save to:",
            font=Fonts.SUBHEADING
        )
        path_label.grid(row=0, column=2, padx=15, pady=15, sticky="w")

        self.path_entry = ctk.CTkEntry(
            options_frame,
            font=Fonts.BODY,
            width=300
        )
        self.path_entry.insert(0, "./downloads")
        self.path_entry.grid(row=0, column=3, padx=10, pady=15, sticky="ew")

        browse_btn = ctk.CTkButton(
            options_frame,
            text="Browse",
            width=100,
            command=self.browse_folder,
            fg_color=ColorScheme.INFO,
            hover_color=ColorScheme.BUTTON_HOVER
        )
        browse_btn.grid(row=0, column=4, padx=15, pady=15)

    def _create_queue_section(self):
        """Create download queue section"""
        queue_frame = ctk.CTkFrame(self, fg_color=ColorScheme.DARK_SECONDARY)
        queue_frame.grid(row=3, column=0, sticky="nsew", padx=20, pady=10)
        queue_frame.grid_rowconfigure(1, weight=1)
        queue_frame.grid_columnconfigure(0, weight=1)

        # Queue header
        header_container = ctk.CTkFrame(queue_frame, fg_color="transparent")
        header_container.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        header_container.grid_columnconfigure(0, weight=1)

        queue_label = ctk.CTkLabel(
            header_container,
            text="📥 Download Queue",
            font=Fonts.HEADING,
            text_color=ColorScheme.PRIMARY
        )
        queue_label.grid(row=0, column=0, sticky="w")

        # Control buttons
        btn_frame = ctk.CTkFrame(header_container, fg_color="transparent")
        btn_frame.grid(row=0, column=1, sticky="e")

        self.start_btn = ctk.CTkButton(
            btn_frame,
            text="▶ Start All",
            width=120,
            command=self.start_downloads,
            fg_color=ColorScheme.SUCCESS,
            hover_color="#00cc70"
        )
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = ctk.CTkButton(
            btn_frame,
            text="⏸ Pause All",
            width=120,
            command=self.pause_downloads,
            fg_color=ColorScheme.WARNING,
            hover_color="#ff8800"
        )
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.clear_btn = ctk.CTkButton(
            btn_frame,
            text="🗑 Clear",
            width=100,
            command=self.clear_completed,
            fg_color=ColorScheme.ERROR,
            hover_color="#ee3344"
        )
        self.clear_btn.grid(row=0, column=2, padx=5)

        # Scrollable queue list
        self.queue_scroll = ctk.CTkScrollableFrame(
            queue_frame,
            fg_color=ColorScheme.DARK_ACCENT
        )
        self.queue_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.queue_scroll.grid_columnconfigure(0, weight=1)

    def _create_status_bar(self):
        """Create status bar"""
        status_frame = ctk.CTkFrame(self, fg_color=ColorScheme.DARK_SECONDARY, corner_radius=0, height=35)
        status_frame.grid(row=4, column=0, sticky="ew", padx=0, pady=0)

        self.status_label = ctk.CTkLabel(
            status_frame,
            text="Ready to download",
            font=Fonts.SMALL,
            text_color=ColorScheme.TEXT_SECONDARY
        )
        self.status_label.pack(side="left", padx=15, pady=7)

        self.queue_count_label = ctk.CTkLabel(
            status_frame,
            text="Queue: 0",
            font=Fonts.SMALL,
            text_color=ColorScheme.PRIMARY
        )
        self.queue_count_label.pack(side="right", padx=15, pady=7)

    def add_to_queue(self):
        """Add URL to download queue"""
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showwarning("Empty URL", "Please enter a YouTube URL")
            return

        if not validate_url(url):
            messagebox.showerror("Invalid URL", "Please enter a valid YouTube URL")
            return

        # Add to queue
        quality = self.quality_var.get().split()[0]  # Extract resolution
        download_path = self.path_entry.get()

        item_id = self.queue_manager.add_item(url, quality, download_path)

        # Create widget
        widget = DownloadItemWidget(
            self.queue_scroll,
            url,
            quality,
            self.remove_from_queue,
            item_id
        )
        widget.pack(fill="x", padx=5, pady=5)
        self.download_widgets[item_id] = widget

        # Update UI
        self.url_entry.delete(0, "end")
        self.update_queue_count()
        self.status_label.configure(text=f"Added to queue: {url[:50]}...")

    def start_downloads(self):
        """Start all downloads in queue"""
        pending_items = self.queue_manager.get_pending_items()

        if not pending_items:
            messagebox.showinfo("Empty Queue", "No items in queue to download")
            return

        self.status_label.configure(text="Starting downloads...")

        for item in pending_items:
            thread = threading.Thread(
                target=self._download_thread,
                args=(item,),
                daemon=True
            )
            thread.start()

    def _download_thread(self, item):
        """Download thread worker"""
        item_id = item['id']
        widget = self.download_widgets.get(item_id)

        if widget:
            widget.set_status("downloading")

        def progress_callback(progress_data):
            if widget:
                if 'downloaded_bytes' in progress_data and 'total_bytes' in progress_data:
                    percent = (progress_data['downloaded_bytes'] / progress_data['total_bytes']) * 100
                    widget.update_progress(percent)

        success = self.downloader.download(
            item['url'],
            item['download_path'],
            item['quality'],
            progress_callback
        )

        if widget:
            if success:
                widget.set_status("completed")
                self.queue_manager.mark_completed(item_id)
                self.status_label.configure(text="Download completed successfully")
            else:
                widget.set_status("failed")
                self.status_label.configure(text="Download failed")

    def pause_downloads(self):
        """Pause all active downloads"""
        self.downloader.pause_all()
        self.status_label.configure(text="Downloads paused")

    def clear_completed(self):
        """Clear completed downloads from queue"""
        completed_ids = self.queue_manager.get_completed_ids()

        for item_id in completed_ids:
            if item_id in self.download_widgets:
                self.download_widgets[item_id].destroy()
                del self.download_widgets[item_id]
                self.queue_manager.remove_item(item_id)

        self.update_queue_count()
        self.status_label.configure(text="Cleared completed downloads")

    def remove_from_queue(self, item_id):
        """Remove specific item from queue"""
        if item_id in self.download_widgets:
            self.download_widgets[item_id].destroy()
            del self.download_widgets[item_id]
            self.queue_manager.remove_item(item_id)
            self.update_queue_count()

    def browse_folder(self):
        """Open folder browser"""
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, folder)

    def update_queue_count(self):
        """Update queue count label"""
        count = len(self.download_widgets)
        self.queue_count_label.configure(text=f"Queue: {count}")
