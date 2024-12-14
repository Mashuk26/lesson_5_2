import os
import shutil
import tempfile
from manager_files import create_folder, delete_file_or_folder, copy_file_or_folder, list_files_and_folders, list_folders, list_files, system_info, creator_info

# Тестирование функций файлового менеджера:
def test_create_folder():
    temp_dir = tempfile.mkdtemp()     # Создаем временную дирректорию, которая автоматически будет очищена завершения тестов
    folder_name = os.path.join(temp_dir, "test_folder")

    create_folder(folder_name)

    assert os.path.exists(folder_name), "Папка не была создана."

    # Удаление тестовой папки
    shutil.rmtree(folder_name)
    shutil.rmtree(temp_dir)


def test_delete_file_or_folder():
    temp_dir = tempfile.mkdtemp()
    folder_name = os.path.join(temp_dir, "test_folder")
    os.mkdir(folder_name)

    delete_file_or_folder(folder_name)

    assert not os.path.exists(folder_name), "Папка не была удалена."

    # Удаление временной директории
    shutil.rmtree(temp_dir)


def test_copy_file_or_folder():
    temp_dir = tempfile.mkdtemp()
    source_file = os.path.join(temp_dir, "test_file.txt")
    with open(source_file, 'w') as f:
        f.write("Тестовое содержимое.")

    destination_file = os.path.join(temp_dir, "copied_file.txt")

    copy_file_or_folder(source_file, destination_file)

    assert os.path.exists(destination_file), "Файл не был скопирован."

    # Удаление временных файлов
    os.remove(source_file)
    os.remove(destination_file)
    shutil.rmtree(temp_dir)


def test_list_files_and_folders():
    temp_dir = tempfile.mkdtemp()
    file1 = os.path.join(temp_dir, "file1.txt")
    file2 = os.path.join(temp_dir, "file2.txt")

    with open(file1, 'w'), open(file2, 'w'):
        pass

    items = list_files_and_folders()

    assert "file1.txt" in items and "file2.txt" in items, "Не все файлы отображаются."

    # Удаление временных файлов
    os.remove(file1)
    os.remove(file2)
    shutil.rmtree(temp_dir)


def test_list_folders_and_files():
    temp_dir = tempfile.mkdtemp()

    folder1 = os.path.join(temp_dir, "folder1")
    folder2 = os.path.join(temp_dir, "folder2")

    os.mkdir(folder1)
    os.mkdir(folder2)

    folders = list_folders()

    assert folder1.split('/')[-1] in folders and folder2.split('/')[-1] in folders, "Не все папки отображаются."

    # Удаление временных папок
    shutil.rmtree(folder1)
    shutil.rmtree(folder2)
    shutil.rmtree(temp_dir)


# Запуск тестов
if __name__ == "__main__":
    test_create_folder()
    test_delete_file_or_folder()
    test_copy_file_or_folder()
    test_list_files_and_folders()
    test_list_folders_and_files()

print("Все тесты прошли успешно!")
