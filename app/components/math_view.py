import flet as ft

from app.compat import BOLD
from app.theme import CARD, NEON, TEXT_DIM


def math_article(title: str, paragraphs: list[str]) -> ft.Container:
    """Render technical content with readable math notation."""
    lines = [ft.Text(title, size=18, weight=BOLD, color=NEON)]
    for paragraph in paragraphs:
        lines.append(ft.Text(paragraph, color=TEXT_DIM, size=14))

    return ft.Container(
        content=ft.Column(lines, spacing=8, scroll=False),
        bgcolor=CARD,
        border_radius=12,
        padding=20,
        height=320,
    )


def blog_card(title: str, excerpt: str, on_open) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(title, size=18, weight=BOLD, color=NEON),
                ft.Text(excerpt, color=TEXT_DIM, size=14),
                ft.ElevatedButton(
                    "Read Article",
                    bgcolor=NEON,
                    color="#000000",
                    on_click=lambda e: on_open(),
                ),
            ],
            spacing=10,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=20,
        border=ft.border.all(1, "#1a3a1a"),
    )
