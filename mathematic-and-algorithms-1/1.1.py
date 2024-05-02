def get_sequences(list):
    max_seq_num = 0
    max_seq_count = 1
    extra_count = 1

    for i in range(1, len(list) - 1):
        current_item = list[i]
        next_item = list[i + 1]

        if current_item == next_item:
            extra_count += 1

            if extra_count > max_seq_count:
                max_seq_count = extra_count
                max_seq_num = current_item

        elif current_item != next_item:
            extra_count = 1

    return max_seq_count, max_seq_num
