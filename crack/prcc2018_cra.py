from pywinauto import Application
from os import getcwd
from os.path import join
from time import sleep


def pr_crack():
    step = {0: ["Adobe Acrobat DC", "TsEdit", "Adobe Prelude CC 2015", 'edit', 10],
            1: ["V7{}AcrobatCont-12-Win-GM", "TsEdit", "V7{}Prelude-4-Win-GM", 'edit', 10],
            2: ["15.7.0", "TsEdit", "4.0.0", 'edit', 10],
            3: ["Install", "TButton", 'click', 10],
            4: ["", "Edit", r"C:\Program Files\Adobe\Adobe Premiere Pro CC 2018\amtlib.dll", 'edit', 10],
            5: ["打开(&O)", "Button", 'click', 10]}

    pr_cra = Application().start(join(getcwd(), "app_pkg", 'PRCC2018', 'crack'))
    for i in range(len(step)):
        next_step = pr_cra.top_window().child_window(title=step[i][0], class_name=step[i][1]).wait('ready',
                                                                                                   timeout=step[i][-1])
        if step[i][-2] == 'click':
            next_step.click_input()
            if i == 3 or i == 5:
                sleep(1)
        elif step[i][-2] == 'edit':
            next_step.set_text(step[i][2])
    pr_cra.kill()
