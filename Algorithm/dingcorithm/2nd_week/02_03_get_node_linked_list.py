class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(1)
# print(node.data, node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        result = ""
        while cur is not None:
            result += str(cur.data)
            if cur.next is not None :
                result += " -> "
            cur = cur.next

        print(result)

    def print_all_a1(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        while index > 0 and cur is not None:
            cur = cur.next
            index -= 1
        print(cur.data)
        return cur

    def get_node_a1(self, index):
        cur = self.head
        cur_index = 0

        while index != cur_index:
            cur = cur.next
            cur_index += 1
        print(cur.data)
        return cur


linked_list = LinkedList(5)
# print(linked_list.head.data, linked_list.head.next)

linked_list.append(12)
linked_list.append(8)
linked_list.append(39)
# linked_list.print_all()

linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.get_node_a1(4)