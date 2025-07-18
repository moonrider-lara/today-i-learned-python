class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur = self.head
        answer = self.head
        total = 1
        while cur.next is not None:
            cur = cur.next
            total += 1

        index = total - k
        for i in range(0, index):
            answer = answer.next

        return answer

    def get_kth_node_from_last_a1(self, k):
        length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur

    # 2개의 포인터를 사용
    def get_kth_node_from_last_a2(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last_a1(2).data)
print(linked_list.get_kth_node_from_last_a2(2).data)