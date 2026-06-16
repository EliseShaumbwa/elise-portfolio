import flet as ft

# from app.components.math_view import blog_card, math_article  # kept for reference, not active
from app.components.overlay import video_overlay
from app.compat import BOLD, ICONS
from app.theme import BG, CARD, NEON, TEXT_DIM


def blog_page(page: ft.Page) -> ft.Container:

    # ── Article data (formulas kept here for reference) ──────────────
    # articles = {
    #     "corrosion": {
    #         "title": "Technical blog",
    #         "excerpt": "How Faraday's law and Tafel equations underpin CorroCheck calculations.",
    #         "paragraphs": [
    #             "Corrosion is an electrochemical process governed by two foundational equations in metallurgical engineering: Faraday's Law and the Tafel Equation.",
    #             "1. Faraday's Law — Corrosion Rate",
    #             "CR = (i_corr × M) / (n × F × ρ)",
    #             "Where: i_corr = corrosion current density (A/m²), M = molar mass (kg/mol), n = electrons transferred, F = Faraday's constant (96,485 C/mol), ρ = density (kg/m³).",
    #             "2. The Tafel Equation — Reaction Kinetics",
    #             "η = ±b × log(i / i₀)",
    #             "Where: η = overpotential (V), b = Tafel slope (V/decade), i = current density (A/m²), i₀ = exchange current density at equilibrium (A/m²).",
    #             "The '+' sign applies to anodic (oxidation) reactions; '−' to cathodic (reduction) reactions.",
    #             "By plotting log(i) vs η (a Tafel plot), the intersection of anodic and cathodic branches gives i_corr, which feeds into Faraday's Law to calculate the actual corrosion rate.",
    #         ],
    #         "video": "videos/blog_corrosion.mp4",
    #     },
    # }

    # ── Article overlay ──────────────────────────────────────────────
    def show_article():
        def close():
            page.overlay.clear()
            page.update()

        overlay_card = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Technical Blog", size=18, weight=BOLD, color=NEON),
                            ft.IconButton(
                                icon=ICONS.CLOSE,
                                icon_color="#ffffff",
                                on_click=lambda e: close(),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    
                    ft.Image(
                        src="images/blog.png",
                        fit="contain",
                        expand=True,
                    ),
                ],
                spacing=12,
                expand=True,
            ),
            bgcolor="#0d1f0d",
            border_radius=12,
            padding=24,
            width=page.width * 0.75 if page.width else 700,
            height=page.height * 0.85 if page.height else 600,
        )

        page.overlay.append(
            ft.Stack(
                [
                    ft.Container(
                        bgcolor="#000000cc",
                        expand=True,
                        on_click=lambda e: close(),
                    ),
                    ft.Container(
                        content=overlay_card,
                        alignment=ft.Alignment(0,0),
                    ),
                ],
                expand=True,
            )
        )
        page.update()

    # ── Article card (title + button only) ───────────────────────────
    article_card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Technical blog", size=18, weight=BOLD, color=NEON),
                ft.ElevatedButton(
                    "Read Article",
                    bgcolor=NEON,
                    color="#000000",
                    on_click=lambda e: show_article(),
                ),
            ],
            spacing=10,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=20,
        border=ft.border.all(1, "#1a3a1a"),
    )

    # ── Video card ───────────────────────────────────────────────────
    video_card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Embedded Video", size=18, weight=BOLD, color=NEON),
                ft.ElevatedButton(
                    "Watch Video",
                    bgcolor=NEON,
                    color="#000000",
                    on_click=lambda e: video_overlay(
                        page, "videos/blog_corrosion.mp4", "Corrosion Video"
                    ),
                ),
            ],
            spacing=10,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=20,
        border=ft.border.all(1, "#1a3a1a"),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Confidence in Concepts", size=32, weight=BOLD, color=NEON),
                ft.Text("Technical blog and embedded video", color=TEXT_DIM),
                ft.Container(height=12),
                ft.Row(
                    [article_card, video_card],  # 👈 both cards side by side
                    spacing=16,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )