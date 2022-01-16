class Node:
    def __init__(self, cargo, next=None) -> None:
        self.__value = cargo
        self.__next = next

    def get_next(self):
        return self.__next

    def get_value(self):
        return self.__value

    def set_next(self, next):
        self.__next = next


class LinkedList:

    def __init__(self):
        """initialise la liste chainée avec une liste déjà existante

        Args:
            lst (list): liste à chainé
        """
        self.__length = 0
        self.__head = None

    def add(self, cargo):
        if self.__length == 0:
            node = Node(cargo)
            self.__head = node
        else:
            last = self.__head
            while last.get_next():
                last = last.get_next()
            last.set_next(Node(cargo))
        self.__length += 1

    def get_reverse(self):
        l = []
        node = self.__head
        while node:
            l.append(node.get_value())
            node = node.get_next()
        l.reverse()
        s = ""
        for i in l:
            s += i
        return s


test = LinkedList()
test.add("first")
test.add("second")
test.add("third")

print(test.get_reverse())
