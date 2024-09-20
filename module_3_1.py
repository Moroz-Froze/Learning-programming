calls = 0

def count_calls(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

# Функция string_info для обработки строки
@count_calls
def string_info(string):
    return (len(string), string.upper(), string.lower())

# Функция is_contains для проверки наличия строки в списке
@count_calls
def is_contains(string, string_list):
    string_lower = string.lower()
    for item in string_list:
        if string_lower == item.lower():
            return True
    return False

# Пример вызова функций
info1 = string_info("Пример строки 1")
print(info1)

info2 = string_info("Пример строки 2")
print(info2)

words = ["Пример", "строки", "для", "теста"]
print(is_contains("Строки", words))  # Выведет True
print(is_contains("Найдется ли эта строка?", words))  # Выведет False

print("Количество вызовов функций:", calls)
