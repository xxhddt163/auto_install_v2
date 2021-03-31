import zipfile
from easygui import diropenbox, multchoicebox
from os.path import join


def unzip(choose):
    """
    解压制定软件安装包到指定目录
    :param choose: 选择安装的文件菜单
    :return: 软件解压目录
    """
    extract_dir = diropenbox("选择解压文件保存的位置")
    zip_file = zipfile.ZipFile("auto_install.zip", "r")
    for program in choose:
        for name in zip_file.namelist():
            if program in name:
                zip_file.extract(name, extract_dir)
                print(f"正在将文件{name}解压到{extract_dir}")
    zip_file.extract('auto_install.exe', extract_dir)
    zip_file.extract('set.bat', extract_dir)
    zip_file.close()
    return extract_dir


def menu_to_file(path, choose):
    """
    将选择的文件转换成文件
    :param choose: 选择的软件
    :param path: 文件保存路径
    :return: None
    """
    with open(join(path, "menu.txt"), "w") as menu_file:
        if 'sys_cra' not in choose:
            menu_file.write("、".join(choose))
        else:
            choose.remove('sys_cra')
            menu_file.write("、".join(choose))


def menu_format(choice_list):
    """将中文选单格式为菜单简写名"""

    menu_dir = {"微信": "Wechat",
                "Net Farmework3": "NF3",
                "360驱动大师": "360drv",
                "谷歌浏览器": "Chrome",
                "腾讯视频": "TXvideo",
                "爱奇艺(推荐)": "IQIYI",
                "DirectX9": "DX",
                "网易云音乐": "163music",
                "搜狗输入法": "SougouPY",
                "QQ音乐": "QQmusic",
                "钉钉": "Dtalk",
                "酷狗音乐(推荐)": "Kugou",
                "2345浏览器(推荐)": "2345explorer",
                "2345拼音输入法(推荐)": "2345pinyin",
                "WPS(推荐)": "WPS",
                "系统优化": "sys_cra",
                "天正建筑T20": "T20",
                "PhotoShop CS3": "PSCS3",
                "PhotoShop CC2018": "PSCC2018",
                "Office 2013 Professional": "OFFICE2013",
                "Premiere CC2018": "PRCC2018"
                }

    menu_temp = choice_list.copy()
    for item in menu_temp:
        if item in menu_dir:
            menu_temp[menu_temp.index(item)] = menu_dir[item]
    return menu_temp


if __name__ == '__main__':
    choice = multchoicebox(msg="请选择安装的程序", title="选择程序",
                           choices=["系统优化", "QQ", "微信", "钉钉", "Winrar", "VCRedist", "Net Farmework3", "DirectX9",
                                    "Office 2013 Professional", "WPS(推荐)", "360驱动大师", "谷歌浏览器", "2345浏览器(推荐)", "腾讯视频",
                                    "爱奇艺(推荐)", "PhotoShop CS3", "PhotoShop CC2018", "Premiere CC2018", "网易云音乐", "QQ音乐",
                                    "酷狗音乐(推荐)",
                                    "搜狗输入法", "2345拼音输入法(推荐)", "3DMAX2014", "CAD2014", "CAD2007", "天正建筑T20"])
    menu = menu_format(choice)
    ex_dir = unzip(menu)
    menu_to_file(ex_dir, menu)
