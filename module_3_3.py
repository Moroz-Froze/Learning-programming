# Функция с параметрами по умолчанию:
# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызов функции print_params с разным количеством аргументов, включая вызов без аргументов
print_params()  # Вывод: 1 строка True
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# 2. Распаковка параметров:
# Создание списка values_list с тремя элементами разных типов
values_list = [54.32, 'Строка', 42]

# Создание словаря values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов
values_dict = {'a': 10, 'b': 'Привет', 'c': False}

# Передача values_list и values_dict в функцию print_params с помощью распаковки параметров (* для списка и ** для словаря)
print_params(*values_list)  # Вывод: 54.32 Строка 42
print_params(**values_dict)  # Вывод: 10 Привет False

# 3. Распаковка + отдельные параметры:
# Создание список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']

# Проверка работы функции с добавлением значения 42
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42
