import time


def partition(sort_list, start, end):
    i = start
    pivot = sort_list[end]
    for j in range(start, end):
        if sort_list[j] < pivot:
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
            i += 1
    sort_list[i], sort_list[end] = sort_list[end], sort_list[i]
    return i


def qsort(sort_list, start, end):
    if start < end:
        pivot = partition(sort_list, start, end)
        qsort(sort_list, start, pivot - 1)
        qsort(sort_list, pivot + 1, end)


def median(list):
    middle_item_index = len(list) // 2

    if len(list) % 2 == 1:
        return list[middle_item_index]

    return (list[middle_item_index] + list[middle_item_index - 1]) / 2


a = [81, 44, 91, 23, 26, 21, 42, 46, 19, 46]
qsort(a, 0, len(a) - 1)
print(f"\n{a}")

start_time = time.time()
sorted_list = qsort(a, 0, len(a) - 1)
print("sorted_list", sorted_list)
end_time = time.time()

print("median", median(a))

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
