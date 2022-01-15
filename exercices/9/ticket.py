def __init__(self):
    self.__numero = self.__class__.__prochain_numero
    self.__class__.__prochain_numero += 1
