finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    count = 0
    for number in array:
        count += 1
        if target == number:
            print("count =", count)
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True