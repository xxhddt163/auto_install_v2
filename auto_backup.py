import os
import zipfile
import time
from getpass import getuser

username = getuser()  # 当前用户名
print(fr"当前用户名为{username},游戏存档目录为C:\Users\{username}\Zomboid\Saves")

def check_dir():  # 目录检查
    print("正在检查存档备份目录......")
    os.chdir(fr'C:\Users\{username}\Zomboid')
    if 'Saves_back' not in os.listdir(os.getcwd()):  # 检查Saves_back文件夹是否创建
        print(fr"存档文件夹C:\Users\{username}\Zomboid\Saves_back不存在，将自动创建")
        os.mkdir(os.path.join(os.getcwd(), 'Saves_back'))  # 没有创建就创建该文件夹
    else:
        print(fr"存档文件夹C:\Users\{username}\Zomboid\Saves_back已存在")


def zip():
    print("正在备份存档......")
    os.chdir(fr'C:\Users\{username}\Zomboid')
    file_name = time.strftime('%Y%m%d%H%M') + '.zip'
    f = zipfile.ZipFile(os.path.join(fr'C:\Users\{username}\Zomboid', 'Saves_back', file_name), 'w')
    for root_dir, dir_list, file_list in os.walk(os.path.join(os.getcwd(), 'Saves')):
        for name in file_list:
            target_file = os.path.join(root_dir, name)
            f.write(target_file, target_file, zipfile.ZIP_DEFLATED)

    f.close()
    print("存档备份完毕，5分钟后将再次备份")


def check_files():  # 文件检查
    print("正在检查存档文件个数......")
    os.chdir(fr'C:\Users\{username}\Zomboid\Saves_back')
    print(f"正在备份存档，当前一共有{len(os.listdir(os.getcwd()))}个存档")
    while True:
        if len(os.listdir(os.getcwd())) < 10:
            break
        target_file = os.listdir(os.getcwd())[0]
        os.remove(os.path.join(fr'C:\Users\{username}\Zomboid\Saves_back', target_file))


def main():
    while True:
        check_dir()
        check_files()
        zip()
        time.sleep(300)


if __name__ == '__main__':
    main()
