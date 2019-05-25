def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# python demo.py <arguments> __name__ 被赋值为 "__main__"
# 这意味着通过在你的模块末尾添加这些代码
# 你既可以把这个文件当作脚本又可当作一个可调入的模块来使用，
# 因为那段解析命令行的代码只有在当模块是以“main”文件的方式执行的时候才会运行
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
