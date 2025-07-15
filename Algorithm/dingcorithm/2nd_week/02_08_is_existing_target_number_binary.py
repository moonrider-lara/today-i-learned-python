finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    index_min = 0
    index_max = len(array)-1
    half = (index_min + index_max) // 2
    count = 0

    while index_min <= index_max:
        count += 1
        if array[half] == target:
            print("count =", count)
            return True
        if array[half] < target:
            index_min = half+1
        else:
            index_max = half-1
        half = (index_min + index_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)