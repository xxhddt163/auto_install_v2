def format_menu(choice_list) -> list:
    """将菜单用简化名改为详细名字"""

    menu_dir = {'Wechat': '微信', 'NF3': 'Net Farmework3', '360drv': '360驱动大师', 'Chrome': '谷歌浏览器', 'TXvideo': '腾讯视频',
                'IQIYI': '爱奇艺', 'DX': 'DirectX9', '163music': '网易云音乐', 'SougouPY': '搜狗输入法', 'QQmusic': 'QQ音乐',
                'Dtalk': '钉钉', 'Kugou': '酷狗音乐', '2345explorer': '2345浏览器', '2345pinyin': '2345拼音输入法', 'WPS': 'WPS',
                'sys_cra': '系统优化', 'T20': '天正建筑T20', 'PSCS3': 'PhotoShop CS3', 'PSCC2018': 'PhotoShop CC2018',
                'OFFICE2013': 'Office 2013 Professional', 'PRCC2018': 'Premiere CC2018', 'Xunlei': '迅雷'}

    menu_temp = choice_list.copy()
    for item in menu_temp:
        if item in menu_dir:
            menu_temp[menu_temp.index(item)] = menu_dir[item]
    return menu_temp
