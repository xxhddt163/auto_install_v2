from os.path import join
from os import getcwd
from os import system


def cad2007_cra(install_dir: str):
    """
    激活天正T20
    :param install_dir: 选择的安装目录
    :return:
    """
    file_name = ["adlmdll.dll", "lacadp.dll"]
    for each in file_name:
        crack_path = join(getcwd(), "app_pkg", "CAD2007", "crack", each)
        target_path = join(install_dir, "CAD2007", each)
        system(f'xcopy "{crack_path}" "{target_path}" /Y')
