import flet as ft

from bussines import find_option_index
from ui_elements.datatable import create_datatable
from ui_elements.header import create_header
from ui_elements.my_ebutton import create_my_ebutton
from ui_elements.my_dropdown import create_my_dropdown

import bussines
import os
import shutil


PATH = f'{os.getcwd()}\\assets'
print(PATH)


def main(page: ft.Page):

    def load_file_schedule(e: ft.FilePickerResultEvent):
        try:
            shutil.move(e.files[0].path, PATH)
            schedule.value = bussines.get_schedule(PATH)
            update_all()
        except:
            pass

    def select_group(e):
        option = find_option_index(dd)
        if option != None:
            show_group_schedule(dd.options.index(option))

    def update_all():
        update_dd()
        if not group.value:
            pass
        else:

            update_lv()
        page.update()

    def update_dd():
        dd.options = [ft.dropdown.Option(schedule.value[el]['group']) for el in range(0, len(schedule.value))]
        dd.autofocus = True

    def update_lv():
        dt = create_datatable(group)
        lv.controls = [dt]

    def show_group_schedule(group_index):
        group.value = schedule.value[group_index]
        update_all()

    page.title = "Schedule App"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    schedule = ft.Text('')
    schedule.visible = False

    group = ft.Text('')
    group.visible = False

    lv = ft.ListView(width=700, expand=1, spacing=10, padding=ft.Padding(top=60, left=0, right=0, bottom=0),
                     auto_scroll=False, adaptive=True)

    dd = create_my_dropdown("Choose group", select_group)

    eb = create_my_ebutton("Choose files...",
                           lambda _: file_picker.pick_files(allow_multiple=True)
                           )

    file_picker = ft.FilePicker(on_result=load_file_schedule)
    page.overlay.append(file_picker)

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    create_header(dd, eb),
                    lv
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=800,
            expand=1
        )
    )

    if ft.app:
        if os.stat(f'{PATH}').st_size != 0:
            schedule.value = bussines.get_schedule(PATH)
            show_group_schedule(0)
            dd.value = group.value['group']
            update_all()


ft.app(main)


