input = "abcba"


def is_palindrome(string):
    length = len(string)-1
    for i in range(0, length):
        if length - i <= 1:
            return True
        if string[i] != string[length-i]:
            return False

    return True


def is_palindrome_a1(string):
    n = len(string)
    for i in range(n): # i: 0 ~ n-1
        if string[i] != string[n - i - 1]:
            return False
    return True


print(is_palindrome(input))
print(is_palindrome_a1(input))