def find_not_repeating_first_character(string):
    for char in string:
        count = 0
        for char2 in string:
            if char == char2:
                count += 1
        if count == 1:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))



# A1. alphabet_occurrence_array 배열에 각 빈도수를 저장하고, 그 배열을 돌면서 not_repeating_character_array 라는 배열에 반복되지 않는 문자를 다 집어넣습니다.
#       그리고 다시 한 번 문자열을 돌면서 해당 문자가 발견된다면 그 값을 반환하면 됩니다.
#       이 때, 1의 빈도수를 가진 인덱스를 알파벳으로 변환해서 not_repeating_character_array 에 저장하면 됩니다.
#       그러면 not_repeating_character_array 에는 ["c", "d"]가 담기게 되는데, 그 중 첫 번째인 "c" 를 반환하면 될까요? 그렇지 않습니다.
#       입력된 문자열 내에서 반복되지 않는 첫번째 문자를 찾아서 반환해줘야 하기 때문에 string 을 다시 반복해서 돌면서 첫 번째 반복되지 않는 문자를 찾아 반환해주시면 됩니다.

def find_not_repeating_first_character_a1(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_first_character_a1
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))