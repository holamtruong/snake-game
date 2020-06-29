
# graphic library
import turtle
# time library
import time

# set delay time is  0.1  second
delay = 0.1


# set up the screen
map = turtle.Screen()
map.title("Snake Game by Truong Ho")
map.bgcolor("gray")
map.setup(width=600, height=600)
map.tracer(0) # => turns off the screen updates


# create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Control function
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"



# Move function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
map.listen()
map.onkeypress(go_up, "w")
map.onkeypress(go_down, "s")
map.onkeypress(go_left, "a")
map.onkeypress(go_right, "d")



# Main game loop
while True:
    map.update()

    move()

    time.sleep(delay)





# stop the sreen
map.mainloop() 





