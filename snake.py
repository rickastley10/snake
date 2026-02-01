import turtle as t
import random
facing = "up"
t.penup()
px, py = 0, 0
segments = []
t.title("snake")
bx = (random.randint(-10, 10))*20
by = (random.randint(-10, 10))*20
segc = 4
t.tracer(0, 0)
for _ in range(segc):
    segments.append({
        "sx": 0,
        "sy": 0
    })
    
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
    for _ in segments:
        t.goto(_["sx"], _["sy"])
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
        
        bx = (random.randint(-10, 10))*20
        by = (random.randint(-10, 10))*20
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
    

def right():
    global facing
    facing = "right"

def left():
    global facing
    facing = "left"

def up():
    global facing
    facing = "up"

def down():
    global facing
    facing = "down"

def click(x, y):
    if y < 0 and 100 > x > -100:
        down()
    if y > 0 and 100 > x > -100:
        up()
    if x < 0 and 100 > y > -100:
        left()
    if x > 0 and 100 > y > -100:
        right()

t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onscreenclick(click)
t.listen()

def mainloop():
    t.clear()

    snake()
    berry()
    snakemove()

    t.ontimer(mainloop, 300)

mainloop()

t.mainloop()