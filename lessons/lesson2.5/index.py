import os
import sys
import subprocess


def check_result_folder():
    if os.path.exists(os.path.join(os.getcwd(), "Result")):
        print("Папки Result нет")
    else:
        print("Папки Result нет, создааем папку Result")
        subprocess.call(["mkdir", "Result"])


def copy_file_to_result():
    file_list = os.listdir(os.path.join(os.getcwd(), "Source"))

    for file in file_list:
        file_to_copy = (os.path.join(os.getcwd(), "Source", file))
        subprocess.call(["cp", file_to_copy, "Result"])
        print("Скопирован файл:", file)


def convert_imgs():
    for file in os.listdir("Result"):
        file_to_convert = (os.path.join(os.getcwd(), "Result", file))
        print("Конвертируем файл:", file)
        subprocess.call(["convert", file_to_convert, "-resize", "200", file_to_convert])




def convert_img():
    check_result_folder()
    copy_file_to_result()
    convert_imgs()



convert_img()
