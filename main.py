import os
import time
import random
import pygame


def p(*path) -> str:
    return os.path.join(
        os.getcwd(),
        *path
    )


def round_color(color: list) -> tuple:
    return tuple(
        round(x) for x in color
    )


def random_color() -> tuple:
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_speed() -> float:
    return float(random.random() * (max_speed - min_speed) + min_speed)


def calc_speed() -> None:
    for i in range(3):
        color_speed[i] = (to_color[i] - from_color[i]) / speed


pygame.init()
info_object = pygame.display.Info()
w, h = info_object.current_w, info_object.current_h
screen = pygame.display.set_mode((w, h), pygame.NOFRAME)
pygame.display.set_icon(pygame.image.load(p('favicon.ico')).convert_alpha())
pygame.display.set_caption('screensaver.py')
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
running = True
from_color = (0, 0, 0)
current_color = [0, 0, 0]
to_color = random_color()
min_speed = 0.5
max_speed = 5.0
# speed - change color from {from_color} to {to_color} in {speed} seconds
speed = random_speed()
color_speed = [0.0, 0.0, 0.0]
current_timer = 0.0
last_tick = time.time()


calc_speed()


while running:
    for event in pygame.event.get():
        if event.type in (
            pygame.QUIT,
            pygame.KEYDOWN,
            pygame.KEYUP,
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEWHEEL
        ):
            running = False
    now = time.time()
    delta = now - last_tick
    current_timer += delta
    current_color[0] += delta * color_speed[0]
    current_color[1] += delta * color_speed[1]
    current_color[2] += delta * color_speed[2]
    if current_timer >= speed:
        current_timer = 0.0
        current_color = list(to_color)
        from_color = to_color
        to_color = random_color()
        speed = random_speed()
        calc_speed()
    last_tick = now
    screen.fill(round_color(current_color))
    pygame.display.flip()


pygame.event.set_grab(False)
pygame.mouse.set_visible(True)
pygame.quit()
