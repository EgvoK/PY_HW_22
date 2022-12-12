#### TASK 02 ####
# Пользователь с клавиатуры вводит путь к файлу.
# После чего запускаются три потока. Первый поток заполняет файл случайными числами.
# Два других потока ожидают заполнения. Когда файл заполнен оба потока стартуют.
# Первый поток находит все простые числа, второй поток факториал каждого числа в файле.
# Результаты поиска каждый поток должен записать в новый файл.
# На экран необходимо отобразить статистику выполненных операций.

import random
import os
from threading import Thread


# C:\Users\Гарян\PY_HW_22 -- путь к файлу

class MyThread:

    def __init__(self):
        self.random_numbers = []
        self.prime_numbers = []
        self.factorial_numbers = []
        self.random_len = 10
        self.random_start = 0
        self.random_end = 10

    def write_random_file(self):
        input_path = input("Enter path for create file: ")
        random_numbers_file = os.path.join(input_path, "numbers.txt")
        with open(random_numbers_file, "w") as random_file:
            for i in range(self.random_len):
                number = random.randint(self.random_start, self.random_end)
                self.random_numbers.append(number)
                random_file.write(str(number) + "\n")
        print(f"In file {random_numbers_file} has been write numbers: {self.random_numbers}")

    def write_prime_file(self):
        with open("prime.txt", "w") as prime_file:
            for number in self.random_numbers:
                if self.is_prime(int(number)):
                    self.prime_numbers.append(number)
                    prime_file.write(str(number) + "\n")
        print(f"In file 'prime.txt' has been write numbers: {self.prime_numbers}")

    def write_factorial_file(self):
        with open("factorial.txt", "w") as factorial_file:
            for number in self.random_numbers:
                f_number = self.get_factorial(number)
                self.factorial_numbers.append(f_number)
                factorial_file.write(str(f_number) + "\n")
        print(f"In file 'factorial.txt' has been write numbers: {self.factorial_numbers}")

    @staticmethod
    def is_prime(number):
        counter = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                counter += 1
        if counter == 0:
            return number

    @staticmethod
    def get_factorial(number):
        factorial = 1
        while number > 1:
            factorial *= number
            number -= 1
        return factorial


new_thread = MyThread()

thr_1 = Thread(target=new_thread.write_random_file())
thr_2 = Thread(target=new_thread.write_prime_file())
thr_3 = Thread(target=new_thread.write_factorial_file())

thr_1.start()
thr_1.join()

thr_2.start()
thr_3.start()
