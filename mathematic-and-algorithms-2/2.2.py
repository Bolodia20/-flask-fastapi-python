def dec2bin_list(n):
    assert type(n) == int, f"""n is not integer"""
    assert n >= 0, f"""n is can't be negative"""
    if n == 0:
        return [0]

    bin_list = []

    i = n

    while i != 0:
        remainder = i % 2
        bin_list.insert(0, remainder)
        i = int(i / 2)

    return bin_list


print(dec2bin_list(675))
