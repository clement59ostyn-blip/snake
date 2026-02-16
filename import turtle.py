import turtle
import time
import random

# ----------------------------
# Configuration de la fenêtre
# ----------------------------
fenetre = turtle.Screen()
fenetre.title("Snake Game")
fenetre.bgcolor("black")
fenetre.setup(width=600, height=600)
fenetre.tracer(0)  # enlève l'animation automatique
fenetre.tracer(0)

# ----------------------------
# Tête du serpent
# ----------------------------
tete = turtle.Turtle()
tete.speed(0)
tete.shape("square")
tete.color("lime")
tete.penup()
tete.goto(0, 0)
tete.direction = "stop"

# ----------------------------
# Pomme
# ----------------------------
pomme = turtle.Turtle()
pomme.speed(0)
pomme.shape("circle")
pomme.color("red")
pomme.penup()
pomme.goto(0, 100)

# ----------------------------
# Corps du serpent
# ----------------------------
segments = []

# ----------------------------
# Score
# ----------------------------
score = 0

affichage = turtle.Turtle()
affichage.speed(0)
affichage.color("white")
affichage.penup()
affichage.hideturtle()
affichage.goto(0, 260)
affichage.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# ----------------------------
# Fonctions de déplacement
# ----------------------------
def monter():
    if tete.direction != "down":
        tete.direction = "up"

def descendre():
    if tete.direction != "up":
        tete.direction = "down"

def gauche():
    if tete.direction != "right":
        tete.direction = "left"

def droite():
    if tete.direction != "left":
        tete.direction = "right"

def bouger():
    if tete.direction == "up":
        y = tete.ycor()
        tete.sety(y + 20)

    if tete.direction == "down":
        y = tete.ycor()
        tete.sety(y - 20)

    if tete.direction == "left":
        x = tete.xcor()
        tete.setx(x - 20)

    if tete.direction == "right":
        x = tete.xcor()
        tete.setx(x + 20)

# ----------------------------
# Clavier
# ----------------------------
fenetre.listen()
fenetre.onkeypress(monter, "Up")
fenetre.onkeypress(descendre, "Down")
fenetre.onkeypress(gauche, "Left")
fenetre.onkeypress(droite, "Right")

# ----------------------------
# Boucle principale
# ----------------------------
while True:
    fenetre.update()
    time.sleep(0.1)

    # Collision avec le mur
    if (tete.xcor() > 290 or tete.xcor() < -290 or
        tete.ycor() > 290 or tete.ycor() < -290):

        time.sleep(1)
        tete.goto(0, 0)
        tete.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        affichage.clear()
        affichage.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        print("GAME OVER "*200)
        time.sleep(2)
        fenetre.bye()
        print("GAME OVER "*200)
    # Collision avec la pomme
    if tete.distance(pomme) < 20:
        x = random.randrange(-260, 260, 20)
        y = random.randrange(-260, 260, 20)
        pomme.goto(x, y)
        nouveau_segment = turtle.Turtle()
        nouveau_segment.speed(0)
        nouveau_segment.shape("square")
        nouveau_segment.color("green")
        nouveau_segment.penup()
        segments.append(nouveau_segment)
        score += 1
        affichage.clear()
        affichage.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    # Déplacement du corps
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(tete.xcor(), tete.ycor())
    bouger()
    # Collision avec soi-même
    for segment in segments:
        if segment.distance(tete) < 20:
            time.sleep(1)
            tete.goto(0, 0)
            tete.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            affichage.clear()
            affichage.write("Score: 0", align="center", font=("Courier", 24, "normal"))
            print("game over")
# ----------------------------
# Bordures
# ----------------------------
    bordure = turtle.Turtle
    bordure.speed:0
    bordure.color:"white"
    bordure.pensize:3
    bordure.penup
    bordure.goto:(-290, -290)
    bordure.pendown
    for i in range(4):
        bordure.forward:580
        bordure.left:90
    bordure.hideturtle