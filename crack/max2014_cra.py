from os.path import join
from os import getcwd
from pywinauto import Application
from script.install_from_png import install_from_png
from pyautogui import click, tripleClick, hotkey
from pyperclip import paste, copy
from script.simple_install import simple_install
from time import sleep


def cra_3dmax(install_dir: str,
              program_name: str) -> None:
    """ 激活3dmax2014及CAD2014
    :param program_name: 程序名称 CAD2014 OR 3DMAX2014
    :param install_dir: 用户程序安装路径
    :return: None
    """
    program_name_dict = {"3DMAX2014": ['3ds Max 2014', '3dsmax'],
                         "CAD2014": ['AutoCAD 2014', 'acad']}

    program_path = join(install_dir, program_name, program_name_dict[program_name][0],
                        program_name_dict[program_name][1])  # 启动文件所在路径
    program_temp = Application().start(program_path + str(" /Language=CHS"))  # 以中文语言打开程序
    while True:
        try:
            Application().connect(title='Autodesk 许可')
        except:
            pass
        else:
            break

    sleep_time = [5, 1, 1, 1, 1]  # 各图片的等待时间
    grayscale = [True, False, True, True, True]  # 各图片是否使用灰度搜索
    skewing = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

    if install_from_png(app_name=program_name, confidence=0.8, sleep_time_list=sleep_time, grayscale_list=grayscale,
                        skewing_list=skewing, png_file_name="_shot1"):  # 点击同意协议一直到复制申请号的界面

        sleep_time = [2, 1]  # 各图片的等待时间
        grayscale = [True, True]  # 各图片是否使用灰度搜索
        skewing = [[200, 0], [0, 0]]  # x、y坐标偏移
        coordinate_list = install_from_png(app_name=program_name, confidence=0.8, sleep_time_list=sleep_time,
                                           grayscale_list=grayscale, skewing_list=skewing, png_file_name="_shot2",
                                           coordinate=True)
        if len(coordinate_list) == 2:
            _extracted_from_cra_3dmax_32(coordinate_list, program_name, program_temp)

def _extracted_from_cra_3dmax_32(coordinate_list, program_name, program_temp):
    button1 = coordinate_list[0]  # 申请号坐标
    button2 = coordinate_list[1]  # 我具有激活码坐标
    tripleClick(button1[0], button1[1])
    hotkey('ctrl', 'c')  # 复制申请号

    key_soft = Application().start(join(getcwd(), 'app_pkg', program_name, 'crack', 'xf-adsk64'))  # 打开注册机
    step = {0: ["Request :Edit", paste(), 'edit', 10],  # 将申请号粘贴
            1: ["CButton", 'click', 6],  # 按下注册机patch按钮
            2: ["确定Button", 'click', 6],  # 按下弹出窗口的确定按钮
            3: ["GButton", 'click', 6]}  # 按下注册机Gen按钮获得激活码

    if simple_install(window_backend='win32', step=step, program=key_soft):
        _extracted_from_cra_3dmax_44(key_soft, button2, program_temp)

def _extracted_from_cra_3dmax_44(key_soft, button2, program_temp):
    while True:  # 判断生成的激活码是否正确
        dict_temp = key_soft.top_window()._ctrl_identifiers()
        for each in dict_temp.keys():  # 通过按钮便签值获取激活码
            if 'Activation :Edit' in dict_temp[each]:
                temp = str(each)
        key = temp.split("'")[1]
        if len(key) == 57:
            copy(key)
            break
        else:
            key_soft.top_window()['GButton'].click_input()

    key_soft.top_window()['QQButton'].click_input()  # 按下注册机Quit按钮
    click(button2[0], button2[1])  # 按下我具有激活码坐标
    sleep(1)
    hotkey('ctrl', 'v')  # 粘贴激活码
    sleep(1)

    for _ in range(5):
        hotkey('tab')
        sleep(.5)
    hotkey('enter')
    sleep(2)
    hotkey('enter')
    sleep(5)
    program_temp.kill()
