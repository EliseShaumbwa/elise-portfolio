import os
import flet as ft
from app.theme import BG, CARD, NEON, TEXT, TEXT_DIM
from app.compat import BOLD


def gallery_overlay(page: ft.Page, image_paths: list[str], title: str):
    """
    Opens a gallery overlay showing thumbnail cards for each image in image_paths.
    Clicking a thumbnail opens a full-screen viewer with Previous/Next navigation.

    Parameters:
    - page        : the Flet Page object (same one you pass everywhere)
    - image_paths : a list of image file paths, e.g. ["images/commits/c1.png", ...]
    - title       : the heading shown at the top, e.g. "Commit History"
    """

    current_index = [0]

    # ── Helper: build a single thumbnail card ──────────────────────────────
    def make_thumb(index: int, path: str) -> ft.Container:
        filename = os.path.basename(path)

        return ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=path,
                        width=140,
                        height=90,
                        fit="cover",
                        border_radius=ft.border_radius.all(6),
                    ),
                    ft.Text(filename, size=11, color=TEXT_DIM, max_lines=1, overflow="ellipsis"),
                ],
                spacing=4,
            ),
            width=148,
            bgcolor=CARD,
            border_radius=8,
            padding=6,
            border=ft.border.all(1, "#1a3a1a"),
            on_click=lambda e, i=index: open_viewer(i),
            on_hover=lambda e: on_thumb_hover(e),
        )

    # ── Helper: hover highlight on thumbnail ──────────────────────────────
    def on_thumb_hover(e):
        e.control.border = ft.border.all(1, NEON if e.data == "true" else "#1a3a1a")
        e.control.update()

    # ── Viewer controls ────────────────────────────────────────────────────
    viewer_title_text = ft.Text("", size=16, weight=BOLD, color=NEON)
    counter_text      = ft.Text("", size=13, color=TEXT_DIM)
    viewer_image      = ft.Image(src="", fit="contain", expand=True)

    prev_btn = ft.ElevatedButton(
        "◀  Previous",
        bgcolor=CARD,
        color=NEON,
        on_click=lambda e: navigate(-1),
    )
    next_btn = ft.ElevatedButton(
        "Next  ▶",
        bgcolor=CARD,
        color=NEON,
        on_click=lambda e: navigate(1),
    )

    # ── Dot indicators ─────────────────────────────────────────────────────
    def build_dots(active: int) -> list[ft.Container]:
        dots = []
        for i in range(len(image_paths)):
            dots.append(
                ft.Container(
                    width=8, height=8,
                    border_radius=4,
                    bgcolor=NEON if i == active else "#1a3a1a",
                )
            )
        return dots

    dot_row = ft.Row([], spacing=5, alignment="center")

    # ── update_viewer ──────────────────────────────────────────────────────
    def update_viewer(index: int):
        path = image_paths[index]
        viewer_title_text.value = os.path.basename(path)
        counter_text.value      = f"{index + 1} / {len(image_paths)}"
        viewer_image.src        = path
        dot_row.controls        = build_dots(index)
        prev_btn.disabled       = index == 0
        next_btn.disabled       = index == len(image_paths) - 1
        viewer_title_text.update()
        counter_text.update()
        viewer_image.update()
        dot_row.update()
        prev_btn.update()
        next_btn.update()

    # ── navigate ───────────────────────────────────────────────────────────
    def navigate(direction: int):
        new_index = max(0, min(len(image_paths) - 1, current_index[0] + direction))
        current_index[0] = new_index
        update_viewer(new_index)

    # ── open_viewer ────────────────────────────────────────────────────────
    def open_viewer(index: int):
        current_index[0] = index
        update_viewer(index)
        gallery_panel.visible = False
        viewer_panel.visible  = True
        gallery_panel.update()
        viewer_panel.update()

    # ── close_viewer ───────────────────────────────────────────────────────
    def close_viewer(e):
        viewer_panel.visible  = False
        gallery_panel.visible = True
        viewer_panel.update()
        gallery_panel.update()

    # ── close_all ──────────────────────────────────────────────────────────
    def close_all(e):
        page.overlay.clear()
        page.update()

    # ══════════════════════════════════════════════════════════════════════
    # GALLERY PANEL
    # ══════════════════════════════════════════════════════════════════════
    thumbs = [make_thumb(i, p) for i, p in enumerate(image_paths)]

    gallery_panel = ft.Container(
        visible=True,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            f"{title} — {len(image_paths)} screenshots",
                            size=18,
                            weight=BOLD,
                            color=NEON,
                        ),
                        ft.IconButton(ft.Icons.CLOSE, icon_color=TEXT_DIM, on_click=close_all),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Divider(color="#1a3a1a"),
                ft.Row(
                    controls=thumbs,
                    spacing=10,
                    run_spacing=10,
                    wrap=True,
                ),
            ],
            spacing=12,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=24,
        width=700,
        border=ft.border.all(1, "#1a3a1a"),
    )

    # ══════════════════════════════════════════════════════════════════════
    # VIEWER PANEL
    # ══════════════════════════════════════════════════════════════════════
    viewer_panel = ft.Container(
        visible=False,
        content=ft.Column(
            [
                ft.Row(
                    [
                        viewer_title_text,
                        ft.Row(
                            [
                                counter_text,
                                ft.IconButton(ft.Icons.CLOSE, icon_color=TEXT_DIM, on_click=close_viewer),
                            ],
                            spacing=8,
                        ),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Divider(color="#1a3a1a"),
                ft.Container(
                    content=viewer_image,
                    height=420,
                    bgcolor=BG,
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                ),
                ft.Divider(color="#1a3a1a"),
                ft.Row(
                    [prev_btn, dot_row, next_btn],
                    alignment="spaceBetween",
                ),
            ],
            spacing=12,
        ),
        bgcolor=CARD,
        border_radius=12,
        padding=24,
        width=700,
        border=ft.border.all(1, "#1a3a1a"),
    )

    # ══════════════════════════════════════════════════════════════════════
    # BACKDROP
    # ══════════════════════════════════════════════════════════════════════
    backdrop = ft.Stack(
        [
            ft.Container(
                bgcolor="#CC000000",
                expand=True,
                on_click=close_all,
            ),
            ft.Container(
                content=ft.Stack([gallery_panel, viewer_panel]),
                alignment=ft.Alignment(0, 0),
                expand=True,
            ),
        ],
        expand=True,
    )

    page.overlay.append(backdrop)
    page.update()