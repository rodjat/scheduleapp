import flet as ft


def create_my_dropdown(label, func):
    return ft.Dropdown(
        on_change=func,
        label=label,
        border_color='black',
        label_style=ft.TextStyle(
            color='black'
        )
    )
