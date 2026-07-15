def calc_total(*nums):
    """
    计算总运动量（个）
    :param nums: 每一天的运动量（可变参数）
    :return: 总运动量（个）
    """
    # nums的数据类型是元祖，sum是内置函数，可以对元组中的数据求和
    return sum(nums)


def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量（个）
    :param days: 天数（默认值是7）
    :return: 平均值
    """
    return total / days


def check_success(total, goal=120):
    """
    判断本次挑战是否成功
    :param total: 总运动量
    :param goal: 成功数量（默认值为120）
    :return: 成功或失败的具体信息
    """
    if total >= goal:
        return 'Congratulations! Challenge succeeded!'
    else:
        return 'Sorry! Challenge failed!'


def main(title, duration):
    print(f'【{title}】【{duration}】challenge (Please enter the daily quantity)')
