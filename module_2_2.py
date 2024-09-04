# Пример ввода чисел
first = 5
second = 5
third = 7

# Условная конструкция для определения количества одинаковых чисел
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
