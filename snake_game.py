
# ----------------------------------------------------------
# Graphic library
import turtle
# Time library
import time
# Random number library
import random
# ----------------------------------------------------------


# ----------------------------------------------------------
# The snake speed (set delay time is  0.1  second)
start_speed = 0.1
snake_speed = start_speed


# Set the game score
score = 0
high_score = 0


# Set up the map
map = turtle.Screen()
map.title("Snake Game by Truong Ho")
map.bgcolor("gray")
map.setup(width=600, height=600)
map.tracer(0)  # <= turns off the screen updates

# Random the food location


def random_food_point():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    return x, y


# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"  # <= set defaut direction of the snake head

# Create the snake body
segments = []

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
# <= set random location of the food when player start the new game
food.goto(random_food_point())

# Write the player score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Courier", 18, "normal"))

# ----------------------------------------------------------


# ----------------------------------------------------------
# Control function
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
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
map.onkeypress(go_up, "Up")
map.onkeypress(go_down, "Down")
map.onkeypress(go_left, "Left")
map.onkeypress(go_right, "Right")

# ----------------------------------------------------------


# ----------------------------------------------------------
# Main game loop
while True:
    map.update()

    # Check for a  colision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # stop the snake move
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the snake body
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the snake speed
        snake_speed = start_speed

        # Write the final score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 18, "normal"))

        # Reset the food location
        food.goto(random_food_point())

    # Check for a colision with the food
    if head.distance(food) < 20:

        # Move the food to random spot
        food.goto(random_food_point())

        # Add the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the game level
        snake_speed -= 0.001

        # Increase the score
        score += 10

        # Game record
        if score > high_score:
            high_score = score

        # Write the last score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 18, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Call 'move' funtion
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segment list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the snake speed
            snake_speed = start_speed

            # Write the final score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score),
                      align="center", font=("Courier", 18, "normal"))

            # Reset the food location
            food.goto(random_food_point())

    # Set the snake speed
    time.sleep(snake_speed)


# Keep the
map.mainloop()

# ----------------------------------------------------------
