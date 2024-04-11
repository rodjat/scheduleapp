import flet as ft


def create_my_ebutton(text, func):
    return ft.ElevatedButton(
        text=text,
        on_click=func,
        color='black',
        style=ft.ButtonStyle(
            color='black',
            bgcolor='white',
            shadow_color='lightgrey',
            overlay_color='lightgrey',
        ),
        adaptive=True
    )
