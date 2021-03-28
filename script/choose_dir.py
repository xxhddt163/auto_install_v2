from wx import PySimpleApp, DirDialog, DD_DEFAULT_STYLE, DD_NEW_DIR_BUTTON, ID_OK


def choose_dir():
    """图形方式选择路径"""
    app = PySimpleApp()
    dialog = DirDialog(None, "选择安装目录", style=DD_DEFAULT_STYLE | DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == ID_OK:
        return dialog.GetPath()


if __name__ == '__main__':
    choose_dir()
