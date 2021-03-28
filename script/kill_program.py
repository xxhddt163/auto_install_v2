from pywinauto import Application


def kill_program(title: str or list, backend: str = "win32") -> None:
    """
    链接自启动的程序并关闭
    :param backend: win32 or uia
    :param title: 自启动程序的窗口标题名
    :return: None
    """
    if type(title) is str:  # 结束的进程只有单个标题
        while True:
            try:
                temp = Application(backend=backend).connect(title=title)
            except:
                pass
            else:  # 未抛出异常时说明程序成功启动
                temp.kill()
                break
    else:  # 结束的进程有多个标题
        key = 1
        while key:
            for each in title:
                try:
                    temp = Application().connect(title=each)
                except:
                    pass
                else:
                    temp.kill()
                    key = 0
