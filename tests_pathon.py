#В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot

import math

# Тестируем функцию filter
def test_filter():
    result = list(filter(lambda x: x > 0, [-1, 0, 1, 2, -2]))
    assert result == [1, 2], "Ошибка в фильтрации положительных чисел"

# Тестируем функцию map
def test_map():
    result = list(map(lambda x: x * 2, [1, 2, 3]))
    assert result == [2, 4, 6], "Ошибка в удвоении элементов"

# Тестируем функцию sorted
def test_sorted():
    result = sorted([3, 1, 2])
    assert result == [1, 2, 3], "Ошибка в сортировке"

# Тестируем константу pi из модуля math
def test_pi():
    result = math.pi
    assert round(result, 5) == 3.14159, "Ошибка в значении pi"

# Тестируем функцию sqrt
def test_sqrt():
    result = math.sqrt(16)
    assert result == 4, "Ошибка в вычислении квадратного корня"

# Тестируем функцию pow
def test_pow():
    result = math.pow(2, 3)
    assert result == 8, "Ошибка в возведении в степень"

# Тестируем функцию hypot
def test_hypot():
    result = math.hypot(3, 4)
    assert result == 5, "Ошибка в вычислении гипотенузы"

# Запускаем тесты
test_filter()
test_map()
test_sorted()
test_pi()
test_sqrt()
test_pow()
test_hypot()

print("Все тесты пройдены успешно!")