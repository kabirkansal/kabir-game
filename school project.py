# Modules
import turtle
import random
import math

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Alien Shooter!")
wn.bgcolor("black")
wn.tracer(0)

# Choose A Nuber Of Eenemies
number_of_enemies = 168

# Create An Empty List Of Enemies
enemies = []

# Add Enemies To The List
for i in range(number_of_enemies):
    # Enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -690
enemy_start_y = 300
enemy_number = 0

for enemy in enemies:    
    enemy.penup()
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("square")
    enemy.setheading(270)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.goto(x, y)
    # Update The Enemy Number
    enemy_number += 1
    if enemy_number == 28:
        enemy_start_y -= 50
        enemy_number = 0

# Line1 Enemies
line1enemy1 = turtle.Turtle()
line1enemy1.penup()
line1enemy1.speed(0)
line1enemy1.shape("circle")
line1enemy1.color("blue")
line1enemy1.goto(-150, 450)
line1enemy1.setheading(270)

line1enemy2 = turtle.Turtle()
line1enemy2.penup()
line1enemy2.speed(0)
line1enemy2.shape("circle")
line1enemy2.color("blue")
line1enemy2.goto(-100, 450)
line1enemy2.setheading(270)

line1enemy3 = turtle.Turtle()
line1enemy3.penup()
line1enemy3.speed(0)
line1enemy3.shape("circle")
line1enemy3.color("blue")
line1enemy3.goto(-50, 450)
line1enemy3.setheading(270)

line1enemy4 = turtle.Turtle()
line1enemy4.penup()
line1enemy4.speed(0)
line1enemy4.shape("circle")
line1enemy4.color("blue")
line1enemy4.goto(0, 450)
line1enemy4.setheading(270)

line1enemy5 = turtle.Turtle()
line1enemy5.penup()
line1enemy5.speed(0)
line1enemy5.shape("circle")
line1enemy5.color("blue")
line1enemy5.goto(50, 450)
line1enemy5.setheading(270)

line1enemy6 = turtle.Turtle()
line1enemy6.penup()
line1enemy6.speed(0)
line1enemy6.shape("circle")
line1enemy6.color("blue")
line1enemy6.goto(100, 450)
line1enemy6.setheading(270)

# Line2 Enemies
line2enemy1 = turtle.Turtle()
line2enemy1.penup()
line2enemy1.speed(0)
line2enemy1.color("orange")
line2enemy1.shape("triangle")
line2enemy1.setheading(90)
line2enemy1.goto(-50, -450)

line2enemy2 = turtle.Turtle()
line2enemy2.penup()
line2enemy2.speed(0)
line2enemy2.color("orange")
line2enemy2.shape("triangle")
line2enemy2.setheading(90)
line2enemy2.goto(0, -450)

line2enemy3 = turtle.Turtle()
line2enemy3.penup()
line2enemy3.speed(0)
line2enemy3.color("orange")
line2enemy3.shape("triangle")
line2enemy3.setheading(90)
line2enemy3.goto(50, -450)

# Bullet
bullet = turtle.Turtle()
bullet.penup()
bullet.speed(0)
bullet.shape("circle")
bullet.color("yellow")
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Define Bullet State
# Ready - Ready To Fire
# Fire - Bullet Is Firing
bulletstate = "ready"

# Pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("orange")
pen.setposition(-710, 380)
pen.pensize(3)
pen.pendown()
pen.fd(1405)
pen.rt(90)
pen.forward(750)
pen.rt(90)
pen.fd(1405)
pen.rt(90)
pen.forward(750)
pen.hideturtle()

# Score 0
score = 0

# Score Pen
scorepen = turtle.Turtle()
scorepen.penup()
scorepen.color("white")
scorepen.speed(0)
scorepen.goto(0, -350)
scorestring = "Score: %s" %score
scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))
scorepen.ht()

# Player
player = turtle.Turtle()
player.penup()
player.shapesize(0.7, 2.0, outline=None)
player.shape("triangle")
player.color("white")
player.goto(-100, 0)
player.speed(0)
player.lives = 3
player.setheading(90)
player.goto(0, -200)

