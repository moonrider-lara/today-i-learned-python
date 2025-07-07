input = 20


def find_prime_list_under_number(number):
    answer = []
    for num in range(2, number + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            answer.append(num)

    return answer


result = find_prime_list_under_number(input)
print(result)



# A1. 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라, 2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보도록 개선해봅시다.
#   주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
#   수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문입니다.
#   이를 이용해서 i * i ≤ n 일 때까지만 비교하시면 됩니다.

def find_prime_list_under_number_a1(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if i * i <= n and n % i == 0: # N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number_a1(input)
print(result)