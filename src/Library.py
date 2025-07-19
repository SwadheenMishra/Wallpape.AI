import flet as ft
import main
import settings
import os

class Frame(ft.Card):
    def __init__(self, image_url: str):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src=image_url,
                            fit=ft.ImageFit.COVER,  # Changed from FILL to COVER
                            width=float('inf'),     # Fill full width
                            height=float('inf'),    # Fill full height
                            expand=True
                        ),
                        expand=True,
                        width=float('inf'),        # Ensure container fills width
                        height=float('inf'),       # Ensure container fills height
                        border_radius=ft.border_radius.all(8),
                    ),
                ],
                expand=True,
            ),
            elevation=14,
            expand=True
        )


def screen(page: ft.Page, navDrawer):
    images = [f'generated/{f}' for f in os.listdir("assets/generated") if f.lower().endswith(".png")]
    frames = [Frame(url) for url in images]

    def on_nav_change(e):
        index = navDrawer.selected_index
        match index:
            case 0:
                main.screen(page, navDrawer)
            case 1:
                pass # already on Settings
            case 2:
                settings.screen(page, navDrawer)  
            

    navDrawer.on_change = on_nav_change

    page.clean()
    page.title = "Wallpaper AI - Library!"

    page.appbar = ft.AppBar(
        title=ft.Text("Library!"),
        center_title=True,
        leading=ft.IconButton(icon=ft.Icons.MENU, on_click=lambda _: page.open(navDrawer)),
        bgcolor="#324648"
    )

    grid = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=250,
        child_aspect_ratio=4 / 3,
        spacing=10,
        run_spacing=10,
        controls=frames
    )

    page.bgcolor = "#1B2729"
    page.add(grid)