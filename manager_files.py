
# В проекте реализовать следующий функционал:
# После запуска программы пользователь видит меню, состоящее из следующих пунктов:
# - создать папку;
# - удалить (файл/папку);
# - копировать (файл/папку);
# - просмотр содержимого рабочей директории;
# - посмотреть только папки;
# - посмотреть только файлы;
# - просмотр информации об операционной системе;
# - создатель программы;
# - играть в викторину;
# - мой банковский счет;
# - смена рабочей директории (*необязательный пункт);
# - выход.

# Программа, которая реализует указанные выше функции:

# Импортируем необходимые библиотеки:

import os
import shutil
# import platform
# import getpass
import viktory
import shopping


def create_folder():
    folder_name = input("Введите название папки: ")
    os.mkdir(folder_name)


def delete_file_or_folder():
    name = input("Введите название файла или папки для удаления: ")
    if os.path.exists(name):
        if os.path.isfile(name):
            os.remove(name)
        else:
            shutil.rmtree(name)
    else:
        print("Файл или папка не существует.")


def copy_file_or_folder():
    source = input("Введите название исходного файла или папки: ")
    destination = input("Введите название новой папки или файла: ")
    if os.path.exists(source):
        shutil.copy(source, destination)
    else:
        print("Файл или папка не найдены.")


def list_files_and_folders():
    for item in os.listdir():
        print(item)


def list_folders():
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)


def list_files():
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)


def system_info():
    print("Информация об операционной системе:")
    print(platform.platform())


def creator_info():
    print("Создатель программы: Владимир Левченко")


def main():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить файл/папку")
        print("3. Скопировать файл/папку")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_file_or_folder()
        elif choice == '3':
            copy_file_or_folder()
        elif choice == '4':
            list_files_and_folders()
        elif choice == '5':
            list_folders()
        elif choice == '6':
            list_files()
        elif choice == '7':
            system_info()
        elif choice == '8':
            creator_info()
        elif choice == '9':
            viktory.main()
        elif choice == '10':
            shopping.shopping()
        elif choice == '11':
            break
        else:
            print("Некорректный выбор. Повторите попытку.")


if __name__ == "__main__":
    main()




