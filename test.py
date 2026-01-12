def generate_fibonacci(n):
    """
    生成斐波那契数列的前n项

    参数:
    n (int): 要生成的斐波那契数列项数

    返回:
    list: 包含前n项斐波那契数的列表
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


def print_fibonacci_sequence(n):
    """
    打印斐波那契数列的前n项

    参数:
    n (int): 要打印的斐波那契数列项数
    """
    sequence = generate_fibonacci(n)

    if not sequence:
        print("请输入大于0的整数")
    else:
        print(f"斐波那契数列的前{n}项:")
        for i, num in enumerate(sequence, 1):
            print(f"第{i}项: {num}")

        # 计算并显示一些统计数据
        if len(sequence) >= 2:
            ratio = sequence[-1] / sequence[-2] if sequence[-2] != 0 else 0
            print(f"\n最后两项的比值: {ratio:.6f}")
            print(f"数列总和: {sum(sequence)}")


# 示例使用
if __name__ == "__main__":
    try:
        n = int(input("请输入要生成的斐波那契数列项数: "))
        print_fibonacci_sequence(n)
    except ValueError:
        print("输入错误：请输入一个整数")