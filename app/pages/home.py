import flet as ft

from app.compat import BOLD, IMAGE_COVER, ICONS, bottom_border
from app.theme import BG, NEON, TEXT_DIM


def home_page(page: ft.Page, on_navigate) -> ft.Container:
    profile = ft.Container(
        content=ft.Image(
            src="images/profile.png",
            width=280,
            height=280,
            fit=IMAGE_COVER,
            error_content=ft.Container(
                width=280,
                height=280,
                bgcolor="#1a1a1a",
                border_radius=140,
                alignment=ft.Alignment(0,0),
                content=ft.Icon(ICONS.PERSON, size=80, color=NEON),
            ),
        ),
        width=280,
        height=280,
        border_radius=140,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        border=ft.border.all(4, NEON),
        shadow=ft.BoxShadow(blur_radius=30, color="#00ff4144", spread_radius=4),
    )

    return ft.Container(
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Mining engineering", size=52, weight=BOLD, color=NEON),
                        ft.Text("Student", size=52, weight=BOLD, color=NEON),
                        ft.Container(height=16),
                        ft.Text(
                            "Contributed to a corrosion checking mobile app\n"
                            "developed with React Native, Expo, Firebase, and AI-based image processing.",
                            size=16,
                            color=TEXT_DIM,
                        ),
                        ft.Container(height=24),
                        ft.ElevatedButton(
                            "Let's Connect",
                            bgcolor=NEON,
                            color="#000000",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=24), padding=20),
                            on_click=lambda e: on_navigate("contact"),
                        ),
                    ],
                    spacing=4,
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(content=profile, alignment=ft.Alignment(0,0), expand=True),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )
