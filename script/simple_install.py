from time import sleep


def simple_install(window_backend: str, step: dict, program: str, sleep_time: list or None = None):
    """ 直接通过top_window与对象名字进行安装
    :param sleep_time: 等待时间
    :param window_backend: 程序的运行模式
    :param step: 程序运行步骤
    :param program: 已运行程序的对象
    :return: None
    """
    for i in range(len(step)):
        try:
            next_step = program.top_window()[step[i][0]].wait("ready", timeout=step[i][-1])
            if step[i][-2] == 'click':
                next_step.click_input()
                if sleep_time is not None:
                    sleep(float(sleep_time[i]))
            elif step[i][-2] == 'edit':
                text_edit2(obj=next_step, backend=window_backend, edit_object=step[i][1])
                if sleep_time is not None:
                    sleep(float(sleep_time[i]))
        except RuntimeError:
            return False
    return True


def text_edit2(obj: str, backend: str, edit_object: str):
    """将edit中的内容修改为指定内容
    :param edit_object: 将edit的内容填写为edit_object的值
    :param obj: 已经准备就绪的按钮或编辑框对象
    :param backend: 程序的运行模式 win32 or uia
    :return:
    """
    if backend == 'win32':
        obj.set_text(edit_object)
    elif backend == 'uia':
        obj.click_input()
        obj.type_keys('{END}')
        obj.type_keys('+{HOME}')
        obj.type_keys(edit_object, with_spaces=True)
