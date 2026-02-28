value = "хер моржовый" 
print("Текст:", value)

value = 321;
print("Число:", value)

name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
print("Ваше имя:", name)
print("Ваш возраст:", age)

txt = "(2+3)/0.25-4*2.1"
print(txt, "=", eval(txt))
res = input("Введите выражение: ")
print("Значение выражения:", eval(res))

number = int(input("Введите целое число: "))
if number%2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

day = input("Какое сегодня число? ")
month = input("Какой сегодня месяц? ")
print("Сегодня:", day)
print("Месяц:", month)


current_year = int(input("Введите текущий год: "))
birth_year = int(input("Введите свой год рождения: "))
your_age = current_year - birth_year
print("Ваш возраст:", your_age)

distance_in_miles = float(input("Введите расстояние в милях: "))
distance_in_kilometers = distance_in_miles * 1.6
print("Расстояние в километрах:", distance_in_kilometers)

# Запрашиваем размер списка
n = int(input("Сколько степеней числа 2 вывести? Введите число: "))
powers_of_two = [2 ** i for i in range(n)]
print("Список степеней двойки:", powers_of_two)

number = int(input("Введите число: "))
if number%3 == 0:
    print("Число делится на 3")
else:
    print("Число не делится на 3")


from enum import unique
import numbers


def second_lagest_number(num):
    unique_numbers = list(set(num))
    if len(unique_numbers) < 2:
        raise ValueError ("Во входном списке должно быть хотя бы 2 числа!")

    unique_numbers.sort() # сортируем по названию
    return unique_numbers[-2] # второе с конца - второе по величение число

user_input = input("Введите числа через пробел :  ")
numbers = list(map(int,user_input.split()))

try:    
    result = second_lagest_number(numbers)
    print("Второе по величение число:", result)
except ValueError as e:
    print(f"Хуй моржовый", e)


def sum_of_odd_numbers(count):
    total = 0
    for i in range(count):
        num = int(input(f"Введите число {i + 1}: "))
        if num % 2 != 0:          # если число нечётное
            total += num
    return total


# пример использования
n = int(input("Сколько чисел будете вводить? "))
result = sum_of_odd_numbers(n)
print("Сумма нечётных чисел:", result)



    