import random

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = random.randint(10, 800)
    apple.y = random.randint(10, 600)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Nice shot!")
        place_apple()
    else:
        print("You must now pay the penalty!")
        quit()


place_apple()