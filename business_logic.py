<<<<<<< HEAD
def add_spaces(a, b):
    """将两个字符串用空格连接"""
    return a + " " + b
=======
import random

def gacha_pull(n):
    five_star = 0
    four_star = 0
    three_star = 0
    for _ in range(n):
        r = random.random()
        if r < 0.006:
            five_star += 1
        elif r < 0.056:
            four_star += 1
        else:
            three_star += 1
    return {'five_star': five_star, 'four_star': four_star, 'three_star': three_star}
>>>>>>> 95ca49b (feat: 完成AI辅助开发并添加测试用例)
