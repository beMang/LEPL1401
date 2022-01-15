class Client:
    """
    Un client. Chaque client a un nom d'utilisateur (supposé unique,
    par exemple adresse email) et un code pin qui est stocké comme un entier.
    """

    def __init__(self, name, pin):
        self.userName = name
        self.pin = pin

    def getUserName(self):
        return self.userName

    def getPin(self):
        return self.pin

    def setPin(self, pin):
        self.pin = pin

    def __str__(self):
        return self.userName + "(" + str(self.pin) + ")"


class ClientList:
    """Une liste de clients"""

    # un noeud de la liste
    class Node:
        def __init__(self, client, prev):
            self.data = client
            self.link = prev

    def __init__(self):
        self.last = None

    def __str__(self):
        pass

    def update(self, name, pin):
        """
        pre: name != None, la liste contient au plus un élément dont le username
             est `name`.
        post: Si un client dont le username est name est déjà présent, met à jour
              son code pin, sinon ajoute à la liste un nouveau client ayant `name`
              comme username et `pin` comme code pin.
        """
        node = self.last
        updated = False
        while node:
            if node.data.getUserName() == name:
                node.data.setPin(pin)
                updated = True
                node = node.link
            else:
                node = node.link
        if updated == False:
            client = Client(name, pin)
            node = ClientList.Node(client, self.last)
            self.last = node


# TESTS
cl = ClientList()
cl.update("alice", 1234)
cl.update("adrien", 1111)
cl.update("alice", 5965)
print(cl)                # [alice(1234)]
