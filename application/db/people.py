from russian_names import RussianNames


def get_employees():
    print(f'Список сотрудников:')
    print(*RussianNames(count=7), sep='\n')
