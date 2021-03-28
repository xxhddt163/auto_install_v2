def txt_change(prom_name: str, menu_change: list) -> None:
    """
    :param menu_change: 安装文件列表
    :param prom_name: 需要删除的程序名字
    :return:
    """
    menu_change.remove(prom_name)
    with open("menu.txt", mode="w") as file:
        file.write("、".join(menu_change))
