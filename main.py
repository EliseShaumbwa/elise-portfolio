import flet as ft

from app.compat import BOLD, SCROLL_OFF, set_window_size
from app.components.nav_bar import nav_bar
from app.pages.blog import blog_page
from app.pages.contact import contact_page
from app.pages.github_evidence import github_page
from app.pages.home import home_page
from app.pages.matlab_hub import matlab_hub_page
from app.pages.projects import projects_page
from app.pages.skills import skills_page
from app.pages.timeline import timeline_page
from app.theme import BG


def main(page: ft.Page):
    page.title = "Elise Shaumbwa | Portfolio"
    page.bgcolor = BG
    page.padding = 0
    page.spacing = 0
    page.scroll = None
    page.theme_mode = ft.ThemeMode.DARK
    if not page.web:
        set_window_size(page, 1200, 800)

    content_area = ft.Container(expand=True)
    state = {"section": "home"}

    def render():
        s = state["section"]
        views = {
            "home": home_page(page, navigate),
            "skills": skills_page(),
            "projects": projects_page(page),
            "timeline": timeline_page(),
            "matlab": matlab_hub_page(page),
            "blog": blog_page(page),
            "github": github_page(page),
            "contact": contact_page(page),
        }
        content_area.content = views.get(s, views["home"])
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    nav_bar(page, s, navigate),
                    content_area,
                ],
                spacing=0,
                expand=True,
                scroll=SCROLL_OFF,
            )
        )
        page.update()

    def navigate(section: str):
        state["section"] = section
        render()

    render()


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, assets_dir="assets", port=8550)
