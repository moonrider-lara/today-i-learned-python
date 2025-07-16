numbers = [1, 1, 1, 1, 1]
target_number = 3

# numbers = [2, 3, 1]
# target_number = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    result = []
    answer = 0

    def get_all_ways_to_target_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            result.append(current_sum)
            return
        get_all_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_to_target_by_doing_plus_or_minus(array, 0, 0)

    for num in result:
        if num == target:
            answer += 1

    return answer


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!