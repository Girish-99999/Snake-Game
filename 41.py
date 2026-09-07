#Snake game!
import turtle
import random
segments = []
score = 0
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
    head = segments[0]
    if head.xcor()>340 or head.xcor()<-340 or head.ycor()>260 or head.ycor()<-280:
        score_writer.clear()
        score_writer.write(
            "Score: " + str(score)+"  Game Over Bro :) Snake Collided With Boundary!",
            font=("Arial", 16, "normal"))
        return True
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            score_writer.clear()
            score_writer.write(
            "Score: " + str(score)+"  Game Over Bro :) Snake Collided With Own Body!",
            font=("Arial", 16, "normal"))
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
        print("Food Eaten!")
        x=random.randrange(-320,321,20)
        y=random.randrange(-260,261,20)
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
    turtle.ontimer(move,200)

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

for i in range(3):
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("cyan")
    segment.penup()
    segment.goto(-20*i, 0)
    segments.append(segment)

turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

pulse_food()
move()

turtle.done()
