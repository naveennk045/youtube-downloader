"""
Individual download item widget for the queue
"""

import customtkinter as ctk
from src.ui.styles import ColorScheme, Fonts


class DownloadItemWidget(ctk.CTkFrame):
    def __init__(self, parent, url, quality, remove_callback, item_id):
        super().__init__(parent, fg_color=ColorScheme.DARK_BG, corner_radius=8)

        self.item_id = item_id
        self.remove_callback = remove_callback
        self.url = url

        self.grid_columnconfigure(1, weight=1)

        # Status indicator
        self.status_dot = ctk.CTkLabel(
            self,
            text="●",
            font=("Arial", 20),
            text_color=ColorScheme.TEXT_MUTED,
            width=30
        )
        self.status_dot.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Info section
        info_frame = ctk.CTkFrame(self, fg_color="transparent")
        info_frame.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
        info_frame.grid_columnconfigure(0, weight=1)

        # Title
        title_text = url if len(url) < 60 else url[:57] + "..."
        self.title_label = ctk.CTkLabel(
            info_frame,
            text=title_text,
            font=Fonts.BODY,
            anchor="w"
        )
        self.title_label.grid(row=0, column=0, sticky="w")

        # Quality badge
        quality_label = ctk.CTkLabel(
            info_frame,
            text=quality,
            font=Fonts.SMALL,
            text_color=ColorScheme.PRIMARY,
            fg_color=ColorScheme.DARK_ACCENT,
            corner_radius=5,
            padx=10,
            pady=2
        )
        quality_label.grid(row=0, column=1, padx=10)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            info_frame,
            height=6,
            progress_color=ColorScheme.PRIMARY
        )
        self.progress_bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5, 0))
        self.progress_bar.set(0)

        # Status text
        self.status_label = ctk.CTkLabel(
            info_frame,
            text="Waiting...",
            font=Fonts.SMALL,
            text_color=ColorScheme.TEXT_MUTED,
            anchor="w"
        )
        self.status_label.grid(row=2, column=0, sticky="w", pady=(2, 0))

        # Remove button
        self.remove_btn = ctk.CTkButton(
            self,
            text="✕",
            width=40,
            height=40,
            command=self._on_remove,
            fg_color=ColorScheme.ERROR,
            hover_color="#cc3344",
            font=("Arial", 16, "bold")
        )
        self.remove_btn.grid(row=0, column=2, padx=10, pady=10)

    def update_progress(self, percent):
        """Update progress bar"""
        self.progress_bar.set(percent / 100)
        self.status_label.configure(text=f"Downloading... {percent:.1f}%")

    def set_status(self, status):
        """Update status indicator"""
        status_config = {
            "waiting": {"color": ColorScheme.TEXT_MUTED, "text": "Waiting..."},
            "downloading": {"color": ColorScheme.PRIMARY, "text": "Downloading..."},
            "completed": {"color": ColorScheme.SUCCESS, "text": "✓ Completed"},
            "failed": {"color": ColorScheme.ERROR, "text": "✗ Failed"},
            "paused": {"color": ColorScheme.WARNING, "text": "⏸ Paused"}
        }

        config = status_config.get(status, status_config["waiting"])
        self.status_dot.configure(text_color=config["color"])
        self.status_label.configure(text=config["text"])

        if status == "completed":
            self.progress_bar.set(1.0)

    def _on_remove(self):
        """Handle remove button click"""
        self.remove_callback(self.item_id)
