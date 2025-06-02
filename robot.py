import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
MIN_SPEED = 2
MAX_SPEED = 5

score = 0
robot = Actor("robo.png")
coin = Actor("coin.png")
bomb = Actor("bomb.png")
speed= 4
robot.pos = (WIDTH/2, HEIGHT/2)
bomb.pos = (randint(50,WIDTH-50), randint(50, HEIGHT - 50))
coin.pos = (randint(50,WIDTH-50), randint(50, HEIGHT - 50))
def draw():
    screen.clear()
    screen.blit("background.png", (0,0))
    screen.draw.text("Score: " + str(score), (50, 50), color="white")
    robot.draw()
    coin.draw()
    bomb.draw()


def update():
    global robot, coin, bomb, speed
    if keyboard.left:
        robot.image = "roboleft"
        robot.x = robot.x - speed
        POS = robot.pos
        #
        robot.pos = POS
    elif keyboard.right:
        robot.x = robot.x + speed
        POS = robot.pos
        robot.image = "roboleft"
        robot.pos = POS  
    elif keyboard.up:
        robot.y -= speed
        POS = robot.pos
        robot.image = "robo"
        robot.pos = POS 
    elif keyboard.down:
        robot.y += speed
        POS = robot.pos
        robot.image = "robo"
        robot.pos = POS 
    else:
        
pgzrun.go()