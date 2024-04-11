from typing import Any

import pandas as pd
import json
from numpy import arange

from pandas import DataFrame

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def load_xl_file(path: str) -> pd.DataFrame:
    return pd.read_excel(path)


def splitting_schedule(df: pd.DataFrame) -> tuple[DataFrame | None, DataFrame | None, DataFrame | None]:
    weekday = df['Unnamed: 0'].fillna(method='ffill').fillna('')
    time = df['Unnamed: 1'].fillna(method='ffill').fillna('')
    practice = df.copy()
    practice.drop(practice.columns[[0, 1]], axis=1, inplace=True)
    practice = practice.fillna(method='ffill', axis=1).fillna(method='ffill').fillna('')

    return weekday, time, practice


def df2json(df: pd.DataFrame) -> dict:
    return json.loads(df.to_json(force_ascii=False, orient='columns'))


def remove_control_char(obj_json: dict) -> dict:
    if type(list(obj_json.values())[0]) == dict:
        for key in obj_json:
            for item in obj_json[key]:
                if obj_json[key][item] == '':
                    obj_json.pop(key)
                    continue
                obj_json[key][item] = obj_json[key][item].replace('\n', ' ')
    else:
        for key in obj_json:
            obj_json[key] = obj_json[key].replace('\n', ' ')

    return obj_json


def create_readable_data(practice_json: dict, weekday_json: dict, time_json: dict) -> list[
    dict[str, list[dict[str, list[dict[str, list[Any] | Any]] | Any]] | Any]]:
    result = []
    lessons_list = []

    for key in practice_json:
        lessons = []

        for item in arange(1, len(practice_json[key]), 10):
            list_tmp = []
            for lesson in arange(item, item + 10, 2):
                list_tmp.append([practice_json[key][str(lesson)], practice_json[key][str(lesson + 1)]])
            lessons.append(list_tmp)
        lessons_list.append(lessons)

        days = []

        for day_key in weekday_json:
            if weekday_json[day_key] == '':
                continue

            times = []

            for time_key in time_json:
                if time_json[time_key] == '' or {'time': time_json[time_key], 'lessons': []} in times:
                    continue
                times.append({'time': time_json[time_key], 'lessons': []})

            if {'day': weekday_json[day_key], 'times': times} in days:
                continue
            days.append({'day': weekday_json[day_key], 'times': times})
        result.append({'direction': key, 'group': practice_json[key]['0'], 'days': days})

    for res_id in range(0, len(result)):
        for day_id in range(0, len(result[res_id]['days'])):
            for lesson_id in range(0, len(lessons_list[res_id][day_id])):
                result[res_id]['days'][day_id]['times'][lesson_id]['lessons'] = lessons_list[res_id][day_id][lesson_id]

    return result


def get_schedule(path: str) -> list[dict[str, list[dict[str, list[dict[str, list[Any] | Any]] | Any]] | Any]]:
    print('------test-------')
    doc = load_xl_file('./assets/raspisanienov.xls')

    weekday, time, practice = splitting_schedule(doc)

    weekday_json = df2json(weekday)
    time_json = df2json(time)
    practice_json = df2json(practice)

    weekday_json = remove_control_char(weekday_json)
    time_json = remove_control_char(time_json)
    practice_json = remove_control_char(practice_json)

    result = create_readable_data(practice_json, weekday_json, time_json)
    # pprint(f'data from bussines: {result}')
    # print(f'data from bussines: {practice_json}')
    # print(f'data from bussines: {practice}')

    return result
