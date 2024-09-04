#1st program
print(9 ** 0.5 * 5)

#2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

#3rd program
a= 2*2+2
b = 2*(2+2)
print(a)
print(b)
print(a == b)

# 4th program
number = '123.456'
fractional_part = number.split('.')[1]
print(fractional_part[0])

# 4th program
number = '123.56'
float_number = float(number)  # Преобразование строки в дробное число
shifted_number = float_number * 10  # Умножение на 10, чтобы сместить 4 в целую часть
first_digit = int(shifted_number) % 10  # Получение первой цифры после запятой
print(first_digit)

#15.08.2024

example = "Привет"  # Любая строка

# Первый символ строки
print(example[0])

# Последний символ строки с использованием отрицательного индекса
print(example[-1])

# Вторая половина строки (с нечётным количеством символов)
half_length = len(example) // 2
print(example[half_length:])

# Строка наоборот
print(example[::-1])

# Каждый второй символ
print(example[1::2])




#17.08.2024

course_name = 'Python'
number_of_homework = 12
hours_spent = 1.5
time_per_assignment = hours_spent / number_of_homework

print(f"Курс: {course_name}, всего задач: {number_of_homework}, затрачено часов: {hours_spent}, среднее время выполнения {time_per_assignment} часа.")

#21.08.2024

print('Hi, PyCharm')
x = 43
y = 32
print(x * y)
print("End line")