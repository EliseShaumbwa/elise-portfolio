import flet as ft

from app.compat import BOLD
from app.theme import BG, CARD, NEON, TEXT_DIM


def timeline_page() -> ft.Container:
    weeks = [
        ("Week 1", "Project kickoff — defined CorroCheck scope, set up repo, helped teammates set up their working environments."),
        ("Week 2", "Presented the pitch for the mining descipline, assigned roles to teammates."),
        ("Week 3", "Created figma project file and added the design team, Helped with screen designs."),
        ("Week 5", "Helped design 2 logo's."),
        ("Week 9", "Finished the remaining UI screen designs."),
        ("Week 10", "Did the prototype, implemented the React Native screens."),
        ("Week 11", "Helped backend with their work."),
        ("Week 12", "Integrated and tested the app, reviewed teammates code, fixed github merge conflicts."),
        ("Week 13", "Integrated and tested the app, fixed repo conflicts."),
    ]

    state = {"idx": 0}
    week_label = ft.Text(weeks[0][0], color=NEON, size=20, weight=BOLD)
    week_desc = ft.Text(weeks[0][1], color=TEXT_DIM, size=15, text_align=ft.TextAlign.CENTER)
    counter = ft.Text(f"1 / {len(weeks)}", color=TEXT_DIM, size=13)

    def update_view():
        w, d = weeks[state["idx"]]
        week_label.value = w
        week_desc.value = d
        counter.value = f"{state['idx'] + 1} / {len(weeks)}"

    def prev_week(e):
        if state["idx"] > 0:
            state["idx"] -= 1
            update_view()
            week_label.update()
            week_desc.update()
            counter.update()

    def next_week(e):
        if state["idx"] < len(weeks) - 1:
            state["idx"] += 1
            update_view()
            week_label.update()
            week_desc.update()
            counter.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Project Timeline", size=32, weight=BOLD, color=NEON),
                ft.Text("Weekly contributions to the CorroCheck group project", color=TEXT_DIM),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column(
                        [week_label, ft.Container(height=12), week_desc],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    bgcolor=CARD,
                    border_radius=12,
                    padding=40,
                    width=600,
                    height=220,
                    border=ft.border.all(1, "#1a3a1a"),
                ),
                ft.Container(height=16),
                ft.Row(
                    [
                        ft.ElevatedButton("← Previous Week", bgcolor=NEON, color="#000000", on_click=prev_week),
                        counter,
                        ft.ElevatedButton("Next Week →", bgcolor=NEON, color="#000000", on_click=next_week),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
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
