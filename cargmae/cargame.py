import turtle

# Screen setup
wn = turtle.Screen()
wn.title("Car Racing Game")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Draw finish line
finish_line = turtle.Turtle()
finish_line.color("black")
finish_line.penup()
finish_line.goto(300, 250)
finish_line.pendown()
finish_line.goto(300, -250)
finish_line.hideturtle()

# Player 1 setup
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("red")
player1.shapesize(stretch_wid=1, stretch_len=2)
player1.penup()
player1.goto(-350, 100)

# Player 2 setup
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("blue")
player2.shapesize(stretch_wid=1, stretch_len=2)
player2.penup()
player2.goto(-350, -100)

# Player 1 movement function
def move_player1():
    x = player1.xcor()
    x += 10
    player1.setx(x)

# Player 2 movement function
def move_player2():
    x = player2.xcor()
    x += 10
    player2.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(move_player1, "w")
wn.onkey(move_player2, "Up")

# Main game loop
while True:
    wn.update()
    
    # Check for win
    if player1.xcor() > 300:
        player1.goto(-350, 100)
        player2.goto(-350, -100)
        print("Player 1 wins!")
    elif player2.xcor() > 300:
        player1.goto(-350, 100)
        player2.goto(-350, -100)
        print("Player 2 wins!")
