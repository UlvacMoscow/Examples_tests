def generate_bin(M:int, prefix=""):
    """ генерируем все числа с лидирующими незначащами нулями,
        в двоичной системе счисления
    """
    if M == 0:
        print(prefix)
        return
    generate_bin(M - 1, prefix + "0")
    generate_bin(M - 1, prefix + "1")


def generate_number(N:int, M:int, prefix = None):
    """ генерируем все числа с лидирующими незначащами нулями,
        в N-ричной системе счисления (N <= 10)
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


# для двоичной сс
generate_bin(3)

# для четырехричной сс
generate_number(4, 3)
