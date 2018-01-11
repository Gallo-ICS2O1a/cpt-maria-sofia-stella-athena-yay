ballSize = 30
radius = ballSize / 2
# Obstacle 1 Location
rectPos = PVector(150, 0)
rectPos_2 = PVector(150, 190)
# Obstacle 2 Location
rectPos_3 = PVector(330, 0)
# Obstacle 3
rectPos_4 = PVector(510, 150)
# Obstacle 4
rectPos_5 = PVector(690, 0)
rectPos_6 = PVector(690, 310)
# Obstacle 5
rectPos_7 = PVector(870, 0)
# Speed of Obstacles
speed = 0.7
# Player
player = PVector(50, 200)
# Speed of Player
speedP = PVector(1, 2)
jump = -3.5
# Screen
screen = "startscreen"
collision= 0
# Score
score = 0
currentobstacle = rectPos


def setup():
    size(900, 400)


def reset():
    global player, speed, speedP, jump, screen, collision, score
    global rectPos, rectPos_2
    global rectPos_3
    global rectPos_4
    global rectPos_5, rectPos_6
    global rectPos_7
    global currentobstacle

# Obstacle 1 Location
    rectPos = PVector(150, 0)
    rectPos_2 = PVector(150, 190)
# Obstacle 2 Location
    rectPos_3 = PVector(330, 0)
# Obstacle 3
    rectPos_4 = PVector(510, 150)
# Obstacle 4
    rectPos_5 = PVector(690, 0)
    rectPos_6 = PVector(690, 310)
# Obstacle 5
    rectPos_7 = PVector(870, 0)
# Speed of Obstacles
    speed = 0.7
# Player
    player = PVector(50, 200)
# Speed of Player
    speedP = PVector(1, 2)
    jump = -3.5
# Screen
    collision= 0
    screen = "gamescreen"
# Score
    score = 0
    currentobstacle = rectPos
# Fake Ball


def draw():
    global ballSize
    global radius
    global speed
    global screen
    global speedP
    global player
    global jump
    global collision
    global score
    global currentobstacle
    global rectPos, rectPos_2
    global rectPos_3
    global rectPos_4
    global rectPos_5, rectPos_6
    global rectPos_7

    background(255)

# Start Screen
    if screen == "startscreen":
        background(0)
        fake = PVector(90, 310)

        fill(255)
        textSize(90)
        text("Flappy Ellipse", 175, 100)

# Fake Ball
        fill(255, 0, 0)
        ellipse(fake.x, fake.y, 100, 100)

# Start button
        fill(0)
        rect(420, 150, 70, 30)
        fill(255)
        textSize(30)
        text("Start", 420, 175)

# Instruction button
        fill(0)
        rect(420, 200, 170, 30)
        fill(255)
        textSize(30)
        text("Instructions", 420, 225)  


# Instructions screen
    if screen == "Instructions":
        background(0)
        fill(255)
        textSize(90)
        text("Instructions", 175, 100)
        textSize(30)
        text("""1. Click the mouse to jump. Double-tap the m
2. Avoid the obstacles
3. If the ball hits the obstacles, GAME OVER""", 175, 175)
        fill(0)
        rect(50, 350, 100, 30)
        fill(255)
        textSize(30)
        text("Back", 50, 375)

# Game Screen
    if screen == "gamescreen":
        background(255)
# Player
        fill(255, 0, 0)
        noStroke()
        ellipse(player.x, player.y, ballSize, ballSize)
        player.y += speedP.y
        if mousePressed and player.x <= 190:
            player.x += speedP.x
        if mousePressed:
            player.y += jump

# Player Sizes
        topBall = player.y - radius
        bottomBall = player.y + radius
        leftBall = player.x - radius
        rightBall = player.x + radius

# Obstacles Move When Player Crosses Point
        if player.x >= 190:
            rectPos.x += -speed
            rectPos_2.x += -speed
            rectPos_3.x += -speed
            rectPos_4.x += -speed
            rectPos_5.x += -speed
            rectPos_6.x += -speed
            rectPos_7.x += -speed

# Make Obstacles Reappear
        if (rectPos.x + 30) < 0 and (rectPos_2.x + 30) < 0:
            rectPos.x = rectPos_7.x + 180
            rectPos_2.x = rectPos_7.x + 180
        elif (rectPos_3.x + 30) < 0:
            rectPos_3.x = rectPos.x + 180
        elif (rectPos_4.x + 30) < 0:
            rectPos_4.x = rectPos_3.x + 180
        elif (rectPos_5.x + 30) < 0 and (rectPos_6.x + 30) < 0:
            rectPos_5.x = rectPos_4.x + 180
            rectPos_6.x = rectPos_4.x + 180
        elif (rectPos_7.x + 30) < 0:
            rectPos_7.x = rectPos_6.x + 180 

