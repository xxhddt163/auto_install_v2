from os.path import join
from os import getcwd
from os import listdir
from pyautogui import locateOnScreen
from pyautogui import click
from pywinauto.keyboard import send_keys
from time import sleep
from pyperclip import copy


def install_from_png(app_name: str, confidence: int or float,
                     sleep_time_list: list, grayscale_list: list, skewing_list: list,
                     paste_identi: bool = False, png_file_name: str = "_shot",
                     coordinate: bool = False, edit_index: int = None, install_path: str = None) -> bool or tuple:
    # sourcery no-metrics
    """
    :param coordinate: True 就返回获取到的坐标值不执行任何操作
    :param png_file_name: png图片文件夹名称后缀
    :param paste_identi: True 字符串粘贴进去 False 字符串输入进去
    :param app_name: 程序名称
    :param edit_index: 第n张图为路径相关的截图
    :param confidence: 匹配的精度 0 - 1
    :param install_path: 程序安装目录
    :param sleep_time_list: 各张图片需要等待多长时间的列表
    :param grayscale_list: 各张图片是否灰度搜索的列表
    :param skewing_list: 各张图片偏移X，Y的列表
    :return:
    """

    path = join(getcwd(), "app_pkg", app_name + png_file_name)  # png文件所在目录
    png_list = listdir(path)  # png文件列表
    index = 0
    count = 0
    coordinate_list = list()  # 不需要操作只需要返回坐标时存储坐标信息
    for each in png_list:
        while count < 5:
            if locateOnScreen(join(path, each), confidence=confidence, grayscale=grayscale_list[index]) is not None:
                left, top, width, height = locateOnScreen(join(path, each), confidence=confidence,
                                                          grayscale=grayscale_list[index])
                x, y = left + width // 2 + skewing_list[index][0], top + height // 2 + skewing_list[index][1]
                if coordinate:
                    coordinate_list.append((x, y))
                    count = 0
                    break
                if edit_index == index:
                    if not paste_identi:
                        click(x, y)
                        send_keys('{END}')
                        send_keys('+{HOME}')
                        send_keys(join(install_path, app_name), with_spaces=True)
                        count = 0
                    elif paste_identi:
                        copy(join(install_path, app_name))
                        click(x, y)
                        send_keys('{END}')
                        send_keys('+{HOME}')
                        send_keys('^v')
                        count = 0
                else:
                    click(x, y)
                    count = 0
                break
            else:
                sleep(sleep_time_list[index])
                count += 1
        if count == 0:
            index += 1
        else:
            return False
    if not coordinate:
        return True
    elif coordinate:
        return coordinate_list
