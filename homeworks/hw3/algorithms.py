# 1859034
# [1, 8, 5, 9, 0, 3, 4]
# N % 10 => utlima cifra a numarului
# (N // 10 ** 0) % 10 = 4
# (N // 10 ** 1) % 10 = 3
# (N // 10 ** 2) % 10  = 0
# ... = 0
# ... = 9
# ... !?


if __name__ == '__main__':
    n = 1859034
    digits = []
    x = 0

    while n // 10 ** x > 0:
        uc = (n // 10 ** x) % 10
        x = x + 1  # 2

        digits.append(uc)
        # n = n // 10

    print('n', n)
    # print('digits', digits[::-1])
    print('digits', digits)

# 4 * 10 ** 0 => 4 * 1 => 4
# 4 * 10 ** 1 => 4 * 10 => 40 + 3 => 43
# 43 * 10 ** 1 => 43 * 10 => 430 + ) => 430
# ...
# 4309581
