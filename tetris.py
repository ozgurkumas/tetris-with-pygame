import pygame
import sys
import random

pygame.init()

screen_width = 400
screen_height = 800

grid_scale = 40

black = (0,0,0)
white = (255,255,255)

fps = 2
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

class Figure:
    def __init__(self):
        self.gridList = []
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

    def update(self):
        for i in self.gridList:
            pygame.draw.rect(screen, self.color, (i[0], i[1], grid_scale, grid_scale))
            pygame.draw.rect(screen, white, (i[0], i[1], grid_scale, grid_scale), 1)


class Figure1(Figure): # l block
    def __init__(self):
        self.gridList = [[120,0], [160,0], [200,0], [240, 0]]
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)
      

fig = Figure1()

while True:

    for i in range(int(screen_height/grid_scale)):
        for j in range(int(screen_width/grid_scale)):
            pygame.draw.rect(screen, black, (j * grid_scale, i * grid_scale, grid_scale, grid_scale))
            pygame.draw.rect(screen, white, (j * grid_scale, i * grid_scale, grid_scale, grid_scale),1)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    for i in range(len(fig.gridList)):
                        fig.gridList[i][0] += grid_scale
                elif event.key == pygame.K_LEFT:
                    for i in range(len(fig.gridList)):
                        fig.gridList[i][0] -= grid_scale
                elif event.key == pygame.K_DOWN:
                    for i in range(len(fig.gridList)):
                        fig.gridList[i][1] += grid_scale
          
    for i in range(len(fig.gridList)):
        fig.gridList[i][1] += grid_scale

    fig.update()
    
    pygame.display.update()
    clock.tick(fps)
