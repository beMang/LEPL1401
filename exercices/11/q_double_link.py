class Node:
    def __init__(self,s, next=None, prev=None) -> None:
        self.value = s
        self.__next = next
        self.__prev = prev

    def get_text(self):
        return self.value

    def set_text(self, s):
        self.value = s

    def prev(self):
        return self.__prev

    def next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def set_prev(self, prev):
        self.__prev = prev

class Tape:
    def __init__(self) -> None:
        self.__length = 0
        self.__current = None
        self.__last = None

    def get_length(self):
        return self.__length

    def next(self):
        if self.__current and self.__current.next():
            self.__current = self.__current.next()
            return self.__current.get_text()

    def previous(self):
        if self.__current and self.__current.prev():
            self.__current = self.__current.prev()
            return self.__current.get_text()

    def add(self, s):
        if self.__last!=None and self.__current!=None:
            node = Node(s, None, self.__last)
            self.__last.set_next(node)
            self.__last = node
            self.__length+=1
        else:
            node = Node(s)
            self.__current = node
            self.__last = node
            self.__length +=1

    def write(self,s):
        if self.__current != None:
            return self.__current.set_text(s)

    def read(self):
        if self.__current != None:
            return self.__current.get_text()