shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not binary_search(menus, order):
            return False
    return True

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

#   이 문제는 단순히 특정한 문자열이 배열에 존재하는지만 확인하면 됩니다.
#   정렬을 할 필요없이, 집합 자료형을 사용하면 쉽게 해결할 수 있습니다.
#   * 집합은 중복을 허용하지 않는 자료형입니다.
def is_available_to_order_a1(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True



result = is_available_to_order(shop_menus, shop_orders)
print(result)

result = is_available_to_order_a1(shop_menus, shop_orders)
print(result)
