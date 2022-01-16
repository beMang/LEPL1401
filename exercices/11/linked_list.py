class LinkedList:
    def __init__(self, lst):
        """initialise la liste chainée avec une liste déjà existante

        Args:
            lst (list): liste à chainé
        """
        self.__length = 0
        self.__head = None

        for i in range(len(lst)-1, -1, -1):
            self.add(lst[i])

    def remove(self):
        if self.__head != None:
            self.__head = self.__head.next()
            self.__length -= 1

    def insert(self, s):
        """
        @pre  s est un string à insérer dans la liste chainée;
            self est une liste chaînée dont les noeuds contiennent des strings;
            les noeuds de la liste sont ordonnées en ordre croissant selon les valeurs (strings)
            qu'ils contiennent.
        @post Un noeud contenant le String s a été inséré dans la liste de façon
            à ce qu'après l'insertion celle-ci soit toujours en ordre croissant.
        """
        if self.__head == None:
            self.__head = Node(s)
        elif s < self.__head.value():
            node = Node(s, self.__head)
            self.__head = node
            self.__length += 1
        else:
            node = self.__head
            while node:
                if node.next() == None:
                    if s > node.value():
                        node.set_next(Node(s))
                        self.__length += 1
                        break
                elif node.value() <= s <= node.next().value():
                    n = Node(s, node.next())
                    node.set_next(n)
                    self.__length += 1
                    break
                node = node.next()

    def __str__(self) -> str:
        s = "[ "
        tail = self.__head
        while tail:
            s += str(tail.value()) + " "
            tail = tail.next()
        s += "]"
        return s

    def remove_from_end(self):
        if self.__head:
            if self.__length == 1:
                self.__head = None
            else:
                before_last = self.__head
                while before_last.next() and before_last.next().next():
                    before_last = before_last.next()
                before_last.set_next(None)
            self.__length -=1
