finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    index_min = 0
    index_max = len(array) - 1
    half = ( index_min + index_max ) // 2
    count = 0

    while index_min <= index_max:
        count += 1
        if target == array[half]:
            print("count =", count)
            return True
        if target < array[half]:
            index_max = half-1
        else:
            index_min = half+1
        half = ( index_min + index_max ) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)