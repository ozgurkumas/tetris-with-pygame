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

def minList(index, list_):
    empty_list = []
    for i in list_:
        empty_list.append(i[index])
    return min(empty_list)
    
def maxList(index, list_):
    empty_list = []
    for i in list_:
        empty_list.append(i[index])
    return max(empty_list)

class Figure:
    def __init__(self):
        self.gridList = []
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

    def update(self):
        for i in self.gridList:
            pygame.draw.rect(screen, self.color, (i[0], i[1], grid_scale, grid_scale))
            pygame.draw.rect(screen, white, (i[0], i[1], grid_scale, grid_scale), 1)


class Figure1(Figure): # l block
    def __init__(self):
        self.gridList = [[120,0], [160,0], [200,0], [240, 0]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)
      

fig = Figure1()
others_list = []


while True:

    for i in range(int(screen_height/grid_scale)):
        for j in range(int(screen_width/grid_scale)):
            pygame.draw.rect(screen, black, (j * grid_scale, i * grid_scale, grid_scale, grid_scale))
            pygame.draw.rect(screen, white, (j * grid_scale, i * grid_scale, grid_scale, grid_scale),1)

    if(fig.isActive==False):
        others_list.append(fig)
        fig = None
        fig = Figure1()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if fig.isActive==True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if maxList(0, fig.gridList) < screen_width-grid_scale:
                            for i in range(len(fig.gridList)):
                                fig.gridList[i][0] += grid_scale
                    elif event.key == pygame.K_LEFT:
                        if minList(0, fig.gridList) > 0:
                            for i in range(len(fig.gridList)):
                                fig.gridList[i][0] -= grid_scale
                    elif event.key == pygame.K_DOWN:
                        if maxList(1, fig.gridList) < screen_height-grid_scale:
                            for i in range(len(fig.gridList)):
                                fig.gridList[i][1] += grid_scale
                        else:
                            fig.isActive = False
          
    if fig.isActive == True:
            if maxList(1, fig.gridList) < screen_height-grid_scale:
                for i in range(len(fig.gridList)):
                    fig.gridList[i][1] += grid_scale
            else:
                fig.isActive = False

    fig.update()
    for object_ in others_list:
        object_.update()
    
    pygame.display.update()
    clock.tick(fps)
