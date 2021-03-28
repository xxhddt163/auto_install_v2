from os.path import join
from os import getcwd
from os import system
from pyperclip import copy
from pyautogui import hotkey
from time import sleep


def t20_cra(install_dir: str):
    """
    激活CAD2007
    :param install_dir: 选择的安装目录
    :return:
    """
    for number in range(18, 24):
        crack_path = join(getcwd(), "app_pkg", "T20", "Crack", f"sys{number}x64", "tch_initstart.arx")
        target_path = join(install_dir, "T20", f"sys{number}x64", "tch_initstart.arx")
        system(f'xcopy "{crack_path}" "{target_path}" /Y')

    copy(join(getcwd(), "app_pkg", "T20", "Crack", "user.reg"))
    hotkey('win', 'r')
    hotkey('ctrl', 'v')
    hotkey('enter')
    sleep(2)
    hotkey('enter')
    sleep(2)
    hotkey('enter')
