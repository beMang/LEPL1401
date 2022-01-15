from cmath import inf


class Student:
    def __init__(self, firstname, surname, mark):
        """
        @pre:  firstname et surname sont des str et mark est un int
        @post: crée une instance de Student avec ces trois attributs
        """
        self.firstname = firstname
        self.surname = surname
        self.mark = mark

def marks_from_file(filename):
    with open(filename, "r") as f:
        l = []
        for line in f.readlines():
            info = line.split()
            student = Student(info[0], info[1], int(info[2]))
            l.append(student)
        return l