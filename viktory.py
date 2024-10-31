"""
Программа викторина будет задавать нам вопросы несколько раз
"""
# 1. Импорт конкретных функций из модуля
# from <название модуля> import нужные функций через ,
# from famous_persons import get_random_person, get_person_and_question
#
# rounds = int(input('Сколько раз вы хотите играть?'))
#
# for i in range(rounds):
#     get_person_and_question()
#
# print('Пока!')

import random

# Список известных людей и их дат рождения
people = {
    "Толстой Л.Н.": "09.09.1828",
    "Королев С.П.": "12.01.1907",
    "Шухов В.Г.": "28.08.1853",
    "Калашников М.Т.": "10.11.1919",
    "Демидов Никита": "26.03.1656",
    "Менделеев Д.И.": "08.02.1834",
    "Ломоносов Михаил": "19.11.1711",
    "Петр I": "09.06.1672",
    "Ленин В.И.": "22.04.1870",
    "Сталин В.И.": "18.12.1878"
}

# Функция для преобразования даты из цифрового в текстовый формат
def date_to_text(date):
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    days = ['первого', 'второго', 'третьего', 'четвертого', 'пятого',
            'шестого','седьмого','восьмого', 'девятого', 'десятого',
            'одиннадцатого', 'двенадцатого', 'тринадцатого', 'четырнадцатого',
            'пятнадцатого', 'шестнадцатого', 'семнадцатого', 'восемьнадцатого',
            'девятнадцатого', 'двадцатого', 'двадцать первого', 'двадцать второго',
            'двадцать третьего', 'двадцать четвертого', 'двадцать пятого',
            'двадцать шестого', 'двадцать седьмого', 'двадцать восьмого',
            'двадцать девятого', 'тридцатого', 'тридцать первого']
    day, month, year = date.split('.')
    return f"{days[int(day)]} {months[int(month) - 1]} {year} года"

# Основная программа
def main():
    while True:
        correct_answers = 0
        random_people = random.sample(list(people.items()), 5)

        for person, dob in random_people:
            print(f"Когда родился(лась) {person}? Введите дату в формате dd.mm.yyyy")
            user_input = input().strip()
            if user_input == dob:
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неверно. Правильный ответ: {date_to_text(dob)}")

        print(f"Правильных ответов: {correct_answers}, Неправильных ответов: {5 - correct_answers}")

        try_again = input("Хотите попробовать снова? (да/нет): ").lower()
        if try_again != "да":
            break


if __name__ == "__main__":
    main()
