def fib(n):  # write Fibonacci series up to n
    # """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()


def fib2(n):
    # Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    else:
        return result


def ask_ok(prompt, retries=4, reminder='please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        elif ok in ('n', 'no', 'nop', 'nope'):
            return False
        else:
            retries = retries - 1
            if retries < 0:
                raise ValueError("invalid user response")
        print(reminder)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind, *name, **dic):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for a in name:
        print(a)
    for k in dic:
        print(k, dic[k])


def contact(*args, sep="#"):
    return sep.join(args)


def make_incrementor(n):
    return lambda x: x + n


def lambda_test():
    pairs = [(1, 'aa', 6), (3, 'ec', 9), (2, 'bc', 8), (4, 'dd', 7)]
    # 按下标所在对象排序
    pairs.sort(key=lambda a: a[2])
    print(pairs)


# fib(3000)
# f = fib
# print(fib2(500000))
# ask_ok("Do you really want to quit?")
# parrot(5, type="gggg")
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
# print(contact("a", "c", "b", sep="&"))
# print(list(range(3, 10)))
# args = [10, 20]
# print(list(range(*args)))
# f = make_incrementor(60)
# print(f(42))
# lambda_test()
