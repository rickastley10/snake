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
startsegcount = 4
t.tracer(0, 0)
score = 0
highscore =0
t.bgcolor("black")
clr = 100
clrm = 1
calccolour = 0
berrycolour = 200
berrycolourm = 1

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
        t.write("snake game\n        click anywhere / press space to start", font=("Arial", 16, "normal"))
    if menu == 0:
        pass

menu1()

def snake():
    global calccolour
    t.fillcolor(0, 1, 0)
    t.pencolor("black")
    t.goto(px, py)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()
    t.penup()
    t.fillcolor("green")
    calccolour = 0
    for seg in segments:
        if calccolour == 100:
            calccolour = 0
        calccolour += 5
        if calccolour == 100:
            calccolour = 0
        t.fillcolor(0, ((100-calccolour)/255), 0)
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
    global segc, segments, score, highscore

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
        score += 1
        by = (random.randint(-10, 10)) * 20
    else:
        segments.pop()

    if any(px == seg["sx"] and py == seg["sy"] for seg in segments):
        gameover()
    if (px >= 300) or (px <= -300) or (py >= 300) or (py <= -300):
        gameover()
def gameover():
    global px, py, score, segc, segments, startsegcount
    score = 0
    px = 0
    py = 0
    segc = startsegcount
    segments.clear()
    segments = []
    for _ in range(segc):
        segments.append({
            "sx": 0,
            "sy": 0
        })
def berry():
    global berrycolour, berrycolourm
    if berrycolourm == 1:
        berrycolour += 10
        if berrycolour >= 200:
            berrycolour = 200
            berrycolourm = 2
    if berrycolourm == 2:
        berrycolour -= 10
        if berrycolour <= 100:
            berrycolour = 100
            berrycolourm = 1
    t.goto(bx, by)
    t.pendown()
    t.fillcolor(berrycolour/255, 0, 0)
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()
    t.penup()

def gui():
    global score, highscore, clr, clrm
    if score > highscore:
        highscore = score


    if clrm == 1:
        clr += 1
        if clr >= 200:
            clr = 200
            clrm = 2

    elif clrm == 2:
        clr -= 1
        if clr <= 0:
            clr = 0
            clrm = 1

    t.goto(200, 200)
    t.pencolor(0, (200/255), (200/255))
    t.write(f"score: {score}\nhighscore: {highscore}")

    t.goto(300, 300)
    t.pendown()

    t.pencolor(0, clr/255, 100/255)
    t.goto(300, -300)
    t.goto(-300, -300)
    t.goto(-300, 300)
    t.goto(300, 300)
    t.penup()

    



def go_right():
    global facing
    if facing != "left":
        facing = "right"

def go_left():
    global facing
    if facing != "right":
        facing = "left"

def go_up():
    global facing
    if facing != "down":
        facing = "up"

def go_down():
    global facing
    if facing != "up":
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
        mainloop()
    if menu == 0:
        if x < 0:
            touchleft()
        elif 0 < x:
            touchright()

def space():
    global menu
    if menu == 1:
        menu = 0
        mainloop()
    if menu == 0:
        pass
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
t.onkey(space, "space")
t.onscreenclick(click)
t.listen()

def mainloop():
    t.clear()
    
    snakemove()
    snake()
    berry()
    gui()
    
    t.ontimer(mainloop, 100)

t.mainloop()
