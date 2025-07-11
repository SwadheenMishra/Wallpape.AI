import flet as ft
import settings

def screen(page: ft.Page, navDrawer):
    def on_nav_change(e):
        index = navDrawer.selected_index
        match index:
            case 0:
                pass  # Already on Generate
            case 2:
                settings.screen(page, navDrawer)

    navDrawer.on_change = on_nav_change  # REASSIGN HANDLER

    search_bar = ft.TextField(
        hint_text="Describe your dream wallpaper...",
        border_radius=30,
        height=55,
        prefix_icon=ft.Icons.SEARCH,
        text_style=ft.TextStyle(size=16),
        cursor_color=ft.Colors.WHITE,
        filled=True,
        fill_color="#2F3E40",
        hint_style=ft.TextStyle(color=ft.Colors.GREY),
        autofocus=True,
        expand=True
    )

    page.clean()
    page.title = "Wallpaper AI - Generate"

    page.appbar = ft.AppBar(
        title=ft.Text("Wallpaper.AI"),
        center_title=True,
        leading=ft.IconButton(icon=ft.Icons.MENU, on_click=lambda _: page.open(navDrawer)),
        bgcolor="#324648"
    )
    page.bgcolor = "#1B2729"

    page.add(
    ft.Container(
        expand=True,
        alignment=ft.alignment.center,  # still fully centers layout
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(  # ⬅ shift just the gradient up a bit
                    content=ft.Container(
                        padding=5,
                        border_radius=35,
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment(-1, -1),
                            end=ft.Alignment(1, 1),
                            colors=["#00c6ff", "#0072ff"]
                        ),
                        content=ft.Container(
                            content=search_bar,
                            padding=3,
                            width=600,
                            height=55,
                            border_radius=30,
                            bgcolor="#2F3E40"
                            )
                        )
                    )
                ]
            )
        )
    )




def on_nav_change(e):
    index = navDrawer.selected_index
    match index:
        case 0:
            pass  # already on Generate
        case 2:
            settings.screen(page, navDrawer)

# Global page + navDrawer references
page = None
navDrawer = ft.NavigationDrawer(
    controls=[
        ft.Divider(),
        ft.Row(
            controls=[ft.Text("Menu", scale=1.5)],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(),
        ft.NavigationDrawerDestination(icon=ft.Icons.PALETTE, label="Generate"),
        ft.NavigationDrawerDestination(icon=ft.Icons.IMAGE, label="Library"),
        ft.NavigationDrawerDestination(icon=ft.Icons.SETTINGS, label="Settings"),
    ],
    on_change=on_nav_change
)

def main(p: ft.Page):
    global page
    page = p
    screen(page, navDrawer)

if __name__ == "__main__":
    ft.app(main)