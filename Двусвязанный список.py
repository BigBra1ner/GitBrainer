class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Flist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value=None):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.size += 1
            self.tail = newNode
            return
        else:
            sol = self.head
            self.head = newNode
            newNode.prev = sol
            self.size += 1
            return

    def print(self):
        if self.head is None:
            return

        node = self.head
        while node is not None:
            print(node.value)
            node = node.prev


if __name__ == "__main__":

    list1 = Flist()
    list1.push_front(2)
    list1.push_front(5)
    list1.push_front(3)
    list1.push_front(9)
    list1.print()
