from os.path import join
from os import getcwd


def load_menu() -> list:
    """读取文件列表"""
    with open(join(getcwd(), "menu.txt")) as file:
        return file.readline().split('、')
