class CircularLinkedList:

    class Node:
        def __init__(self, cargo=None, next=None):
            """ Initialises a new Node object. """
            self.__cargo = cargo
            self.__next = next

        def value(self):
            """ Returns the value of the cargo contained in this node. """
            return self.__cargo

        def next(self):
            """ Returns the next node to which this node links. """
            return self.__next

        def set_next(self, node):
            """ Sets the next node to which this node links to a new node. """
            self.__next = node

    def __init__(self):
        """ Initialises a new empty circular linked list.
        @pre:  -
        @post: A new circular linked list with no nodes has been initialised.
               The first pointer refers to None.
        """
        self.__first = None       # pointer to the first node
        self.__last = None       # pointer to the last node

    def first(self):
        """ Returns the first node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the first node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__first

    def last(self):
        """ Returns the last node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the last node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__last

    def add(self, cargo):
        """ Adds new Node with given cargo to front of this circular linked list.
        @pre:  self is a (possibly empty) CircularLinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the circular linked list.
               The head of the list now points to this new node.
               The last node now points to this new node.
        """
        node = self.Node(cargo, self.first())
        self.__first = node
        if self.last() == None:   # when this was the first element being added,
            self.__last = node     # set the last pointer to this new node
        self.last().set_next(node)

    def remove(self, cargo):
        """ Removes a node with given cargo from the circular linked list.
        @pre:  -
        @post: A node with given cargo was removed from the circular linked list.
            The removed node, with next pointer set to None, is returned.
            In case multiple nodes with this cargo exist, only one is removed.
            The list is unchanged if no such node exists or the list is empty.
            In that case, None is returned as result.
        """
        node = self.last()
        while node:
            if node.next().value() == cargo:
                to_delete = node.next()
                if to_delete == self.first():
                    self.last().set_next(to_delete.next())
                    self.__first = to_delete.next()
                elif to_delete == self.last():
                    node.set_next(self.first())
                    self.__last = node
                else:
                    node.set_next(to_delete.next())
                to_delete.set_next(None)
                return to_delete

    def removeAll(self, cargo):
        """ Removes all nodes with given cargo. """
        # Utilise autre méthode
        result = self.__first
        while result:
            result = self.remove(cargo)


def remove(self, cargo):
    """ Removes a node with given cargo from the circular linked list.
    @pre:  -
    @post: A node with given cargo was removed from the circular linked list.
        The removed node, with next pointer set to None, is returned.
        In case multiple nodes with this cargo exist, only one is removed.
        The list is unchanged if no such node exists or the list is empty.
        In that case, None is returned as result.
    """
    node = self.last()
    while node:
        if node.next().value() == cargo:
            to_delete = node.next()
            if to_delete == self.first():
                self.last().set_next(to_delete.next())
                self.__first = to_delete.next()
            elif to_delete == self.last():
                node.set_next(self.first())
                self.__last = node
            else:
                node.set_next(to_delete.next())
            to_delete.set_next(None)
            return to_delete
        node = node.next()
        if node == self.last():
            break


def removeAll(self, cargo):
    """ Removes all nodes with given cargo. """
    # Utilise autre méthode
    result = self.__first
    while result:
        result = self.remove(cargo)
