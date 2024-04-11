
def find_option_index(dropdown):
    option_name = dropdown.value
    for option in dropdown.options:
        if option_name == option.key:
            return option
    return None


def get_days_from_data(data):
    monday = data[0]['day']
    tuesday = data[1]['day']
    wednesday = data[2]['day']
    thursday = data[3]['day']
    friday = data[4]['day']

    return [monday, tuesday, wednesday, thursday, friday]


def get_list_times_for_day(times):
    list_ = []
    for el in times:
        list_.append(el['time'])
    return list_


def get_times_from_data(data):
    monday = get_list_times_for_day(data[0]['times'])
    tuesday = get_list_times_for_day(data[1]['times'])
    wednesday = get_list_times_for_day(data[2]['times'])
    thursday = get_list_times_for_day(data[3]['times'])
    friday = get_list_times_for_day(data[4]['times'])

    return [monday, tuesday, wednesday, thursday, friday]


def get_list_lessons_for_time(times):
    list_ = []
    for el in times:
        list_.append(el['lessons'])
    return list_


def get_lessons_from_data(data):
    monday = get_list_lessons_for_time(data[0]['times'])
    tuesday = get_list_lessons_for_time(data[1]['times'])
    wednesday = get_list_lessons_for_time(data[2]['times'])
    thursday = get_list_lessons_for_time(data[3]['times'])
    friday = get_list_lessons_for_time(data[4]['times'])

    return [monday, tuesday, wednesday, thursday, friday]