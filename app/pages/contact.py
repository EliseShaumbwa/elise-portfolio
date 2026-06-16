import flet as ft

from app.compat import BOLD, ICONS
from app.theme import BG, CARD, NEON, TEXT, TEXT_DIM


def contact_page(page: ft.Page) -> ft.Container:
    status = ft.Text("", color=NEON, size=13)

    social = [
        (ICONS.CODE, "GitHub", "github.com/EliseShaumbwa"),
        (ICONS.EMAIL, "Email", "elise.shaumbwa@example.com"),
        (ICONS.CHAT, "WhatsApp", "+26 4XX XXX XXXX"),
        (ICONS.LINK, "LinkedIn", "linkedin.com/in/elise-shaumbwa"),
    ]

    def show_info(e, label, value):
        status.value = f"{label}: {value}"
        status.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Contact", size=32, weight=BOLD, color=NEON),
                ft.Text("Let's connect — Elise Shaumbwa", color=TEXT_DIM),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.TextField(label="Your Name", border_color=NEON),
                            ft.TextField(label="Your Email", border_color=NEON),
                            ft.TextField(label="Message", multiline=True, min_lines=3, border_color=NEON),
                            ft.ElevatedButton(
                                "Send Message",
                                bgcolor=NEON,
                                color="#000000",
                                on_click=lambda e: setattr(status, "value", "Message saved locally") or status.update(),
                            ),
                            status,
                        ],
                        spacing=14,
                        width=420,
                    ),
                    bgcolor=CARD,
                    border_radius=12,
                    padding=28,
                    border=ft.border.all(1, "#1a3a1a"),
                ),
                ft.Container(height=16),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=icon,
                            icon_color=TEXT,
                            tooltip=label,
                            on_click=lambda e, l=label, v=val: show_info(e, l, v),
                        )
                        for icon, label, val in social
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text("© 2026 Elise Shaumbwa. All rights reserved.", color=TEXT_DIM, size=12),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )
