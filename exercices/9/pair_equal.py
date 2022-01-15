def __eq__(self, p):
    if not p:
        return False
    return self.a == p.a and self.b == p.b
