from math import pi, cos, sin


class Robot:

    def __init__(self, nom, x=0, y=0):
        # nom du robot
        self.__nom = nom
        # position du robot
        self.__x = x               # position x du robot
        self.__y = y               # position y du robot
        # angle en degres radius représentant la direction du robot
        self.__angle = 0
        self.__history = []

    def __str__(self):
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return str(self.nom()) + "@(" + str(round(self.x())) + "," + \
            str(round(self.y())) + ") angle: "+str(self.angle())

    def nom(self):
        return self.__nom

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def angle(self):
        "retourne l'angle en degres représentant la direction du robot"
        return self.__angle % 360

    def __set_x(self, x):
        self.__x = x

    def __set_y(self, y):
        self.__y = y

    def __set_angle(self, angle):
        self.__angle += angle

    def position(self):
        return (self.x(), self.y())

    def history(self):
        return self.__history

    def __move(self, distance, sense):
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  fait avancer le robot de distance pixels
            si sense = -1 fait reculer le robot de distance pixels
        """
        old_x = self.x()
        old_y = self.y()
        orientation_x = cos(self.angle()*pi/180)
        orientation_y = sin(self.angle()*pi/180)
        self.__set_x(old_x + orientation_x * distance * sense)
        self.__set_y(old_y + orientation_y * distance * sense)
        self.draw_from(old_x, old_y)

    def move_forward(self, distance):
        """ fait avancer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance, 1)
        self.__history.append(("forward", distance))

    def move_backward(self, distance):
        """ fait reculer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance, -1)
        self.__history.append(("backward", distance))

    def __turn(self, direction):
        """ méthode auxiliaire pour les méthodes turn_right() et turn_left()
            si direction = 1 change l'angle du robot de 90 degrés vers la droite
                             (dans le sens des aiguilles d'une montre)
            si direction = -1 change l'angle du robot de 90 degrés vers la gauche
                             (dans le sens contraire des aiguilles d'une montre)
        """
        if direction == 1:
            self.__set_angle(-90)
        if direction == -1:
            self.__set_angle(90)

    def turn_right(self):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__turn(1)
        self.__history.append(("right", 90))

    def turn_left(self):
        """ fait tourner le robot de 90 degrés vers la gauche
            (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(-1)
        self.__history.append(("left", 90))

    def unplay(self):
        self.__history = []
