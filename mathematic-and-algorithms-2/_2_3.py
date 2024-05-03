from _2_1 import dot


def power(matrix, n):
    result = [[1, 0], [0, 1]]

    while n > 0:
        if n % 2 == 1:
            result = dot(result, matrix)
        matrix = dot(matrix, matrix)
        n //= 2
    return result


def log_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = [[0, 1], [1, 1]]
        result_matrix = power(matrix, n - 1)
        return result_matrix[1][1]


def recursion_fib(n):
    if n <= 1:
        return n
    else:
        return recursion_fib(n - 1) + recursion_fib(n - 2)


def linear_fib(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
    return a


(log_fib(6))
(linear_fib(6))
(recursion_fib(6))
