import flet as ft

from app.components.overlay import image_overlay
from app.compat import BOLD, ICONS
from app.theme import BG, CARD, NEON, TEXT_DIM


def matlab_hub_page(page: ft.Page) -> ft.Container:
    courses = [
        ("MATLAB Onramp", "images/onramp.png"),
        ("Make and Manipulate Matrices", "images/matrices.png"),
        ("Explore Data with MATLAB Plots", "images/plots.png"),
        ("Calculations with Vectors and Matrices", "images/vectors.png"),
        ("Simulink Onramp", "images/simulink.png"),
        ("Signal Processing Onramp", "images/signal.png"),
        ("Common Data Analysis Techniques", "images/data.png"),
        ("Clean and Prepare Data for Analysis", "images/analysis.png"),
    ]

    cards = []
    for name, img_path in courses:
        cards.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ICONS.SCHOOL, color=NEON, size=32),
                        ft.Text(name, color=NEON, weight=BOLD, size=14, text_align=ft.TextAlign.CENTER),
                        ft.ElevatedButton(
                            "View Certificate",
                            bgcolor=NEON,
                            color="#000000",
                            on_click=lambda e, p=img_path, n=name: image_overlay(page, p, n),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
                bgcolor=CARD,
                border_radius=12,
                padding=16,
                width=200,
                height=180,
                border=ft.border.all(1, "#1a3a1a"),
            )
        )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("MATLAB Achievement Hub", size=32, weight=BOLD, color=NEON),
                ft.Text("8 MathWorks Learning Center courses — proof of completion", color=TEXT_DIM),
                ft.Container(height=12),
                ft.Row(cards[:4], wrap=True, spacing=12, run_spacing=12, alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(cards[4:], wrap=True, spacing=12, run_spacing=12, alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )
