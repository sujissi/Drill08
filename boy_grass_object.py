from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):  # 생성자 함수 항상 첫번째 인자 selfdudi====
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(selfself): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0,7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def reset_world():
    global running
    global grass
    # global boy
    global team
    global world
    running = True
    world = []
    grass = Grass()
    world.append(grass)
    # boy = Boy()
    team = [Boy() for i in range(10)]
    world += team


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def rander_world():
    clear_canvas()
    # grass.draw()
    # # boy.draw()
    # for boy in team:
    #     boy.draw()
    for o in world:
        o.draw()
    update_canvas()
    pass


def update_world():
    # grass.update()
    # # boy.update()
    # for boy in team:
    #     boy.update()
    for o in world:
        o.update()


# initialization code
open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    rander_world()
    delay(0.05)

# game main loop code

# finalization code

close_canvas()
