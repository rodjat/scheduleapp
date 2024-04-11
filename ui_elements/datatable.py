import flet as ft
from flet_core import DataTable, DataRow, DataColumn
from bussines import get_days_from_data, get_times_from_data, get_lessons_from_data


HEIGHT = 20
WIDTH_CELL_DAY = 200
WIDTH_CELL_TIME = 100
WIDTH_CELL_LESSON = 200


def create_column(text, width):
    return DataColumn(ft.Text(
        text,
        # height=HEIGHT,
        width=width,
        text_align=ft.TextAlign.CENTER
    ))


def create_row_full(day: str, time: str, lesson: str) -> DataRow:
    if lesson == 'ПУСТО':
        lesson = ''
    return DataRow(
        cells=[
            ft.DataCell(ft.Text(
                day,
                # height=HEIGHT,
                width=WIDTH_CELL_DAY,
                text_align=ft.TextAlign.CENTER
            )),
            ft.DataCell(ft.Text(
                time,
                # height=HEIGHT,
                width=WIDTH_CELL_TIME,
                text_align=ft.TextAlign.CENTER
            )),
            ft.DataCell(ft.Text(
                lesson,
                # height=HEIGHT,
                width=WIDTH_CELL_LESSON,
                text_align=ft.TextAlign.CENTER
            )),
        ]
    )


def create_datatable(data):
    dt = DataTable(
        width=700,
        horizontal_lines=ft.BorderSide(1, 'black'),
        vertical_lines=ft.BorderSide(3, 'black'),
        border=ft.border.all(2, 'black'),
        border_radius=10,
        heading_row_color=ft.colors.GREY,
        data_row_min_height=80,
        data_row_max_height=100,

    )

    days = get_days_from_data(data.value['days'])
    times = get_times_from_data(data.value['days'])
    lessons = get_lessons_from_data(data.value['days'])

    dt.columns = [
        create_column('День недели', WIDTH_CELL_DAY),
        create_column('Время', WIDTH_CELL_TIME),
        create_column('Пара', WIDTH_CELL_LESSON)
    ]
    for i in range(0, 5):
        dt.rows = dt.rows + [
            create_row_full(days[i], times[i][0], lessons[i][0][0]),
            create_row_full('', '', lessons[i][0][1]),
            create_row_full('', times[i][1], lessons[i][1][0]),
            create_row_full('', '', lessons[i][1][1]),
            create_row_full('', times[i][2], lessons[i][2][0]),
            create_row_full('', '', lessons[i][2][1]),
            create_row_full('', times[i][3], lessons[i][3][0]),
            create_row_full('', '', lessons[i][3][1]),
            create_row_full('', times[i][4], lessons[i][4][0]),
            create_row_full('', '', lessons[i][4][1]),
        ]

    return dt
