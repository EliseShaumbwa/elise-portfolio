import flet as ft

from app.compat import BOLD, ICONS
from app.theme import BG, CARD, NEON, TEXT_DIM


def skills_page() -> ft.Container:
    skills = [
        (ICONS.CODE, "Frontend Development", "Responsive UI"),
        (ICONS.STORAGE, "Backend Development", "AI Integration, Node.js, Firebase, System Integration, Testing"),
        (ICONS.DESIGN_SERVICES, "UI/UX Design", "Prototyping, , Wireframing"),
        (ICONS.SCIENCE, "Engineering Modules", "Metallurgical, Mining & Civil corrosion analysis"),
        (ICONS.ANALYTICS, "Data & MATLAB", "MathWorks courses, numerical modelling, reporting"),
        (ICONS.HUB, "DevOps & GitHub", "Commits, pull requests, code review, documentation"),
    ]

    cards = []
    for icon, title, tech in skills:
        cards.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(icon, color=NEON, size=36),
                        ft.Text(title, size=18, weight=BOLD, color=NEON),
                        ft.Text(tech, color=TEXT_DIM, size=13),
                    ],
                    spacing=8,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=CARD,
                border_radius=12,
                padding=24,
                border=ft.border.all(1, "#1a3a1a"),
                width=280,
                height=180,
            )
        )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Technical Expertise", size=32, weight=BOLD, color=NEON),
                ft.Text("Core competencies across the CorroCheck stack", color=TEXT_DIM),
                ft.Container(height=12),
                ft.Row(cards[:3], wrap=True, spacing=16, run_spacing=16),
                ft.Row(cards[3:], wrap=True, spacing=16, run_spacing=16),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )
