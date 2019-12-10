from operation.tricks import cal_std


# 通过算数平均值判断是否需要继续去噪
def judge_improve(sketch):
    std = cal_std(sketch)
    if std > 100:
        return True
    else:
        return False
