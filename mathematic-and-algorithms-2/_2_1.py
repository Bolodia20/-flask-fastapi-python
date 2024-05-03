a1 = [[2, 5, 2], [1, 0, -2], [3, 1, 1]]

b1 = [[-2, 1, 0], [-2, 2, 1], [0, 0, 3]]


def dot(a, b):
    print(a)
    print(b)
    print(len(a[0]))
    print(len(b))
    print("-----")

    if len(a[0]) != len(b):
        return "error"

    mult_matrix = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b)):
            elem = 0
            for k in range(len(a)):
                elem += a[i][k] * b[k][j]

            mult_matrix[i][j] = elem

    return mult_matrix


dot(a1, b1)
