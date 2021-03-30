from easygui import textbox
from time import localtime, strftime
from time import sleep
from os.path import join
from os import getcwd
from os import system
from pywinauto import Application
from pyautogui import hotkey
from script.load_menu import load_menu
from script.format_menu import format_menu
from script.running_time import running_time
from script.kill_program import kill_program
from script.install_from_png import install_from_png
from script.txt_change import txt_change
from script.install import install
from script.install_from_topwindow import install_from_topwindow
from script.simple_install import simple_install
from crack.office2013_cra import office_crack
from crack.pscc2018_cra import ps_crack
from crack.prcc2018_cra import pr_crack
from crack.max2014_cra import cra_3dmax
from crack.cad2007_cra import cad2007_cra
from crack.t20_cra import t20_cra
import sys
from pyperclip import copy, paste
import tkinter as tk
from script.choose_dir import choose_dir
import _thread


class Ui:
    def __init__(self):
        self.choose = r'D:\Program Files (x86)'  # 安装目录

    def auto_install(self):
        """
        安装程序的主函数
        :param install_path: 程序安装路径
        :return:
        """
        choose = self.choose
        sys.stderr = open('stdout.log', 'a')  # 错误信息输出到文件
        start_time = (strftime("%H:%M", localtime()))  # 获取运行程序时的开始时间
        failure = []  # 保存安装失败的软件名称
        menu = load_menu()  # 读取安装目录下的menu.txt获取需要安装的文件
        menu_change = menu.copy()

        for each in menu:

            labelframe1 = tk.LabelFrame(self.root, text=f'安装进度（第{menu.index(each) + 1}个，共{len(menu)}个）', height=80,
                                        width=300)  # 信息区
            labelframe1.grid(row=1, column=0, columnspan=10, padx=10, pady=10)
            labelframe1.propagate(0)  # 使组件大小不变，此时width才起作用
            tk.Label(labelframe1, text=f"正在安装{format_menu(each.split())[0]}...", font=(', 11')).pack(fill="both",
                                                                                                     expand="yes")

            if each == 'QQ':
                main_window = ["腾讯QQ安装向导", "win32", "QQ"]
                step = {0: ["自定义选项", 'click', 15],
                        1: ["添加到快速启动栏", 'click', 6],
                        2: ["开机自动启动", 'click', 6],
                        3: ['', 'edit', 6],
                        4: ["立即安装", 'click', 6],
                        5: ["完成安装", 'click', 40]}

                program = Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', 'QQ', 'QQ.exe'))

                if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                           program=program, install_path=join(choose, each), edit_value=3):
                    kill_program(main_window[2])
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == 'Wechat':
                main_window = ["微信安装向导", "uia", "微信"]
                step = {0: ["更多选项", 'click', 40],
                        1: ["程序安装目录", 'edit', 6],
                        2: ["安装微信", 'click', 6],
                        3: ['开始使用', 'click', 40]}

                program = Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', 'wechat', 'wechat.exe'))

                if install(main_window=main_window[0], window_backend=main_window[1], step=step, program=program,
                           install_path=join(choose, each)):
                    kill_program(main_window[2])
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == 'Dtalk':
                main_window = ["钉钉 安装", "win32"]
                step = {0: ["下一步(&N) >", 'click', 30],
                        1: ["", 'edit', 6],
                        2: ["下一步(&N) >", 'click', 6],
                        3: ["运行 钉钉(&R)", 'click', 40],
                        4: ["完成(&F)", 'click', 6]}

                program = Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', 'Dtalk', 'Dtalk.exe'))

                if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                           program=program, install_path=join(choose, each), edit_value=1):
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == 'Winrar':
                main_window = ["WinRAR 5.91", "win32", 10]
                step = {0: ["", "Edit", 'edit', 6],
                        1: ["安装", "Button", 'click', 6]}

                program = Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', 'Winrar', 'Winrar.exe'))

                if install(main_window=main_window[0], window_backend=main_window[1], step=step, program=program,
                           install_path=join(choose, each), edit_value=0, special=True):

                    while True:
                        try:
                            temp = Application().connect(title="WinRAR 简体中文版安装")
                        except:
                            pass
                        else:  # 未抛出异常时说明程序成功链接
                            for button in ["确定", "完成"]:
                                temp2 = temp.window(title='WinRAR 简体中文版安装').child_window(title=button).wait('ready',
                                                                                                            timeout=30)
                                temp2.click()
                            break
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == 'VCRedist' or each == 'DX' or each == 'NF3':
                main_window = "win32"
                step = {0: ["确定", 'click', 10],
                        1: ["是(&Y)", 'click', 10]}
                sleep_time = [1, 0]
                program = Application(backend=main_window).start(join(getcwd(), 'app_pkg', each, each))

                if install_from_topwindow(window_backend=main_window, step=step, program=program,
                                          install_path=join(choose, each), sleep_time=sleep_time):
                    ok_dict = {'DX': 'DirectX 9.0c 安装完成！程序即将退出',
                               'VCRedist': 'Visual C++ 运行库 安装完成！程序即将退出',
                               'NF3': '.Net Framework 安装完成！程序即将退出'}
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                    while True:
                        try:
                            if program.window(title_re='信息').child_window(title=ok_dict[each]).exists():
                                break
                        except:
                            sleep(1)
                    program.window(title_re='信息').child_window(title=ok_dict[each]).wait('ready', timeout=80)
                    program.window(title_re='信息').child_window(title="确定").click_input()
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == 'OFFICE2013':
                main_window = ["Microsoft Office Professional Plus 2013", "uia"]
                step = {0: ["我接受此协议的条款", "CheckBox", 'click', 20],
                        1: ["继续", "Button", 'click', 6],
                        2: ["自定义", "Button", 'click', 6],
                        3: ["Microsoft Access", "MenuItem", 'click', 6],
                        4: ["不可用", "Button", 'click', 6],
                        5: ["Microsoft InfoPath", "MenuItem", 'click', 6],
                        6: ["不可用", "Button", 'click', 6],
                        7: ["Microsoft Lync", "MenuItem", 'click', 6],
                        8: ["不可用", "Button", 'click', 6],
                        9: ["Microsoft OneNote", "MenuItem", 'click', 6],
                        10: ["不可用", "Button", 'click', 6],
                        11: ["Microsoft Outlook", "MenuItem", 'click', 6],
                        12: ["不可用", "Button", 'click', 6],
                        13: ["Microsoft Publisher", "MenuItem", 'click', 6],
                        14: ["不可用", "Button", 'click', 6],
                        15: ["Microsoft SkyDrive Pro", "MenuItem", 'click', 6],
                        16: ["不可用", "Button", 'click', 6],
                        17: ["Microsoft Visio Viewer", "MenuItem", 'click', 6],
                        18: ["不可用", "Button", 'click', 6],
                        19: ["文件位置", "TabItem", 'click', 6],
                        20: ["", "Edit", 'edit', 10],
                        21: ["立即安装", "Button", 'click', 6]}

                program = Application(backend=main_window[1]).start(
                    join(getcwd(), 'app_pkg', 'OFFICE2013', 'setup.exe'))

                if install(main_window=main_window[0], window_backend=main_window[1], step=step, program=program,
                           install_path=join(choose, each), edit_value=20, special=True):
                    program.window(title_re='Microsoft Office Professional Plus 2013').child_window(title="继续联机",
                                                                                                    control_type="Button"
                                                                                                    ).wait('ready',
                                                                                                           timeout=600)
                    program.window(title_re='Microsoft Office Professional Plus 2013')['关闭Button'].click_input()
                    office_crack(choose)  # 激活office
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == "WPS":
                sleep_time = [5, 1, 1, 1]  # 各图片的等待时间
                grayscale = [True, True, True, False]  # 各图片是否使用灰度搜索
                skewing = [[0, 0], [0, 0], [-200, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", 'WPS', 'wpssetup_k56008174_281235.exe'))  # 打开指定的安装程序

                result = install_from_png(app_name=each, edit_index=2,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                else:
                    failure.extend(format_menu(each.split()))

            if each == '360drv':
                main_window = ["欢迎使用 360驱动大师", "uia"]
                step = {0: ["已经阅读并同意", 'CheckBox', 'click', 10],
                        1: ["", 'Edit', 'edit', 6],
                        2: ["安装完成后打开360驱动大师", 'CheckBox', 'click', 6],
                        3: ["立即安装", 'Button', 'click', 6]}

                sleep_time = [3]  # 各图片的等待时间
                grayscale = [True]  # 各图片是否使用灰度搜索
                skewing = [[0, 0]]  # x、y坐标偏移

                program = Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', each, each))

                result = install_from_png(app_name=each, confidence=0.8, install_path=choose,
                                          sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing)  # 第一个按钮获取不到用png图片匹配
                if result:
                    if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                               program=program, install_path=join(choose, each), edit_value=1,
                               special=True):  # 图片匹配成功后再用pywinauto控制
                        txt_change(prom_name=each, menu_change=menu_change)
                    else:
                        failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序
                else:
                    failure.extend(format_menu(each.split()))

            if each == "Chrome":
                program = Application(backend='win32').start(join(getcwd(), 'app_pkg', each, each))
                txt_change(prom_name=each, menu_change=menu_change)
                while True:
                    if not program.is_process_running():
                        break
                kill_program("欢迎使用 Chrome - Google Chrome")

            if each == "2345explorer":
                sleep_time = [5, 1]  # 各图片的等待时间
                grayscale = [True, False]  # 各图片是否使用灰度搜索
                skewing = [[300, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", each, '2345explorer_k56008174.exe'))  # 打开指定的安装程序
                result = install_from_png(app_name=each, edit_index=0,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing, paste_identi=True)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                    kill_program(title=['2345网址导航－开创中国百年品牌（已创建11年整） - 2345加速浏览器 10.14', '网络不稳定或断网 - 2345加速浏览器 10.14'])
                else:
                    failure.extend(format_menu(each.split()))

            if each == "TXvideo":
                main_window = ["腾讯视频 2020 安装程序 ", "win32"]
                step = {0: ["自定义安装", 'click', 30],
                        1: ["开机自动启动", 'click', 6],
                        2: ["", 'edit', 6],
                        3: ["立即安装", 'click', 8],
                        4: ["立即体验", 'click', 90]}

                program = Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', each, each))

                if install(main_window=main_window[0], window_backend=main_window[1], step=step, program=program,
                           install_path=join(choose, each), edit_value=2):
                    txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                    kill_program(title='腾讯视频')
                else:
                    failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序

            if each == "IQIYI":
                main_window = ["爱奇艺 安装向导", "win32"]
                step = {0: ["阅读并同意", 'click', 30],
                        1: ["", 'edit', 6],
                        2: ["立即安装", 'click', 6],
                        3: ["完成", 'click', 90]}

                Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', each, 'iqiyi_k56008174_107328.exe'))
                while True:
                    try:
                        program = Application(backend=main_window[1]).connect(
                            title_re=main_window[0])  # 直接打开的程序对象不能直接使用需要重新链接
                    except:
                        pass
                    else:
                        if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                                   program=program,
                                   install_path=join(choose, each), edit_value=1):
                            txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                            break
                        else:
                            failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序
                            break

            if each == "PSCS3":
                main_window = ["安装 - Adobe Photoshop CS3 Extended", "win32"]
                step = {0: ["下一步(&N) >", "TButton", 'click', 10],
                        1: [r"C:\Program Files (x86)\Adobe\Adobe Photoshop CS3", "TEdit", 'edit', 6],
                        2: ["下一步(&N) >", "TButton", 'click', 6],
                        3: ["下一步(&N) >", "TButton", 'click', 6],
                        4: ["安装(&I)", "TButton", 'click', 6],
                        5: ["完成(&F)", "TButton", 'click', 60]}

                Application(backend=main_window[1]).start(join(getcwd(), 'app_pkg', each, each))
                while True:
                    try:
                        program = Application(backend=main_window[1]).connect(
                            title='安装')  # 直接打开的程序对象不能直接使用需要重新链接
                    except:
                        pass
                    else:
                        if install(main_window=main_window[0], window_backend=main_window[1], step=step,
                                   program=program,
                                   install_path=join(choose, each), edit_value=100, special=True):
                            txt_change(prom_name=each, menu_change=menu_change)  # 安装成功修改menu文件
                            break
                        else:
                            failure.extend(format_menu(each.split()))  # 安装失败记录安装失败程序
                            break

            if each == "PSCC2018":  # PSCC2018打开自动安装不需要任何按钮
                if "PSCS3" in menu:  # 防止装完PSCS3马上打开程序报错
                    sleep(5)
                ps_path = join(getcwd(), "app_pkg", each, 'Set-up')
                copy(ps_path)
                hotkey('win', 'r')
                hotkey('ctrl', 'v')
                hotkey('enter')
                while True:
                    try:
                        ps_cc = Application().connect(path=paste())
                    except:
                        pass
                    else:
                        break

                while True:
                    if not ps_cc.is_process_running():
                        break
                txt_change(prom_name=each, menu_change=menu_change)
                kill_program(title='Adobe Photoshop CC 2018')
                ps_crack()

            if each == "PRCC2018":  # PRCC2018打开自动安装不需要任何按钮
                pr_path = join(getcwd(), "app_pkg", each, 'Set-up')
                copy(pr_path)
                hotkey('win', 'r')
                hotkey('ctrl', 'v')
                hotkey('enter')
                while True:
                    try:
                        pr_cc = Application().connect(path=paste())
                    except:
                        pass
                    else:
                        break

                while True:
                    if not pr_cc.is_process_running():
                        break
                txt_change(prom_name=each, menu_change=menu_change)
                kill_program(title='Adobe Premiere Pro CC 2018')
                pr_crack()

            if each == "163music":
                sleep_time = [5, 1, 1, 1, 1, 5]  # 各图片的等待时间
                grayscale = [True, True, True, True, True, True]  # 各图片是否使用灰度搜索
                skewing = [[0, 0], [0, 0], [0, 0], [-230, 0], [0, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", each, each))  # 打开指定的安装程序

                result = install_from_png(app_name=each, edit_index=3,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing, paste_identi=True)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                    while True:
                        try:
                            Application(backend='uia').connect(title='网易云音乐')
                        except:
                            pass
                        else:
                            system('taskkill /IM cloudmusic.exe /F')
                            sleep(3)
                            break
                else:
                    failure.extend(format_menu(each.split()))

            if each == "QQmusic":
                sleep_time = [5, 1, 1, 1, 5]  # 各图片的等待时间
                grayscale = [True, True, True, True, True]  # 各图片是否使用灰度搜索
                skewing = [[0, 0], [0, 0], [-230, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", each, 'QQMusic_YQQFullStack'))  # 打开指定的安装程序

                result = install_from_png(app_name=each, edit_index=2,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing, paste_identi=True)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                    kill_program(title='QQ音乐', backend='uia')
                else:
                    failure.extend(format_menu(each.split()))

            if each == "Kugou":
                sleep_time = [5, 1, 1, 1, 1, 1, 8]  # 各图片的等待时间
                grayscale = [True, True, True, True, True, True, True]  # 各图片是否使用灰度搜索
                skewing = [[0, 0], [-250, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", each, 'kugou_k56008174_306395'))  # 打开指定的安装程序

                result = install_from_png(app_name=each, edit_index=1,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing, paste_identi=True)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                    kill_program(title='酷狗音乐', backend='uia')
                else:
                    failure.extend(format_menu(each.split()))

            if each == "SougouPY":
                sleep_time = [5, 1, 1, 1, 1, 8]  # 各图片的等待时间
                grayscale = [True, True, True, True, True, True]  # 各图片是否使用灰度搜索
                skewing = [[0, 0], [0, 0], [0, 0], [70, 0], [0, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", each, each))  # 打开指定的安装程序

                result = install_from_png(app_name=each, edit_index=3,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing, paste_identi=True)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                else:
                    failure.extend(format_menu(each.split()))

            if each == "2345pinyin":
                sleep_time = [5, 1, 1, 10]  # 各图片的等待时间
                grayscale = [True, True, True, True]  # 各图片是否使用灰度搜索
                skewing = [[40, 0], [0, 0], [0, 0], [0, 0]]  # x、y坐标偏移

                Application().start(join(getcwd(), "app_pkg", each, '2345pinyin_k56008174.exe'))  # 打开指定的安装程序

                result = install_from_png(app_name=each, edit_index=0,
                                          confidence=0.8, install_path=choose, sleep_time_list=sleep_time,
                                          grayscale_list=grayscale, skewing_list=skewing, paste_identi=True)  # 采用全图片匹配
                if result:
                    txt_change(prom_name=each, menu_change=menu_change)
                else:
                    failure.extend(format_menu(each.split()))

            if each == "3DMAX2014":
                step = {0: ["ListBox3", 'click', 30],
                        1: ["我接受Button", 'click', 6],
                        2: ["下一步Button", 'click', 6],
                        3: ["序列号:Edit", '666', 'edit', 6],
                        4: ["Edit2", '69696969', 'edit', 6],
                        5: ["产品密钥:Edit5", '128F1', 'edit', 6],
                        6: ["下一步Button", 'click', 6],
                        7: ["安装路径:Edit", join(choose, each), 'edit', 6],
                        8: ["安装Button", 'click', 6]}

                setup_path = join(getcwd(), "app_pkg", each, "Setup.exe")
                copy(setup_path)
                hotkey('win', 'r')
                hotkey('ctrl', 'v')
                hotkey('enter')
                while True:
                    try:
                        program = Application().connect(title="Autodesk 3ds Max 2014")
                    except:
                        pass
                    else:
                        break
                if simple_install(window_backend='win32', step=step, program=program):
                    while True:
                        try:
                            temp = Application().connect(title_re='文件正在使用')
                            if temp.top_window().window(title='忽略(&I)').exists():
                                temp.top_window()['忽略(&I)'].click_input()
                        except:
                            pass

                        if program.top_window().child_window(title="完成").exists():
                            program.top_window().child_window(title="完成").wait("ready", timeout=10)
                            program.top_window()['完成'].click_input()
                            txt_change(prom_name=each, menu_change=menu_change)
                            break
                        else:
                            sleep(3)
                    cra_3dmax(choose, each)
                else:
                    failure.extend(format_menu(each.split()))

            if each == "CAD2014":
                step = {0: ["ListBox3", 'click', 30],
                        1: ["我接受Button", 'click', 6],
                        2: ["下一步Button", 'click', 6],
                        3: ["序列号:Edit", '666', 'edit', 6],
                        4: ["Edit2", '69696969', 'edit', 6],
                        5: ["产品密钥:Edit5", '001F1', 'edit', 6],
                        6: ["下一步Button", 'click', 6],
                        7: ["安装路径:Edit", join(choose, each), 'edit', 6],
                        8: ["安装Button", 'click', 6]}

                setup_path = join(getcwd(), "app_pkg", each, "Setup.exe")
                copy(setup_path)
                hotkey('win', 'r')
                hotkey('ctrl', 'v')
                hotkey('enter')

                while True:
                    try:
                        program = Application().connect(title="Autodesk® AutoCAD® 2014")
                    except:
                        pass
                    else:
                        break
                if simple_install(window_backend='win32', step=step, program=program):
                    while True:
                        try:
                            temp = Application().connect(title_re='文件正在使用')
                            if temp.top_window().window(title='忽略(&I)').exists():
                                temp.top_window()['忽略(&I)'].click_input()
                        except:
                            pass

                        if program.top_window().child_window(title="完成").exists():
                            program.top_window().child_window(title="完成").wait("ready", timeout=10)
                            program.top_window()['完成'].click_input()
                            txt_change(prom_name=each, menu_change=menu_change)
                            break
                        else:
                            sleep(3)
                    cra_3dmax(choose, each)
                else:
                    failure.extend(format_menu(each.split()))

            if each == "CAD2007":
                program = Application().start(join(getcwd(), "app_pkg", each, 'setup'))
                if program.top_window()['确定Button'].wait("ready", timeout=10) and program.top_window()[
                    '确定Button'].exists():
                    sleep(1)
                    program.top_window()['确定Button'].click_input()
                while True:
                    try:
                        program = Application().connect(title="AutoCAD 2007 安装")
                    except:
                        pass
                    else:
                        break
                step = {0: ["Button2", 'click', 10],
                        1: ["RadioButton2", 'click', 6],
                        2: ["Button0", 'click', 6],
                        3: ["Edit1", '000', 'edit', 6],
                        4: ["Edit2", '00000000', 'edit', 6],
                        5: ["Button1", 'click', 6],
                        6: ["Edit1", "admin", 'edit', 6],
                        7: ["Edit2", "admin", 'edit', 6],
                        8: ["Edit3", "admin", 'edit', 6],
                        9: ["Edit4", "admin", 'edit', 6],
                        10: ["Edit5", "admin", 'edit', 6],
                        11: ["Button1", "click", 6],
                        12: ["Button1", "click", 6],
                        13: ["Button1", "click", 6],
                        14: ["Edit", join(choose, each), 'edit', 6],
                        15: ["Button1", "click", 6],
                        16: ["Button1", "click", 6],
                        17: ["Button1", "click", 6]}
                sleep_time = [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 3, 3, 0, 3, 3, 3]
                if simple_install(window_backend="win32", step=step, program=program, sleep_time=sleep_time):
                    sleep(5)
                    try:
                        Application().connect(title="AutoCAD 2007 安装程序")
                    except:
                        failure.extend(format_menu(each.split()))
                        break
                    sleep(2)
                    while True:
                        try:
                            program = Application().connect(title="AutoCAD 2007 安装程序")
                            if program.top_window()['完成(&F)'].exists():
                                break
                        except:
                            sleep(1)
                    step = {0: ["CheckBox", 'click', 8],
                            1: ["Button1", 'click', 6]}
                    simple_install(window_backend="win32", step=step, program=program)
                    txt_change(prom_name=each, menu_change=menu_change)
                    cad2007_cra(choose)
                else:
                    failure.extend(format_menu(each.split()))

            if each == "T20":
                program = Application().start(join(getcwd(), "app_pkg", each, 'setup'))
                while True:
                    if program.top_window()["我接受许可证协议中的条款((&A)RadioButton"].exists():
                        break
                    else:
                        sleep(1)

                step = {0: ["我接受许可证协议中的条款((&A)RadioButton", 'click', 10],
                        1: ["下一步(&N) >Button", 'click', 6],
                        2: ["浏览(&R)...Button", 'click', 6],
                        3: ["路径(&P)：Edit", join(choose, each), 'edit', 6],
                        4: ["确定Button", 'click', 6],
                        5: ["下一步(&N) >Button", 'click', 6],
                        6: ["下一步(&N) >Button", 'click', 6]}
                sleep_time = [0, 2, 1, 0, 0.5, 0.5, 0]
                if simple_install(window_backend="win32", step=step, program=program, sleep_time=sleep_time):
                    while True:
                        try:
                            if program.top_window()['InstallShield Wizard 完成'].exists():
                                break
                        except:
                            sleep(1)
                    step = {0: ["完成Button", 'click', 10]}
                    if simple_install(window_backend="win32", step=step, program=program):
                        t20_cra(choose)
                        txt_change(prom_name=each, menu_change=menu_change)
                else:
                    failure.extend(format_menu(each.split()))

        end_time = strftime("%H:%M", localtime())  # 获取程序安装结束时的时间
        menu = format_menu(menu)
        labelframe1 = tk.LabelFrame(self.root, text="", height=80, width=300)  # 信息区
        labelframe1.grid(row=1, column=0, columnspan=10, padx=10, pady=10)
        labelframe1.propagate(0)  # 使组件大小不变，此时width才起作用
        tk.Label(labelframe1,
                 text=f"程序安装完毕，用时{running_time(start_time, end_time)}分钟，共选择了{len(menu)}个软件,\n安装失败的软件为：{','.join(failure)}",
                 font=(', 8')).pack(fill="both", expand="yes")

    def auto_install_run(self):
        _thread.start_new_thread(self.auto_install, ())

    def change_dir(self):
        self.choose = choose_dir()
        if self.choose is None:
            self.choose = r'D:\Program Files (x86)'
        self.path.set(self.choose)

    def setup(self):
        self.button2.config(state=tk.DISABLED)  # 开始安装按钮点击一次之后就失效
        self.button2.grid(row=0, column=3, padx=3, pady=4)
        self.auto_install_run()

    def ui(self):
        self.root = tk.Tk()
        self.root.title("程序安装工具")

        self.path = tk.StringVar()  # 动态显示选择的路径
        self.path.set(self.choose)

        tk.Label(self.root, text="安装位置：").grid(row=0, column=0, padx=0, pady=4)  # 纯文字显示

        tk.Label(self.root, textvariable=self.path).grid(row=0, column=1, padx=0, pady=4)  # 显示路径的label

        tk.Button(self.root, text="更改目录", command=self.change_dir).grid(row=0, column=2, pady=4)

        self.button2 = tk.Button(self.root, text="开始安装", command=self.setup)
        self.button2.grid(row=0, column=3, padx=3, pady=4)

        self.root.mainloop()


if __name__ == '__main__':
    u = Ui()
    u.ui()
