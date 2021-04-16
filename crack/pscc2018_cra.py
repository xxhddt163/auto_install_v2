from pywinauto import Application
from os import getcwd
from os.path import join
from time import sleep


def ps_crack():
    step = {0: ["Adobe Acrobat DC", "TsEdit", "Adobe Photoshop CC 2017", 'edit', 10],
            1: ["V7{}AcrobatCont-12-Win-GM", "TsEdit", "V7{}Photoshop-18-Win-GM", 'edit', 10],
            2: ["15.7.0", "TsEdit", "18.0.0", 'edit', 10],
            3: ["Music", "TsCheckBox", 'click', 10],
            4: ["Install", "TButton", 'click', 10],
            5: ["", "Edit", r"C:\Program Files\Adobe\Adobe Photoshop CC 2018\amtlib.dll", 'edit', 10],
            6: ["打开(&O)", "Button", 'click', 10]}

    ps_cra = Application().start(join(getcwd(), "app_pkg", 'PSCC2018', 'crack'))

    for i in range(len(step)):
        try:
            next_step = ps_cra.top_window().child_window(title=step[i][0], class_name=step[i][1]).wait('ready',
                                                                                                       timeout=step[i][
                                                                                                           -1])
        except RuntimeError:
            break
        else:
            if step[i][-2] == 'click':
                next_step.click_input()
                if i in [4, 6]:
                    sleep(1)
            elif step[i][-2] == 'edit':
                next_step.set_text(step[i][2])

    ps_cra.kill()