# Speeds
speed = 0.1
enemyspeed = 0.1
bulletspeed = 20
line1enemy1speed = 0.2
line1enemy2speed = 0.2
line1enemy3speed = 0.2
line1enemy4speed = 0.2
line1enemy5speed = 0.2
line1enemy6speed = 0.2
line2enemy1speed = 0.2
line2enemy2speed = 0.2
line2enemy3speed = 0.2

# Functions
def left():
    player.left(30)

def right():
    player.right(30)

def increase():
    global speed
    speed += 1

def decrease():
    global speed
    speed -= 1

def fire_bullet():
    # Declare Bulletstate As A Global If It Needs Changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move The Bullet To Just Above The PLayer
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Keyboard Bindings
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(increase, "Up")
turtle.onkey(decrease, "Down")
turtle.onkey(fire_bullet, "space")

while True:
    wn.update()
    player.forward(speed)
    bullet.forward(bulletspeed)
    line1enemy1.fd(line1enemy1speed)
    line1enemy2.fd(line1enemy2speed)
    line1enemy3.fd(line1enemy3speed)
    line1enemy4.fd(line1enemy4speed)
    line1enemy5.fd(line1enemy5speed)
    line1enemy6.fd(line1enemy6speed)
    line2enemy1.fd(line2enemy1speed)
    line2enemy2.fd(line2enemy2speed)
    line2enemy3.fd(line2enemy3speed)
    
    # Border Checking
    if player.xcor() > 685 or player.xcor() < -685:
        player.right(180)

    if player.ycor() > 370 or player.ycor() <  -370:
        player.right(180)   
        
    # Check To See If The Bullet Has Gone To The Top
    if bullet.ycor() > 355:
        bullet.hideturtle()
        bulletstate = "ready"

    for enemy in enemies:
        enemy.forward(enemyspeed)

        # Ckeck For A Collision Between The Bullet And The Enemy
        if isCollision(bullet, enemy):
             # Reset The Bullet
             bullet.hideturtle()
             bulletstate = "ready"
             bullet.setposition(0, -400)
             # Reset The Enemy
             enemy.setposition(0, 100000)
             # Update The Score
             score += 10
             scorestring = "Score: %s" %score
             scorepen.clear()
             scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

        # Check For A Collision Between The Player And The Enemy
        if isCollision(player, enemy):
            player.hideturtle()
            bullet.hideturtle()
            enemy.hideturtle()
            scorepen.clear()
            scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
            break

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line1enemy1):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line1enemy1.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line1enemy2):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line1enemy2.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))
        
    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line1enemy3):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line1enemy3.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))
    
    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line1enemy4):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line1enemy4.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line1enemy5):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line1enemy5.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line1enemy6):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line1enemy6.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line2enemy1):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line2enemy1.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line2enemy2):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line2enemy2.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))

    # Ckeck For A Collision Between The Bullet And The Enemy
    if isCollision(bullet, line2enemy3):
        # Reset The Bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset The Enemy
        line2enemy3.setposition(0, 100000)
        # Update The Score
        score += 10
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align="center", font=("Arial", 44, "normal"))    

    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line1enemy1):
        player.hideturtle()
        bullet.hideturtle()
        line1enemy1.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break
    
    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line1enemy2):
        player.hideturtle()
        bullet.hideturtle()
        line1enemy2.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break

    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line1enemy3):
        player.hideturtle()
        bullet.hideturtle()
        line1enemy3.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break
    
    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line1enemy4):
        player.hideturtle()
        bullet.hideturtle()
        line1enemy4.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break

    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line1enemy5):
        player.hideturtle()
        bullet.hideturtle()
        line1enemy5.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break
    
    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line1enemy6):
        player.hideturtle()
        bullet.hideturtle()
        line1enemy6.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break

    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line2enemy1):
        player.hideturtle()
        bullet.hideturtle()
        line2enemy1.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break
    
    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line2enemy2):
        player.hideturtle()
        bullet.hideturtle()
        line2enemy2.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break
    
    # Check For A Collision Between The Player And The Enemy
    if isCollision(player, line2enemy3):
        player.hideturtle()
        bullet.hideturtle()
        line2enemy3.hideturtle()
        scorepen.clear()
        scorepen.write("Game Over", False, align="center", font=("Arial", 44, "normal"))
        break
