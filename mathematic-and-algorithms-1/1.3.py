def find_index_of_minimum(vector, start=0):
    minimum, index_of_minimum = vector[start], start
    for index, value in enumerate(vector[start + 1 :]):
        if value < minimum:
            minimum = value
            index_of_minimum = index + start + 1
    return index_of_minimum


a = [81, 44, 91, 23, 26, 42, 46, 19, 46]


def selection_sort(list):
    sorted_list = list

    for i in range(len(sorted_list)):
        min_value_index = find_index_of_minimum(sorted_list, i)
        min_value = sorted_list[min_value_index]
        current_value = sorted_list[i]
        sorted_list[i] = min_value
        sorted_list[min_value_index] = current_value

    return sorted_list


selection_sort(a)
