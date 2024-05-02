import random


def get_list_with_generated_random_numbers(
    items_count,
    min_value,
    total_value,
):
    initial_list = [min_value] * items_count
    list_with_random_numbers = initial_list

    for i in range(items_count):
        total_values = sum(list_with_random_numbers)
        max_available_sum = total_value - total_values + min_value

        if i == items_count - 1:
            rest_count = max_available_sum
            list_with_random_numbers[i] = rest_count
            break

        random_value = random.randint(min_value, max_available_sum)
        list_with_random_numbers[i] = random_value

    return list_with_random_numbers
