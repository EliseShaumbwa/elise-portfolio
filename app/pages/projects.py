import flet as ft

from app.components.gallery_overlay import gallery_overlay
from app.compat import BOLD, ICONS
from app.theme import BG, CARD, NEON, TEXT, TEXT_DIM


def projects_page(page: ft.Page) -> ft.Container:

    # ── Add your screenshot paths here as you take more ───────────────────
    corrocheck_screenshots = [
        "images/screenshots/corrocheck_01.png",
        "images/screenshots/corrocheck_02.png",
        "images/screenshots/corrocheck_03.png",
        "images/screenshots/corrocheck_04.png",
        "images/screenshots/corrocheck_05.png",
        "images/screenshots/corrocheck_06.png",
        "images/screenshots/corrocheck_07.png",
        "images/screenshots/corrocheck_08.png",
        "images/screenshots/corrocheck_09.png",
        "images/screenshots/corrocheck_10.png",
        "images/screenshots/corrocheck_11.png",
        "images/screenshots/corrocheck_12.png",
        "images/screenshots/corrocheck_13.png",
        "images/screenshots/corrocheck_14.png",
        "images/screenshots/corrocheck_15.png",
    ]

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Projects", size=32, weight=BOLD, color=NEON),
                ft.Text("CorroCheck — Corrosion Checking Application", color=TEXT_DIM),
                ft.Container(height=16),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Icon(ICONS.BUILD_CIRCLE, color=NEON, size=48),
                                    ft.Text("CorroCheck", size=24, weight=BOLD, color=NEON),
                                    ft.Text(
                                        "A group engineering app for corrosion assessment across "
                                        "the Metallurgical descipline. Built with Expo, React Native "
                                        "and Firebase.",
                                        color=TEXT_DIM,
                                        size=14,
                                    ),
                                    ft.Row(
                                        [
                                            ft.OutlinedButton(
                                                "View Screenshots",
                                                on_click=lambda e: gallery_overlay(
                                                    page,
                                                    corrocheck_screenshots,
                                                    "CorroCheck Screenshots",
                                                ),
                                            ),
                                        ],
                                        spacing=12,
                                    ),
                                ],
                                spacing=12,
                            ),
                            bgcolor=CARD,
                            border_radius=12,
                            padding=28,
                            border=ft.border.all(1, "#1a3a1a"),
                            width=500,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Key Features", color=NEON, weight=BOLD, size=18),
                                    ft.Text("• AI-Powered Corrosion Detection from Images", color=TEXT_DIM),
                                    ft.Text("• Automated Report Generation", color=TEXT_DIM),
                                    ft.Text("• Personal Analysis History", color=TEXT_DIM),
                                    ft.Text("• Secure Multi-User Support", color=TEXT_DIM),
                                ],
                                spacing=8,
                            ),
                            bgcolor=CARD,
                            border_radius=12,
                            padding=28,
                            border=ft.border.all(1, "#1a3a1a"),
                            expand=True,
                        ),
                    ],
                    spacing=20,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )