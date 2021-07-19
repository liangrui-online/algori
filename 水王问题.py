"""
水王问题：

已知一个数组，找出其中出现次数超过半数的数
"""


def solution_naive(data):
    from collections import defaultdict

    counter = defaultdict(int)

    for item in data:
        counter[item] += 1

    target, num = None, 0
    for char, n in counter.items():
        if n > num:
            target = char
            num = n

    if num > len(data) >> 1:
        return target
    else:
        return None


def solution_naive_2(data):
    from collections import Counter

    counter = Counter(data)

    most = counter.most_common(n=1)
    target, num = most[0]

    if num > len(data) >> 1:
        return target
    else:
        return None


def solution_good(data):
    if not data:
        return None
    target = None
    num = 0
    for item in data:
        if num == 0:
            target = item
            num += 1
        elif target == item:
            num += 1
        else:
            num -= 1

    return target if num else None


def test_solution():
    import random
    import string

    # 生成序列
    target = random.choice(string.digits)
    num = random.randint(5, 50)
    data = [target] * num + [random.choice(string.digits) for i in range(num-3)]
    random.shuffle(data)

    for solution in (solution_naive, solution_naive_2, solution_good):
        assert target == solution(data)


if __name__ == '__main__':
    test_solution()
