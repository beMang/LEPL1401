import turtle
import time
from Robot import Robot


class TurtleBot(Robot):

    def __init__(self, nom, x=0, y=0):
        super().__init__(nom, x, y)
        # fenêtre graphique sur laquelle le chemin du robot sera tracé;
        # le point à la position (0,0) se trouve dans le coin supérieur gauche
        self.__t = turtle.Turtle()
        self.__t.penup()
        self.__t.setpos(x, y)
        self.__t.pendown()

    def draw_from(self, old_x, old_y):
        """
        méthode auxiliaire pour tracer une ligne de l'ancienne position
        (old_x,old_y) du robot à sa position (x,y) actuelle
        """
        self.__t.goto(self.x(), self.y())

    def unplay(self):
        self.__t.color("white")
        for action in reversed(self.history()):
            if action[0] == "forward":
                self.move_backward(action[1])
            elif action[0] == "backward":
                self.move_forward(action[1])
            elif action[0] == "left":
                self.turn_right()
            elif action[0] == "right":
                self.turn_left()
            else:
                raise Exception("Historique invalide")
        super().unplay()
        self.__t.color("black")


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':

    # create robot called R2-D2 at position (100,100) and facing East,
    # to be more or less in the center of the window
    r2d2 = TurtleBot("R2-D2", 100, 100)

    print(r2d2)
    # R2-D2@(100, 100) angle: 0.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(150, 100) angle: 270.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(150.0, 50.0) angle: 180.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(100.0, 50.0) angle: 90.0
    r2d2.move_forward(50)
    print(r2d2)
    # R2-D2@(100, 100) angle: 90.0
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    print(r2d2.history())
    print(r2d2.history())
    time.sleep(2)
    r2d2.unplay()