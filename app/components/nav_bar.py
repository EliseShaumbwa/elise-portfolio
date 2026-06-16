import flet as ft

from app.compat import BOLD, bottom_border
from app.theme import BG, NEON, TEXT, BORDER


def nav_bar(page: ft.Page, active: str, on_navigate) -> ft.Container:
    links = [
        ("home", "Home"),
        ("skills", "Skills"),
        ("projects", "Projects"),
        ("timeline", "Timeline"),
        ("matlab", "MATLAB Hub"),
        ("blog", "Blog"),
        ("github", "GitHub"),
        ("contact", "Contact"),
    ]

    def link_btn(key: str, label: str) -> ft.TextButton:
        is_active = key == active
        return ft.TextButton(
            label,
            on_click=lambda e, k=key: on_navigate(k),
            style=ft.ButtonStyle(
                color=NEON if is_active else TEXT,
                overlay_color="#00ff4115",
            ),
        )

    return ft.Container(
        content=ft.Row(
            [
                ft.Text("Elise Shaumbwa", size=22, weight=BOLD, color=NEON),
                ft.Row([link_btn(k, l) for k, l in links], spacing=4),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.padding.symmetric(horizontal=40, vertical=16),
        bgcolor=BG,
        border=bottom_border(BORDER),
    )
