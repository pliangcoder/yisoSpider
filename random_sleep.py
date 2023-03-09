import time
import random


def random_sleep(*_time):
    try:
        size = len(_time)
        if size == 2:
            if _time[0] > _time[1]:
                time.sleep((_time[0] + _time[1]) / 2)
            else:
                pan_duan = isinstance(_time[0], int)  # 判断是不是int类型
                pan_duan2 = isinstance(_time[0], float)
                pan_duan3 = isinstance(_time[1], int)
                pan_duan4 = isinstance(_time[1], float)
                if pan_duan and pan_duan3:  # 两个都是int 类型才执行这句话
                    time.sleep(random.randint(_time[0], _time[1]))
                elif pan_duan2 or pan_duan4:  # 两个一个（float类型）是真就执行这句话
                    time.sleep(random.uniform(_time[0], _time[1]))
        elif size == 1:
            pan_duan = isinstance(_time[0], int)  # 判断是不是int类型
            pan_duan2 = isinstance(_time[0], float)
            if pan_duan:  # 是int 类型才执行这句话
                time.sleep(random.randint(0, _time[0]))
            elif pan_duan2:  # （float类型）是真就执行这句话
                time.sleep(random.uniform(0, _time[0]))
        elif size == 0:  # 不填参数睡眠一秒
            time.sleep(1)
        else:  # 大于三个数,只要前两个
            pan_duan = isinstance(_time[0], int)  # 判断是不是int类型
            pan_duan2 = isinstance(_time[0], float)
            pan_duan3 = isinstance(_time[1], int)
            pan_duan4 = isinstance(_time[1], float)
            if pan_duan and pan_duan3:  # 两个都是int 类型才执行这句话
                time.sleep(random.randint(_time[0], _time[1]))
            elif pan_duan2 or pan_duan4:  # 两个一个（float类型）是真就执行这句话
                time.sleep(random.uniform(_time[0], _time[1]))
    except:
        raise "input error type"
