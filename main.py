import pygame
import menu
import grid
import square
import figureT
import straight_line
import zigzag
import zigzag2
import gamma
import gamma2
from constants import *
import random
import math

pygame.init()

window = pygame.display.set_mode((WIDTH + WIDTH_MENU, WIDTH / AMOUNT_WIDTH * AMOUNT_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Still the same old Tetris')

score = 0
speed = 1
m = menu.Menu(2)

gr = grid.Grid()
gr.fill_field()

def value_score():
    global score
    if score < 2:
        return 1
    else:
        return int(math.log2(score))


def choice_fig():
    fig_list = [square.Square(0, random.randint(0, AMOUNT_WIDTH - WIDTH_SQUARE), value_score()),
                figureT.FigureT(0, random.randint(0, AMOUNT_WIDTH - WIDTH_T), value_score(), 0),
                straight_line.Straight_line(0, random.randint(0, AMOUNT_WIDTH - WIDTH_LINE), value_score(), 0),
                zigzag.Zigzag(0, random.randint(0, AMOUNT_WIDTH - WIDTH_ZIGZAG), value_score(), 0),
                zigzag2.Zigzag2(0, random.randint(0, AMOUNT_WIDTH - WIDTH_ZIGZAG), value_score(), 0),
                gamma.Gamma(0, random.randint(0, AMOUNT_WIDTH - WIDTH_GAMMA), value_score(), 0),
                gamma2.Gamma2(0, random.randint(0, AMOUNT_WIDTH - WIDTH_GAMMA), value_score(), 0)]

    fig = random.choice(fig_list)
    return fig

fig = choice_fig()
gr.fill_by_figure(fig)

wait = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill(BLACK)
    m.draw(window, score, speed)

    if wait == 0:
        fig.speed = fig.move_down(gr)
        gr.refill_field(fig, (fig.row - 1, fig.column))
        wait = FPS // fig.speed
    elif wait % 4 == 1:
        coor = fig.update(gr)
        gr.refill_field(fig, coor)
        wait -= 1
    else:
        wait -= 1
    if fig.stop(gr):
        score = gr.one_line()
        fig = choice_fig()
        speed = fig.speed
        gr.fill_by_figure(fig)

    for row in gr.field:
        for c in row:
            c.draw(window)
    pygame.display.update()
    clock.tick(FPS)