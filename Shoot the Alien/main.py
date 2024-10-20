import pgzrun
from random import randint
WIDTH= 600
HEIGHT= 600
TITLE= 'Shoot the Alien'

Sprite= Actor('alien')
def draw ():
    screen.clear()
    screen.fill('DARK BLUE')
    Sprite.draw()

def placealien ():
    Sprite.x=randint(50,WIDTH-50)
    Sprite.y=randint(50,HEIGHT-50)


def update ():
    pass
placealien()
pgzrun.go()