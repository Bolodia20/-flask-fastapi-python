from _2_1 import dot
import math
import matplotlib.pyplot as plt


def get_vector_length(vector):
    sum = 0
    for i in vector[0]:
        sum += pow(i, 2)

    return math.sqrt(sum)


def angle_between_vectors(a, b):
    product_of_numbers = 0

    for i in range(len(a[0])):
        product_of_numbers += a[0][i] * b[0][i]

    vector_a = get_vector_length(a)
    vector_b = get_vector_length(b)

    cosine = (product_of_numbers) / (vector_a * vector_b)
    alpha = math.acos(cosine)
    alpha_degrees = math.degrees(alpha)

    return alpha_degrees


a = [[1, 1]]
b = [[-2, 2]]
c = [[1.8, -0.5]]


theta_ab = angle_between_vectors(a, b)
print("Angle between vectors a and b:", theta_ab, "degrees")

theta_bc = angle_between_vectors(b, c)
print("Angle between vectors b and c:", theta_bc, "degrees")

theta_ca = angle_between_vectors(c, a)
print("Angle between vectors c and a:", theta_ca, "degrees")

vectors = [[1, 1], [-2, 2], [1.8, -0.5]]

g = [[0.7, -0.7], [0.7, 0.7]]
g_vectors = dot(a, g)


def get_linear_matrix(vectors, matrix):
    res = []
    for i in vectors:
        res.append(dot([i], matrix))

    return res


res_g = get_linear_matrix(vectors, g)
