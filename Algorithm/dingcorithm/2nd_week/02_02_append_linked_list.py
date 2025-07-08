class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(1)
print(node.data, node.next)

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

linked_list = LinkedList(3)
print(linked_list.head.data, linked_list.head.next)

linked_list.append(12)
linked_list.append(8)
linked_list.append(39)
linked_list.print_all()
