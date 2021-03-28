from datetime import datetime


def running_time(start, end):
    """计算程序运行多少时间"""
    start = datetime.strptime(start, "%H:%M")  # 将字符串格式的开始时间实例化为datetime对象
    end = datetime.strptime(end, "%H:%M")
    return int((end - start).seconds / 60)  # 计算结束时间与开始时间之间相差多少秒并将秒换算成分钟
