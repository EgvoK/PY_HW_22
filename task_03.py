#### TASK 03 ####
# Пользователь с клавиатуры вводит путь к существующей директории и к новой директории.
# После чего запускается поток, который должен скопировать содержимое директории в новое место.
# Необходимо сохранить структуру директории.
# На экран необходимо отобразить статистику выполненных операций.

import os
import shutil
from shutil import *
from threading import Thread


# "C:/Users/Гарян/PY_HW_22/dir_1_03/" -- source_path
# "C:/Users/Гарян/PY_HW_22/dir_2_03/" -- destination_path
def copy_dir():

    source_path = input("Enter path of source directory: ")
    destination_path = input("Enter path of destination directory: ")

    for item in os.listdir(source_path):
        source = os.path.join(source_path, item)
        destination = os.path.join(destination_path, item)
        if os.path.isdir(source):
            shutil.copytree(source, destination, symlinks=False, ignore=None)
        else:
            shutil.copy2(source, destination)
    for item in os.listdir(destination_path):
        print(f"{item} has been copy in folder {destination_path}")


thr_1 = Thread(target=copy_dir(), args=())
thr_1.start()






