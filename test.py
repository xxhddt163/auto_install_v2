from wx import PySimpleApp, DirDialog, DD_DEFAULT_STYLE, DD_NEW_DIR_BUTTON, ID_OK
from os import mkdir, remove, walk, rename
from os.path import join
from easygui import msgbox, multchoicebox, enterbox
from shutil import copy
from pyperclip import copy as copy_path
from time import sleep
from pyautogui import hotkey
import requests

configfile_template = r'''#api-addr: :1501
block-hash: ""
block-time: "15"
bootnode: []
bootnode-mode: false
cache-capacity: "6000000"
clef-signer-enable: false
clef-signer-endpoint: ""
clef-signer-ethereum-address: ""
config: ""
cors-allowed-origins: []
#data-dir: beedata
db-block-cache-capacity: "33554432"
db-disable-seeks-compaction: false
db-open-files-limit: "1048576"
db-write-buffer-size: "33554432"
#debug-api-addr: :1601
debug-api-enable: true
full-node: true
gateway-mode: false
global-pinning-enable: true
help: false
mainnet: true
nat-addr: ""
network-id: "1"
#p2p-addr: :1701
p2p-quic-enable: false
p2p-ws-enable: false
password: "bzz@gogo"
password-file: ""
payment-early: "10000000"
payment-threshold: "100000000"
payment-tolerance: "100000000"
postage-stamp-address: ""
price-oracle-address: ""
resolver-options: []
standalone: false
swap-deployment-gas-price: ""
swap-enable: true
swap-endpoint: http://124.232.149.231:8545
swap-factory-address: ""
swap-initial-deposit: "0"
swap-legacy-factory-addresses: []
tracing-enable: false
tracing-endpoint: 127.0.0.1:6831
tracing-service-name: bee1533
transaction: ""
verbosity: "5"
warmup-time: 20m0s
welcome-message: "beefrey-Team"
'''


def choose_dir():
    """图形方式选择路径"""
    app = PySimpleApp()
    msgbox("请选择安装目录")
    dialog = DirDialog(None, "选择安装目录", style=DD_DEFAULT_STYLE | DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == ID_OK:
        return dialog.GetPath()


def create_dir():
    """创建目录"""
    for _ in range(10001, 10001 + dir_number):
        dir_name = join(dir_path, 'bee' + str(_))
        mkdir(dir_name)
        for __ in ["bee.exe", "beeconfig.yaml", "start.bat"]:
            copy_file(dest_dir=dir_name, file_name=__)
        mkdir(join(dir_name, "keys"))
        for __ in ["swarm.key", "pss.key", "libp2p.key"]:
            copy_file(dest_dir=join(dir_name, "keys"), file_name=__)
    remove_file()


def download_file():
    """下载文件相关"""
    for __ in ["http://124.232.149.231:520/bzzv1/bee.exe",
               "http://124.232.149.231:520/bzzv1/beeconfig.yaml",
               "http://124.232.149.231:520/bzzv1/swarm.key",
               "http://124.232.149.231:520/bzzv1/pss.key",
               "http://124.232.149.231:520/bzzv1/libp2p.key"
               ]:
        r = requests.get(__)
        with open(join(dir_path, __.split('/')[-1]), "wb") as f:
            f.write(r.content)
    with open(join(dir_path, "start.bat"), 'w') as f:
        f.writelines("bee.exe start --config beeconfig.yaml")


def copy_file(dest_dir, file_name):
    """将下载的文件复制到指定目录"""
    copy(join(dir_path, file_name), dest_dir)


def remove_file():
    """删除缓存文件"""
    for _ in ["bee.exe",
              "beeconfig.yaml",
              "swarm.key",
              "pss.key",
              "libp2p.key",
              "start.bat"
              ]:
        remove(join(dir_path, _))


def run_program():
    """遍历目录执行所有的bat文件"""
    if "Yes" in run:
        wait_time = int(enterbox("输入等待的时间（秒）：", "启动间隔时间"))
        for root_dir, dir_list, file_list in walk(dir_path):
            if "start.bat" in file_list:
                copy_path(join(root_dir, "start.bat"))
                hotkey('win', 'r')
                hotkey('ctrl', 'v')
                hotkey('enter')
                sleep(wait_time)


def alter(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line.replace(old_str, new_str))
    remove(file)
    rename("%s.bak" % file, file)


def change_yaml():
    n = 1
    for root_dir, dir_list, file_list in walk(dir_path):
        if "beeconfig.yaml" in file_list:
            with open(join(root_dir, "beeconfig.yaml"), 'w') as f:
                f.write(configfile_template)
            alter(join(root_dir, "beeconfig.yaml"), "#api-addr: :1501", "api-addr: :%s" % str(1500 + n))
            alter(join(root_dir, "beeconfig.yaml"), "#data-dir: beedata", f"data-dir: {root_dir}")
            alter(join(root_dir, "beeconfig.yaml"), "#debug-api-addr: :1601", f"debug-api-addr: :{str(1600 + n)}")
            alter(join(root_dir, "beeconfig.yaml"), "#p2p-addr: :1701", f"p2p-addr: :{str(1700 + n)}")
            n += 1


if __name__ == '__main__':
    dir_path = choose_dir()
    dir_number = int(enterbox("请输入创建目录的个数", "请输入创建文件的个数"))
    run = multchoicebox('是否执行程序？', '', ['Yes', 'No'])
    download_file()
    create_dir()
    change_yaml()
    run_program()
