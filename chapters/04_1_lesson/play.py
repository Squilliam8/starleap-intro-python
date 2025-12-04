import turtle
import time 
import random

screen = turtle.Screen()
screen.setup(800, 800)
turtle.tracer(False)

turtles: list[turtle.Turtle] = []


X_BOUND=800
Y_BOUND=800

def draw_bounds():
    t = turtle.Turtle()
    t.goto(X_BOUND, Y_BOUND)
    t.pendown()
    t.goto(X_BOUND, -Y_BOUND)
    t.goto(-X_BOUND, -Y_BOUND)
    t.goto(-X_BOUND, Y_BOUND)
    t.goto(X_BOUND, Y_BOUND)
    t.hideturtle()
    screen.update()
draw_bounds()


def add_turtle(x, y):
    global turtles
    t = turtle.Turtle()
    turtle.colormode(255)
    t.color((random.randint(0,255), random.randint(0, 255), random.randint(0, 255)))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.shape('turtle')
    turtles.append(t)
screen.onclick(add_turtle)



while True:
    for t in turtles:
        t.pensize(4)
        (old_x, old_y) =t.position()
        possible_moves = [t.forward, t.back, t.right, t.left]
        random_value = random.randint(1, 400)
        random.choice(possible_moves)(random_value)
        (new_x, new_y) = t.position()
        if (new_x > X_BOUND or new_x < -X_BOUND or new_y > Y_BOUND or new_y < -Y_BOUND):
            t.goto(old_x, old_y)
    
    
    time.sleep(0)
    screen.update()




turtle.mainloop()