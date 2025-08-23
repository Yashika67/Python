import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Egg Catching Game")
screen.bgcolor("skyblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Basket (player)
basket = turtle.Turtle()
basket.shape("circle")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Egg
egg = turtle.Turtle()
egg.shape("circle")
egg.color("white")
egg.penup()
egg.goto(random.randint(-250, 250), 250)

# Score display
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("black")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

# Basket movement
def move_left():
    x = basket.xcor() - 30
    if x < -270:
        x = -270
    basket.setx(x)

def move_right():
    x = basket.xcor() + 30
    if x > 270:
        x = 270
    basket.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Egg speed
egg_speed = 1

# Game loop
game_on = True
while game_on:
    screen.update()
    egg.sety(egg.ycor() - egg_speed)

    # If egg is caught
    if egg.ycor() < -230 and basket.xcor() - 50 < egg.xcor() < basket.xcor() + 50:
        egg.goto(random.randint(-250, 250), 250)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))
        egg_speed += 0.02  # Increase difficulty

    # If egg touches ground
    if egg.ycor() < -280:
        score_display.clear()
        score_display.write(f"GAME OVER! Final Score: {score}", align="center", font=("Arial", 20, "bold"))
        game_on = False

    time.sleep(0.01)

screen.mainloop()
