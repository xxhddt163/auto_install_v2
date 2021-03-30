import tkinter as tk
from script.choose_dir import choose_dir
from auto_install import auto_install


class Ui:
    def __init__(self):
        self.choose = r'D:\Program Files (x86)'  # 安装目录

    def change_dir(self):
        self.choose = choose_dir()
        if self.choose is None:
            self.choose = r'D:\Program Files (x86)'
        self.path.set(self.choose)

    def setup(self):
        auto_install(self.choose)

    def ui(self):
        root = tk.Tk()
        root.title("程序安装工具")

        self.path = tk.StringVar()  # 动态显示选择的路径
        self.path.set(self.choose)

        labelframe1 = tk.LabelFrame(root, text=f'安装进度（第    个，共    个）', height=80, width=300)  # 信息区
        labelframe1.grid(row=1, column=0, columnspan=10, padx=10, pady=10)
        labelframe1.propagate(0)  # 使组件大小不变，此时width才起作用
        tk.Label(labelframe1, text=f"", font=(', 15')).pack(fill="both", expand="yes")

        tk.Label(root, text="安装位置：").grid(row=0, column=0, padx=0, pady=4)  # 纯文字显示

        tk.Label(root, textvariable=self.path).grid(row=0, column=1, padx=0, pady=4)  # 显示路径的label

        tk.Button(root, text="更改目录", command=self.change_dir).grid(row=0, column=2, pady=4)

        tk.Button(root, text="开始安装", command=self.setup).grid(row=0, column=3, padx=3, pady=4)

        root.mainloop()


if __name__ == '__main__':
    u = Ui()
    u.ui()
