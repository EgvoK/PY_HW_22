from task_01_controller import *
from task_01_view import *
from task_01 import *
import random
from threading import Thread, Lock
from time import sleep

random_numbers = []
sum_result = 0
avg_result = 0
lock = Lock()


def get_random_numbers(start_range, end_range, list_length, lock):
    lock.acquire()
    for i in range(list_length):
        random_numbers.append(random.randint(start_range, end_range))
    sleep(0.1)
    lock.release()
    list_display(random_numbers)
    return random_numbers


def get_sum_numbers(list_numbers, lock):
    lock.acquire()
    global sum_result
    for number in list_numbers:
        sum_result += number
    sum_display(sum_result)
    sleep(0.1)
    lock.release()
    return sum_result


def get_avg_numbers(list_numbers, lock):
    lock.acquire()
    global sum_result
    global avg_result
    avg_result = sum_result / len(list_numbers)
    avg_display(avg_result)
    sleep(0.1)
    lock.release()
    return avg_result


def start_threads():
    thr_1 = Thread(target=get_random_numbers, args=(ask_start_range(), ask_end_range(), ask_list_length(), lock))
    thr_2 = Thread(target=get_sum_numbers, args=(random_numbers, lock))
    thr_3 = Thread(target=get_avg_numbers, args=(random_numbers, lock))

    thr_1.start()
    thr_2.start()
    thr_3.start()

    thr_1.join()
    thr_2.join()
    thr_3.join()
