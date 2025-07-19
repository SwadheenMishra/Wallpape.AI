import flet as ft
import main
import Library
import json

def fetch_API_Key(Path: str = "API_KEY/api_key.json") -> str:
    with open(Path, "r") as f:
        key_data = json.load(f)
    return key_data

def update_api_key(new_key: str, path: str = "API_KEY/api_key.json"):
    try:
        with open(path, "w") as f:
            json.dump({"key": new_key}, f, indent=4)
        print("API key updated.")
    except Exception as e:
        print("Failed to update API key:", e)


def screen(page: ft.Page, navDrawer):
    def on_nav_change(e):
        index = navDrawer.selected_index
        match index:
            case 0:
                main.screen(page, navDrawer)
            case 1:
                Library.screen(page,navDrawer)
            case 2:
                pass  # already on Settings

    navDrawer.on_change = on_nav_change

    page.clean()
    page.title = "Wallpaper AI - Settings!"

    keyData = fetch_API_Key()

    if (k := keyData["key"]) == "None":
        InputAPI = ft.TextField(hint_text="Enter your API key!")
    else:
        InputAPI = ft.TextField(value=k)    

    page.appbar = ft.AppBar(
        title=ft.Text("Settings!"),
        center_title=True,
        leading=ft.IconButton(icon=ft.Icons.MENU, on_click=lambda _: page.open(navDrawer)),
        bgcolor="#324648"
    )

    InputAPI.on_change = lambda e: update_api_key(e.control.value)

    page.bgcolor = "#1B2729"
    page.add(ft.Row(controls=[ft.Column(controls=[ft.Text("Note: The API key will be stored locally so dont worry about it getting leaked!", theme_style=ft.TextStyle.italic), InputAPI], expand=True)], expand=True, alignment=ft.MainAxisAlignment.CENTER))
