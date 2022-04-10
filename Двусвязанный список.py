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
        """Добавляет элемент в начало списка и делает его головой"""
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.size += 1
            self.tail = newNode
            return

        sol = self.head
        self.head = newNode
        newNode.prev = sol
        newNode.prev.next = self.head
        self.size += 1
        return

    def print(self):
        """Выводит список на экран"""
        if self.head is None:
            return
        node = self.head
        while node is not None:
            print(node.value)
            node = node.prev

    def pop_front(self):
        """Вытаскивает первый элемент списка"""
        if self.head is None:
            return False

        self.size -= 1
        val = self.head.value
        self.head = self.head.prev
        self.head.next = None
        return val

    def push_back(self, value=None):
        """Добавляет элемент в конец списка и делает его хвостом"""
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.size += 1
            self.tail = newNode
            return

        sl = self.tail
        self.tail = newNode
        newNode.next = sl
        newNode.next.prev = self.tail
        self.size += 1
        return

    def pop_back(self):
        """Вытаскивает последний элемент списка"""
        if self.head is None:
            return False

        self.size -= 1
        val = self.tail.value
        self.tail = self.tail.next
        self.tail.prev = None
        return val

    def return_by_index(self, des):
        if self.head is None:
            return None
        pr = self.size // 2
        if des > pr:
            node = self.tail
            index = self.size - 1
            while node is not None:
                if index == des:
                    return node.value
                node = node.next
                index -= 1

        node = self.head
        index = 0
        while node is not None:
            if index == des:
                return node.value
            node = node.prev
            index += 1

    def log(self):
        """Выводит список на экран"""
        if self.head is None:
            return None
        node = self.head
        while node is not None:
            print(node.next.value if node.next else node.next)
            print(node.value)
            print(node.prev.value if node.prev else node.prev)
            print()

            node = node.prev


if __name__ == "__main__":
    list1 = Flist()
    list1.push_back(2)
    list1.push_back(5)
    list1.push_back(3)
    list1.push_back(9)
    list1.push_back(1)
    list1.push_back(7)
    list1.push_back(6)
    list1.push_back(9)
    list1.push_back(12)
    list1.push_back(0)
    list1.log()

