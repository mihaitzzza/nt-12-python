def my_sum(a, b):
    return a + b


def my_sum_from_all_args(*args, **kwargs):
    s = 0
    print('args', args)
    print('kwargs', kwargs)

    for i in args:
        # print('--- inside function i:', i)
        if type(i) in [int, float]:
            s += i

    return s


def do_something(a, b, c, e, f):
    r = 0

    if a % 2 == 0:
        r = b + c
    elif b % 2 == 0:
        r = c + e
    else:
        r = a + b + c + e + f

    return r
