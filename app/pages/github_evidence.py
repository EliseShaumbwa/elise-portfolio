import flet as ft

from app.components.gallery_overlay import gallery_overlay
from app.compat import BOLD
from app.theme import BG, CARD, NEON, TEXT, TEXT_DIM


def github_page(page: ft.Page) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("GitHub Evidence & Documentation", size=32, weight=BOLD, color=NEON),
                ft.Text("Commit history, pull requests, and engineering impact", color=TEXT_DIM),
                ft.Container(height=12),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Commit History", color=NEON, weight=BOLD, size=18),
                                    ft.Text(
                                        "Screenshots of commits to the CorroCheck main repository.",
                                        color=TEXT_DIM,
                                        size=13,
                                    ),
                                    ft.ElevatedButton(
                                        "View Commits",
                                        bgcolor=NEON,
                                        color="#000000",
                                        on_click=lambda e: gallery_overlay(
                                                page,
                                                image_paths=[
                                                    "images/commits/commit_001.png",
                                                    "images/commits/commit_002.png",
                                                    "images/commits/commit_003.png",
                                                    "images/commits/commit_004.png",
                                                    "images/commits/commit_005.png",
                                                    "images/commits/commit_006.png",
                                                    "images/commits/commit_007.png",
                                                    "images/commits/commit_008.png",
                                                    "images/commits/commit_009.png",
                                                ],
                                                title="Commit History",
                                        ),
                                    ),
                                ],
                                spacing=10,
                            ),
                            bgcolor=CARD,
                            border_radius=12,
                            padding=24,
                            width=300,
                            border=ft.border.all(1, "#1a3a1a"),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Pull Request Logs", color=NEON, weight=BOLD, size=18),
                                    ft.Text(
                                        "Proposed features, code reviews performed, and merges completed.",
                                        color=TEXT_DIM,
                                        size=13,
                                    ),
                                    ft.ElevatedButton(
                                        "View PRs",
                                        bgcolor=NEON,
                                        color="#000000",
                                        on_click=lambda e: gallery_overlay(
                                            page,
                                            image_paths=[
                                                "images/prs/pr_001.png",
                                                "images/prs/pr_002.png",
                                                "images/prs/pr_003.png",
                                                "images/prs/pr_004.png",
                                                "images/prs/pr_005.png",
                                            ],
                                            title="Pull Request Logs",
                                        ),
                                    ),
                                ],
                                spacing=10,
                            ),
                            bgcolor=CARD,
                            border_radius=12,
                            padding=24,
                            width=300,
                            border=ft.border.all(1, "#1a3a1a"),
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Impact Summary", color=NEON, weight=BOLD, size=18),
                                    ft.Text(
                                        "By integrating Roboflow's AI backend into the CorroCheck submission flow, I enabled "
                                        "real-time corrosion detection for Civil and Metallurgical engineering use cases — "
                                        "allowing field engineers to submit images and receive instant structural damage "
                                        "assessments directly within the app.",
                                        color=TEXT_DIM,
                                        size=13,
                                    ),
                                ],
                                spacing=10,
                            ),
                            bgcolor=CARD,
                            border_radius=12,
                            padding=24,
                            expand=True,
                            border=ft.border.all(1, "#1a3a1a"),
                        ),
                    ],
                    spacing=16,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=BG,
        padding=40,
    )
