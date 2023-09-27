import datetime

import application.salary
import application.db.people


if __name__ == '__main__':
    hello = 'Доброго времени суток, уважаемый бухгалтер'
    print(hello)
    print('-' * len(hello))
    print(f'Текущая дата: {datetime.datetime.now().strftime("%d-%m-%Y (%H:%M:%S)")}')
    print('-' * len(hello))
    application.salary.calculate_salary()
    print('-' * len(hello))
    application.db.people.get_employees()
