# Réalisé par Adrien Antonutti et Joséphine Civilio
import turtle                # module des graphiques tortue

win = turtle.Screen()  # initialise la fenêtre
win.title("Drapeaux")
win.bgcolor("#a3a3a3")
margin = 20  # marges pour la fenêtre
t = turtle.Turtle()  # créer une nouvelle tortue
t.hideturtle()
t.speed("fastest")
t.penup()
t.goto(t.shapesize()[1]/2 - win.window_width()/2 + margin,
       win.window_height()/2 - t.shapesize()[0]/2 - margin)  # On met la tortue en haut à gauche (en fonction de l'écran)


def rectangle(w, h, color):  # Dessine un rectangle
    t.color(color)
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:  # Pour modifier la distance parcourue une fois sur 2
            t.forward(w)
        else:
            t.forward(h)
        t.right(90)
    t.end_fill()


# Dessine un drapeau horizontal ou vertical en fonction des arguments
def three_color_flag(w, *args):
    if args[0] == "horizontal":
        height = ((w/3)*2)/3
        for i in range(3):
            rectangle(w, height, args[i+1])
            t.right(90)
            t.forward(height)
            t.left(90)
        t.left(90)
        t.forward(height*3)
        t.right(90)
    elif args[0] == "vertical":
        height = (w/3)*2
        for i in range(3):
            rectangle(w/3, height, args[i+1])
            t.forward(w/3)
        t.backward(w)
    else:
        print("Erreur, drapeau soit vertical soit horizontal")


def star(size, color):  # Dessine une étoile (à 5 branches)
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()
    for side in range(5):
        t.forward(size*0.725)
        t.right(144)
        t.forward(size*0.725)
        t.left(72)
    t.end_fill()


def european_flag(size):
    w = size
    h = size/3*2
    rectangle(w, h, "#003399")
    t.forward(w/2)
    t.right(90)
    t.forward(h/2)
    t.left(90)
    for i in range(0, 12):
        t.right(i*30)  # On se décale d'un certain angle
        t.forward(h/3)
        t.left(i*30)  # Pour que l'étoile soit droite
        star(h/18, "#FFCC00")
        t.right(i*30)
        t.backward(h/3)  # On revient au centre du cercle d'étoile
        t.left(30*i)


def belgian_flag(size):
    three_color_flag(size, "vertical", "#000000", "#FDDA24", "#EF3340")


def french_flag(size):
    three_color_flag(size, "vertical", "#0055A4", "#FFFFFF", "#EF4135")


def dutch_flags(size):
    three_color_flag(size, "horizontal", "#AE1C28", "white", "#21468B")


def german_flags(size):
    three_color_flag(size, "horizontal", "black", "#DD0000", "#FFCE00")


# Dessin général
small_flags_size = 200  # Pour définir la taille d'un drapeau
ecart = 0.2  # Pour régler l'écart entre les drapeaux

# 4 premiers drapeaux
belgian_flag(small_flags_size)
t.forward((1+ecart)*small_flags_size)
dutch_flags(small_flags_size)
t.forward((1+ecart)*small_flags_size)
french_flag(small_flags_size)
t.forward((1+ecart)*small_flags_size)
german_flags(small_flags_size)

# Drapeau européen
t.backward(3*(1+ecart)*small_flags_size)
t.right(90)
t.forward((small_flags_size/3)*2 + margin)
t.left(90)
european_flag(small_flags_size*(4+ecart*3))

win.exitonclick()  # Pour quitter lors du click
