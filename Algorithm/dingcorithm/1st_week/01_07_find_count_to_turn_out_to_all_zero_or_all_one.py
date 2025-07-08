input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    initial_val_0 = initial_val_1 = 0

    if string[0] == '0':
        initial_val_0 += 1
    else:
        initial_val_1 += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                initial_val_0 += 1
            else:
                initial_val_1 += 1

    return min(initial_val_0, initial_val_1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)


# A1.   1) 값이 뒤집어 질 경우
#       2) 첫 번째 원소가 0인지 1인지
#       에 대해서 계산하면, 모두 0으로 만드는 횟수와 모두 1로 만드는 횟수를 만들 수 있습니다.
#       그리고 0으로 만드는 횟수와 모두 1로 만드는 횟수 둘 중 최솟값을 반환해주면 됩니다.

def find_count_to_turn_out_to_all_zero_or_all_one_a1(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one_a1(input)
print(result)