# Obstacle 1 and 2
        fill(0)
        rect(rectPos.x, rectPos.y, 30, 90)
        rect(rectPos_2.x, rectPos_2.y, 30, height)
# Collision for Obstacle 1 and 2
        if (rightBall >= rectPos.x and leftBall <= (rectPos.x + 30)) and (bottomBall >= (height - (height - rectPos_2.y)) or  topBall <= 90):
             collision = 1
# Score for passing Obstacle 1 and 2
        if leftBall >= rectPos.x and currentobstacle.x == rectPos.x:
            score += 1
            currentobstacle = rectPos_3

# Obstacle 3
        rect(rectPos_3.x, rectPos_3.y, 30, 275)
# Collision for Obstacle 3
        if rightBall >= rectPos_3.x and leftBall <= (rectPos_3.x + 30) and  topBall <= 275:
            collision = 1
# Score for passing Obstacle 3
        if leftBall >= rectPos_3.x and currentobstacle.x == rectPos_3.x:
            score += 1
            currentobstacle = rectPos_4

# Obstacle 4
        rect(rectPos_4.x, rectPos_4.y, 30, height)
# Collision for Obstacle 4
        if rightBall >= rectPos_4.x and leftBall <= (rectPos_4.x + 30) and bottomBall >= (height - (height - rectPos_4.y)):
             collision = 1
# Score for Passing Obstacle 4
        if leftBall >= rectPos_4.x and currentobstacle.x == rectPos_4.x:
            score += 1
            currentobstacle = rectPos_5

# Obstacle 5 and 6
        rect(rectPos_5.x, rectPos_5.y, 30, 210)
        rect(rectPos_6.x, rectPos_6.y, 30, height)
# Collsion for Obstacle 5 and 6
        if (rightBall >= rectPos_5.x and leftBall <= (rectPos_5.x + 30)) and (bottomBall >= (height - (height - rectPos_6.y)) or  topBall <= 220):
             collision = 1
# Score for Passing Obstacle 5 and 6
        if leftBall >= rectPos_5.x and currentobstacle.x == rectPos_5.x:
            score += 1
            currentobstacle = rectPos_7

# Obstacle 7
        rect(rectPos_7.x, rectPos_7.y, 30, 275)
# Collision for Obstacle 7
        if rightBall >= rectPos_7.x and leftBall <= (rectPos_7.x + 30) and  topBall <= 275:
            collision = 1
# Score for Passing Obstacle 7
        if leftBall >= rectPos_7.x and currentobstacle.x == rectPos_7.x:
            score += 1
            currentobstacle = rectPos


# Border Restrictions
        if topBall <= 0 or bottomBall >= height:
            collision = 1

# Score
        fill(217, 177, 177)
        textSize(18)
        text(score, 20, 20)

# Switch Screens from GAME OVER to Start or Game Sceen
    if collision == 1:
        speed = 0
        speedP = PVector(0, 0)
        jump = 0
        screen = "gameover"
        collision = 0

    if screen == "gameover":
        fill(255, 0, 0)
        textSize(60)
        text("GAME OVER", 300, 100)

        textSize(30)
        text("""Play Again
Exit""", 350, 150) 


def mousePressed():
    global screen
    global collision
# Press start button
    if mouseX <= 490 and mouseY <= 180 and mouseX >= 420 and mouseY >= 150 and screen == "startscreen": 
        screen = "gamescreen"
        reset()
# Press instructions button
    if mouseX <= 590 and mouseY <= 230 and mouseX >= 420 and mouseY >= 200 and screen == "startscreen":
        screen = "Instructions"
# Press back button
    if mouseX <= 150 and mouseY <= 380 and mouseX >= 50 and mouseY >= 350 and screen == "Instructions": 
        screen = "startscreen"       
# Play again from Game Over screen
    if mouseX <= 500 and mouseY <= 158 and mouseX >= 350 and mouseY >= 125 and screen == "gameover":
        screen = "gamescreen"
        reset()
# Go to Start Screen by Pressing Exit
    if mouseX <= 450 and mouseY <= 203 and mouseX >= 350 and mouseY >= 170 and screen == "gameover":
        screen = "startscreen"
