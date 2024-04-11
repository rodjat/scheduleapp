import flet as ft


def create_header(dropdown: ft.Control, elbutton: ft.Control) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            [
                dropdown,
                elbutton
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        alignment=ft.Alignment(0, 0),
        padding=ft.Padding(10, 10, 10, 10)
    )
