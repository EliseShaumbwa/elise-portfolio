import flet as ft

from app.compat import BOLD, IMAGE_CONTAIN, IMAGE_COVER, ICONS, make_video
from app.theme import BG, CARD, NEON, TEXT


def video_overlay(page: ft.Page, src: str, title: str = "Video") -> ft.Container:
    """In-app video player overlay — no external windows."""
    player = make_video(src)

    def close():
        page.overlay.clear()
        page.update()

    overlay = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(title, size=18, weight=BOLD, color=NEON),
                        ft.IconButton(
                            icon=ICONS.CLOSE,
                            icon_color=TEXT,
                            on_click=lambda e: close(),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(content=player, expand=True, border_radius=8),
            ],
            spacing=12,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=20,
        width=page.width * 0.75 if page.width else 800,
        height=page.height * 0.75 if page.height else 500,
    )

    page.overlay.append(
        ft.Stack(
            [
                ft.Container(bgcolor="#000000cc", expand=True, on_click=lambda e: close()),
                ft.Container(content=overlay, alignment=ft.Alignment(0,0)),
            ],
            expand=True,
        )
    )
    page.update()
    return overlay


def image_overlay(page: ft.Page, src: str, title: str = "Image") -> None:
    """In-app image viewer overlay."""
    img = ft.Image(src=src, fit=IMAGE_CONTAIN, expand=True)

    def close():
        page.overlay.clear()
        page.update()

    card = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(title, size=18, weight=BOLD, color=NEON),
                        ft.IconButton(icon=ICONS.CLOSE, icon_color=TEXT, on_click=lambda e: close()),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(content=img, expand=True),
            ],
            spacing=12,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=20,
        width=page.width * 0.8 if page.width else 900,
        height=page.height * 0.8 if page.height else 600,
    )

    page.overlay.append(
        ft.Stack(
            [
                ft.Container(bgcolor="#000000cc", expand=True, on_click=lambda e: close()),
                ft.Container(content=card, alignment=ft.Alignment(0,0)),
            ],
            expand=True,
        )
    )
    page.update()
