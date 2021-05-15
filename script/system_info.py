import platform


def system_info() -> str:
    """ 返回目标windows系统的版本
    :return: 7 or 10
    """
    return platform.uname().release
