import flet as ft

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

def screen(page: ft.Page, navDrawer, prompt):
    page.clean()
    page.title = "Wallpaper AI - Generated!"
    page.bgcolor = "#1B2729"

    Buttons = ft.Row(controls=[
        ft.ElevatedButton("Home", bgcolor="#34494C", scale=1.5),
        ft.ElevatedButton("Try again!", bgcolor="#34494C", scale=1.5),
        ft.ElevatedButton("View in Library", bgcolor="#34494C", scale=1.5)
        ], 
        # expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=60
    )

    PreviewImage = Frame(f"generated/{"_".join(prompt.split())}.png")
    page.add(ft.Column(controls=[ft.Row(controls=[PreviewImage], expand=True, alignment=ft.MainAxisAlignment.CENTER), Buttons], expand=True)) 
