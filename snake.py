import turtle as t
import random
t.hideturtle()
facing = "up"
t.penup()
px, py = 0, 0
segments = []
t.title("snake")
bx = (random.randint(-10, 10)) * 20
by = (random.randint(-10, 10)) * 20
segc = 4
t.tracer(0, 0)


for _ in range(segc):
    segments.append({
        "sx": 0,
        "sy": 0
    })

menu = 1

def menu1():
    if menu == 1:
        t.goto(-100, 0)
        t.pencolor("red")
        t.write("snake game\n        click anywhere to start", font=("Arial", 16, "normal"))
    if menu == 0:
        mainloop()

menu1()

def snake():
    t.fillcolor("black")
    t.goto(px, py)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()
    t.penup()
    for seg in segments:
        t.goto(seg["sx"], seg["sy"])
        t.pendown()
        t.begin_fill()
        for _ in range(4):
            t.forward(20)
            t.right(90)
        t.end_fill()
        t.penup()

def snakemove():
    global px, py
    global bx, by
    global segc, segments

    if facing == "up":
        segments.insert(0, {"sx": px, "sy": py})
        py += 20
    elif facing == "down":
        segments.insert(0, {"sx": px, "sy": py})
        py -= 20
    elif facing == "left":
        segments.insert(0, {"sx": px, "sy": py})
        px -= 20
    elif facing == "right":
        segments.insert(0, {"sx": px, "sy": py})
        px += 20

    if px == bx and py == by:
        bx = (random.randint(-10, 10)) * 20
        by = (random.randint(-10, 10)) * 20
    else:
        segments.pop()

    if any(px == seg["sx"] and py == seg["sy"] for seg in segments):
        segc = 4
        segments.clear()
        segments = []
        for _ in range(segc):
            segments.append({
                "sx": 0,
                "sy": 0
            })
        px = 0
        py = 0

def berry():
    t.goto(bx, by)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()
    t.penup()

def go_right():
    global facing
    facing = "right"

def go_left():
    global facing
    facing = "left"

def go_up():
    global facing
    facing = "up"

def go_down():
    global facing
    facing = "down"

def touchleft():
    global facing
    if facing == "right":
        facing = "up"
    elif facing == "up":
        facing = "left"
    elif facing == "left":
        facing = "down"
    elif facing == "down":
        facing = "right"

def touchright():
    global facing
    if facing == "right":
        facing = "down"
    elif facing == "down":
        facing = "left"
    elif facing == "left":
        facing = "up"
    elif facing == "up":
        facing = "right"

def click(x, y):
    global menu
    if menu == 1:
        menu = 0
        menu1()
    if menu == 0:
        if x < 0:
            touchleft()
        elif 0 < x:
            touchright()

t.onkey(go_up, "Up")
t.onkey(go_down, "Down")
t.onkey(go_left, "Left")
t.onkey(go_right, "Right")
t.onkey(go_up, "w")
t.onkey(go_down, "s")
t.onkey(go_left, "a")
t.onkey(go_right, "d")
t.onkey(touchleft, "q")
t.onkey(touchright, "e")
t.onscreenclick(click)
t.listen()

def mainloop():
    t.clear()
    snake()
    berry()
    snakemove()
    t.ontimer(mainloop, 300)

t.mainloop()
