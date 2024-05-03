from _2_1 import dot
import math


def vector_length(v):
    return math.sqrt(sum([x**2 for x in v]))


def angle_between_vectors(a, b):
    dot_product = dot(a, b)
    length_a = vector_length(a[0])
    length_b = vector_length(b[0])
    print("dot_product", dot_product)
    print("length_a", length_a)
    print("length_b", length_b)

    cos_theta = dot_product / (length_a * length_b)
    if cos_theta > 1:
        cos_theta = 1
    elif cos_theta < -1:
        cos_theta = -1
    theta = math.acos(cos_theta)
    return math.degrees(theta)


a = [[1, 1]]
b = [[-2, 2]]
c = [[1.8, -0.5]]

theta_ab = angle_between_vectors(a, b)
print("Angle between vectors a and b:", theta_ab, "degrees")

theta_bc = angle_between_vectors(b, c)
print("Angle between vectors b and c:", theta_bc, "degrees")

theta_ca = angle_between_vectors(c, a)
print("Angle between vectors c and a:", theta_ca, "degrees")
