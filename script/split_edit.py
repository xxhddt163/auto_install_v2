def split_edit(program: str, main_window: str = None):
    """
    通过程序判断默认安装目录
    :param main_window: 实例化对象的主程序窗口名
    :param program: 运行的安装程序实例化对象
    :return: 安装目录
    """
    if main_window is not None:
        program.window(title_re=main_window)['Edit'].print_control_identifiers(depth=1, filename='temp.txt')
        with open('temp.txt') as file:
            temp = file.readlines()
            temp_str = ''.join(temp)
            return temp_str.split('"')[1]
    elif main_window is None:
        program.top_window()['Edit'].print_control_identifiers(depth=1, filename='temp.txt')
        with open('temp.txt') as file:
            temp = file.readlines()
            temp_str = ''.join(temp)
            return temp_str.split('"')[1]
