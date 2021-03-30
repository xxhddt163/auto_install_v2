from pywinauto import Application
from time import sleep


def kill_program(title: str or list, backend: str = "win32", time: int = 10) -> None:
    """
    链接自启动的程序并关闭
    :param time: 链接程序等待时间
    :param backend: win32 or uia
    :param title: 自启动程序的窗口标题名
    :return: None
    """
    if type(title) is str:  # 结束的进程只有单个标题
        while time:
            try:
                temp = Application(backend=backend).connect(title=title)
            except:
                sleep(1)
                time -= 1
            else:  # 未抛出异常时说明程序成功启动
                temp.kill()
                break
    else:  # 结束的进程有多个标题
        time *= 2
        while time:
            for each in title:
                try:
                    temp = Application().connect(title=each)
                except:
                    sleep(1)
                    time -= 1
                else:
                    temp.kill()