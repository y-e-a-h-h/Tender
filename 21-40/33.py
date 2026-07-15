# 函数的说明文档
m = float(input('m= '))
n = float(input('n= '))


def add(m, n):
    """
    计算两个数相加的结果
    :param m: 第一个数
    :param n: 第二个数
    :return: 二者相加的结果
    """
    answer = m + n
    return answer


result = add(m, n)
print(result)
