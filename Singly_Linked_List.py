class Node:
    def __init__(self, data):
        self.head = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.head)
            temp = temp.next

    def push_front(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def insert_node(self, prev_node, new_data):
        new_node = Node(new_data)

        if prev_node is None:
            print("The given previous node must be in linked linked")
            return

        new_node.next = prev_node.next

        prev_node.next = new_node



if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third



    llist.insert_node(llist.head.next, 8)

    llist.printlist()