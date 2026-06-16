"""Compatibility helpers for Flet 0.84.x."""

import flet as ft
import flet_video as fv   # <-- NEW import for the video package

BOLD = ft.FontWeight.BOLD
IMAGE_COVER = ft.BoxFit.COVER
IMAGE_CONTAIN = ft.BoxFit.CONTAIN
SCROLL_OFF = ft.ScrollMode.HIDDEN
ICONS = getattr(ft, "Icons", ft.icons)


def set_window_size(page: ft.Page, width: int, height: int) -> None:
    page.window.width = width
    page.window.height = height


def make_video(src: str) -> ft.Control:
    return fv.Video(              # <-- changed ft.Video  →  fv.Video
        expand=True,
        playlist=[fv.VideoMedia(src)],   # <-- changed ft.VideoMedia  →  fv.VideoMedia
        autoplay=True,
        show_controls=True,
        aspect_ratio=16 / 9,
        volume=100,
    )


def bottom_border(color: str):
    return ft.border.only(bottom=ft.BorderSide(1, color))