#Snake game!
import turtle
import random
segments = []
score = 0
highest_score=0
end_position=0
direction = 90
turtle.setup(width=720, height=640)
turtle.bgcolor("black")
turtle.tracer(0)
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")
score_writer.goto(-350, 290)
score_writer.write("Score: 0", font=("Arial", 16, "normal"))
food_size=1
growing=True
food=turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.goto(50,50)
line=turtle.Turtle()
line.color("cyan")
line.penup()
line.goto(-350,270)
line.pendown()
line.forward(700)
line.right(90)
line.forward(560)
line.right(90)
line.forward(700)
line.right(90)
line.forward(560)
line.hideturtle()
pixels=200
running=True
'''start_button=turtle.Turtle()
start_button.shape("square")
start_button.color("white")
start_button.penup()
start_button.goto(200, 290)
start_button.shapesize(stretch_wid=1.7, stretch_len=15)'''
menu_text = turtle.Turtle()
menu_text.hideturtle()
menu_text.penup()
menu_text.color("white")
menu_text.goto(90,283)
menu_text.write("MEDIUM", font=("Arial", 15, "bold"))
menu_text.goto(20, 283)
menu_text.write("EASY", font=("Arial", 15, "bold"))
menu_text.goto(190, 283)
menu_text.write("HARD", font=("Arial", 15, "bold"))
menu_text.goto(270,283)
menu_text.write("END", font=("Arial", 15, "bold"))
h_s=turtle.Turtle()
h_s.color("white")
h_s.penup()
h_s.hideturtle()
h_s.goto(-60,283)
h_s.write("H.S : "+str(highest_score),font=("Arial",15,"bold"))
joke=True
def mouse_click(x, y):
    global pixels,joke
    print(x,y)
    if running==False:
        if 18<x<68 and 290<y<310:
            pixels=300
            start_game()
        if 87<x<170 and 290<y<310:
            pixels=200
            start_game()
        if 188<x<242 and 290<y<310:
            if joke:
                pixels=20
                joke=False
            else:
                joke=True
                pixels=140
            start_game()
        elif 267<309 and 290<y<310:
            end_game()

def end_game():
    if running==False:
        turtle.bye()

def start_game():
    global running,pixels,direction
    if running==False:
        for segment in segments:
            segment.hideturtle()
        direction=90
        running=True
        segments.clear()
        create_snake()
        move()

def increase_speed():
    global pixels
    pixels-=5

def create_snake():
    for i in range(3):
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("blue")
        segment.penup()
        segment.goto(-20*i, 0)
        segments.append(segment)

def pulse_food():
    global food_size, growing
    if growing:
        food_size += 0.05
        if food_size >= 1.5:
            growing = False
    else:
        food_size -= 0.05
        if food_size <= 0.7:
            growing = True
    food.shapesize(food_size)
    turtle.ontimer(pulse_food, 50)

def collision():
    global running,score,highest_score
    if score>highest_score:
        highest_score=score
        h_s.clear()
        h_s.write(
        "H.S : " + str(highest_score),
        font=("Arial", 15, "bold")
    )
    head = segments[0]
    if head.xcor()>350 or head.xcor()<-340 or head.ycor()>270 or head.ycor()<-290:
        score_writer.clear()
        score=0
        running=False
        if joke:
            score_writer.write(
                "Game Over, Collided with wall!",
                    font=("Arial", 15, "normal")
            )
        else:
            score_writer.write(
                "Game Over:) Sorry i joked!",
                    font=("Arial", 15, "normal")
            )
        return True
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            score_writer.clear()
            score=0
            running=False
            score_writer.write(
                "Game,Over, Collided with own body!",
                    font=("Arial", 15, "normal")
            )
            return True
    return False

def body():
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("cyan")
    segment.penup()
    segment.goto(end_position)
    return segment
   
def win():
    if segments[0].distance(food)<20:
        global score
        score+=1
        increase_speed()
        print("Food Eaten!")
        x=random.randrange(-320,320,20)
        y=random.randrange(-260,260,20)
        food.goto(x,y)
        segments.append(body())
    score_writer.clear()
    score_writer.write(
        "Score: " + str(score),
        font=("Arial", 16, "normal")
    )

def move():
    global end_position
    end_position=segments[-1].position()
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].position())
    segments[0].setheading(direction)
    segments[0].forward(20)
    if collision():
        print("GAME OVER!")
        return
    win()
    turtle.update()
    turtle.ontimer(move,pixels)

def up():
    global direction
    if direction!=270:
        direction = 90
def down():
    global direction
    if direction!=90:
        direction = 270
def left():
    global direction
    if direction!=0:
        direction = 180
def right():
    global direction
    if direction!=180:
        direction = 0

create_snake()

turtle.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(start_game,"n")
turtle.onkeypress(end_game,"e")
turtle.onscreenclick(mouse_click)
pulse_food()
move()

turtle.done()
