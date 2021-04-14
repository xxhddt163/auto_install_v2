from script.split_edit import split_edit
from os import remove
from time import sleep


def install_from_topwindow(window_backend: str, step: dict, program: str, install_path: str,
                           edit_value: int or None = None,
                           special: bool = False, edit_with_dict: bool = False, sleep_time: list or None = None):
    """
    通过window名判定程序是否就绪进行安装
    :param sleep_time: 等待时间
    :param edit_with_dict: True 将字典对应列表的[1]作为修改值，False 将字典对应列表的值改为安装路径
    :param special: 当title有重复的时设置为True 判定时有class_name
    :param edit_value: edit所在的步骤编号
    :param window_backend: 程序的运行模式
    :param step: 程序运行步骤
    :param program: 已运行程序的对象
    :param install_path: 程序安装目录
    :return: None
    """

    for i in range(len(step.keys())):
        if i == edit_value:
            edit_dir = split_edit(program=program)
            step[edit_value][0] = edit_dir
            remove('temp.txt')
        try:
            if special:
                if window_backend == 'win32':  # 通过title与class_name判定
                    next_step = program.top_window().child_window(title=step[i][0],
                                                                  class_name=step[i][1]).wait('ready',
                                                                                              timeout=step[i][-1])
                else:  # backend不是uia的情况下肯定就是win32
                    next_step = program.top_window().child_window(title=step[i][0],
                                                                  control_type=step[i][1]).wait('ready',
                                                                                                timeout=step[i][-1])
                if step[i][2] == 'click':
                    next_step.click_input()
                    if sleep_time is not None:
                        sleep(float(sleep_time[i]))
                elif step[i][2] == 'edit':
                    if edit_with_dict:
                        text_edit2(obj=next_step, backend=window_backend, edit_object=step[i][3])
                    else:
                        text_edit(obj=next_step, backend=window_backend, path=install_path)
                    if sleep_time is not None:
                        sleep(float(sleep_time[i]))
            if not special:  # 仅通过title判定
                next_step = program.top_window().child_window(title=step[i][0]).wait('ready',
                                                                                     timeout=step[i][-1])
                if step[i][1] == 'click':
                    next_step.click_input()
                    if sleep_time is not None:
                        sleep(float(sleep_time[i]))
                elif step[i][1] == 'edit':
                    if edit_with_dict:
                        text_edit2(obj=next_step, backend=window_backend, edit_object=step[i][2])
                    else:
                        text_edit(obj=next_step, backend=window_backend, path=install_path)
                    if sleep_time is not None:
                        sleep(float(sleep_time[i]))
        except RuntimeError:
            return False
    return True


def text_edit(obj: str, backend: str, path: str):
    """将edit中的内容修改为安装路径
    :param obj: 已经准备就绪的按钮或编辑框对象
    :param backend: 程序的运行模式 win32 or uia
    :param path: 程序所安装的目录
    :return:
    """
    if backend == 'win32':
        obj.set_text(path)
    elif backend == 'uia':
        obj.click_input()
        obj.type_keys('{END}')
        obj.type_keys('+{HOME}')
        obj.type_keys(path, with_spaces=True)


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
