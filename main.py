import random
import string
# Задание 1

N = int(input("Введите количество паролей: "))
K = int(input("Введите длину пароля: "))
for _ in range(N):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=K))
    print(password)
#_____________________________________________________________________________


# Задание 2

import random
def generate_schedule(num_exams, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    hours = list(range(9, 15))
    minutes = ["00", 30]
    for i in range(num_exams):
        subject = random.choice(subjects)
        day = random.choice(days_of_week)
        time = f"{random.choice(hours)}:{random.choice(minutes)}"
        ticket = random.randint(1, 20)
        print(f"Экзамен по дисциплине «{subject}» состоится в {day} в {time}. Ваш счастливый билет {ticket}.")
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименование дисциплин через запятую и пробел: ").split(", ")
generate_schedule(num_exams, subjects)

#_____________________________________________________________________________


# Задание 3

import datetime

days_until_exam = int(input("Введите количество дней до экзамена: "))
current_date = datetime.datetime.now()
exam_date = current_date + datetime.timedelta(days=days_until_exam)
month_name = exam_date.strftime("%B")
print(f"Экзамен состоится {exam_date.day} {month_name}.")

#_____________________________________________________________________________



# Задание 4
from datetime import datetime, timedelta
def calculate_lucky_dates(start_date, n):
    current_date = datetime.strptime(start_date, "%Y/%m/%d").date()
    lucky_dates = []
    while len(lucky_dates) < 3:
        if current_date.weekday() != 0 and current_date.day % 4 != 0:
            lucky_dates.append(current_date.strftime("%d %B, %A"))
        current_date += timedelta(days=n)
    return lucky_dates
start_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))
lucky_dates = calculate_lucky_dates(start_date, n)
print("Счастливые даты экзамена:")
for date in lucky_dates:
    print(date)

#_____________________________________________________________________________


# main_program.py
import my_module

# Описание модуля
print(my_module.module_description())

# Использование функций из модуля
chislo = 5
print(f"Квадрат числа {chislo} равен: {my_module.square_number(chislo)}")

if my_module.is_even(chislo):
    print(f"Число {chislo} является четным.")
else:
    print(f"Число {chislo} не является четным.")
#_____________________________________________________________________________





# Задание 6

def sum_menhe_k(A, K):
    total_sum = sum(element for element in A if element < K)
    return total_sum


def main():
    N = int(input("Введите количество чисел в списке: "))
    A = []
    for i in range(N):
        num = int(input(f"Введите число {i + 1}: "))
        A.append(num)

    K = int(input("Введите значение K: "))

    result = sum_menhe_k(A, K)
    print(f"Сумма значений элементов списка A, меньших {K}, равна: {result}")


if __name__ == "__main__":
    main()
#_____________________________________________________________________________





# Задание 7

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def max_digit_sum(numbers):
    max_sum = 0
    number_with_max_sum = None

    for num in numbers:
        current_sum = sum_of_digits(num)
        if current_sum > max_sum:
            max_sum = current_sum
            number_with_max_sum = num

    return number_with_max_sum

def main():
    N = int(input("Введите количество чисел: "))
    numbers = []
    for i in range(N):
        num = int(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    max_sum = max_digit_sum(numbers)
    print(f"Число с максимальной суммой цифр: {max_sum}")

if __name__ == "__main__":
    main()

