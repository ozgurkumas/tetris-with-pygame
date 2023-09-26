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
        self.rootPos = []
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

    def update(self):
        for i in self.gridList:
            pygame.draw.rect(screen, self.color, (i[0], i[1], grid_scale, grid_scale))
            pygame.draw.rect(screen, white, (i[0], i[1], grid_scale, grid_scale), 1)

    def rotate(self):
        posK = self.rootPos[0]
        posM = self.rootPos[1]
        for i in range(len(self.gridList)):
            posX = self.gridList[i][0]
            posY = self.gridList[i][1]
            self.gridList[i][0] = posK + posY - posM
            self.gridList[i][1] = posM + posK - posX


class Figure1(Figure): # l block
    def __init__(self):
        self.gridList = [[120,0], [160,0], [200,0], [240, 0]]
        self.rootPos = [self.gridList[1][0], self.gridList[1][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

class Figure2(Figure): #j block
    def __init__(self):
        self.gridList = [[120,0], [120,40], [160,40], [200, 40]]
        self.rootPos = [self.gridList[2][0], self.gridList[2][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

class Figure3(Figure): #L block
    def __init__(self):
        self.gridList = [[200,0], [200,40], [160,40], [120, 40]]
        self.rootPos = [self.gridList[2][0], self.gridList[2][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

class Figure4(Figure): #o block
    def __init__(self):
        self.gridList = [[200,0], [200,40], [160,40], [160, 0]]
        self.rootPos = [self.gridList[1][0], self.gridList[1][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

class Figure5(Figure): #s block
    def __init__(self):
        self.gridList = [[160,0], [160,40], [120,40], [200, 0]]
        self.rootPos = [self.gridList[1][0], self.gridList[1][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

class Figure6(Figure): #t block
    def __init__(self):
        self.gridList = [[160,0], [160,40], [120,40], [200, 40]]
        self.rootPos = [self.gridList[1][0], self.gridList[1][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)

class Figure7(Figure): #z block
    def __init__(self):
        self.gridList = [[160,0], [160,40], [120,0], [200, 40]]
        self.rootPos = [self.gridList[1][0], self.gridList[1][1]]
        self.isActive = True
        self.color_list = [(0, 0, 255), (204, 96, 86), (208, 230, 101), (176, 26, 166), (40, 155, 184)]
        self.color = random.choice(self.color_list)


def rotPerm(main_obj, others): #permission for rotating
    rotPermBool = True
    positions = []
    for pos in main_obj.gridList:
        positions.append([pos[0], pos[1]])
    posK = main_obj.rootPos[0]
    posM = main_obj.rootPos[1]
    for i in range(len(positions)):
        posX = positions[i][0]
        posY = positions[i][1]
        positions[i][0] = posK + posY - posM
        positions[i][1] = posM + posK - posX
    
    
    if(maxList(0, positions) > screen_width - grid_scale):
        difference = int( (maxList(0, positions) - screen_width + grid_scale)/grid_scale )
        for i in range(len(main_obj.gridList)):
            main_obj.gridList[i][1] -= (difference * grid_scale)
    elif(minList(0, positions) < 0):
        difference = int( (-minList(0, positions))/grid_scale )
        for i in range(len(main_obj.gridList)):
            main_obj.gridList[i][1] += (difference * grid_scale)
    elif maxList(1, positions) > screen_height-grid_scale:
        rotPermBool = False

    for pos in positions:
        for object_ in others:
            if pos in object_.gridList:
                rotPermBool = False
                break

    return rotPermBool
      

def perm(main_obj, others, dir):
    positions = []
    permission_bool = True
    if len(others)>0:
        if dir==0: #down
            for pos in main_obj.gridList:
                positions.append([pos[0], pos[1]+grid_scale])
            for pos in positions:
                for object_ in others:
                    if pos in object_.gridList[:]:
                        permission_bool = False
                        main_obj.isActive = False
                        break
        elif dir==1: #right
            for pos in main_obj.gridList:
                positions.append([pos[0]+grid_scale, pos[1]])
            for pos in positions:
                for object_ in others:
                    if pos in object_.gridList:
                        permission_bool = False
                        break
        elif dir==2: #left
            for pos in main_obj.gridList:
                positions.append([pos[0]-grid_scale, pos[1]])
            for pos in positions:
                for object_ in others:
                    if pos in object_.gridList:
                        permission_bool = False
                        break
    return permission_bool

fig = random.choice([Figure1(), Figure2(), Figure3(), Figure4(), Figure5(), Figure6(), Figure7()])
others_list = []


while True:

    for i in range(int(screen_height/grid_scale)):
        for j in range(int(screen_width/grid_scale)):
            pygame.draw.rect(screen, black, (j * grid_scale, i * grid_scale, grid_scale, grid_scale))
            pygame.draw.rect(screen, white, (j * grid_scale, i * grid_scale, grid_scale, grid_scale),1)

    if(fig.isActive==False):
        others_list.append(fig)
        fig = None
        fig = random.choice([Figure1(), Figure2(), Figure3(), Figure4(), Figure5(), Figure6(), Figure7()])

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if fig.isActive==True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if maxList(0, fig.gridList) < screen_width-grid_scale and perm(fig, others_list, 1)==True:
                            for i in range(len(fig.gridList)):
                                fig.gridList[i][0] += grid_scale
                            fig.rootPos = [fig.gridList[1][0], fig.gridList[1][1]]
                    elif event.key == pygame.K_LEFT:
                        if minList(0, fig.gridList) > 0 and perm(fig, others_list, 2)==True:
                            for i in range(len(fig.gridList)):
                                fig.gridList[i][0] -= grid_scale
                            fig.rootPos = [fig.gridList[1][0], fig.gridList[1][1]]
                    elif event.key == pygame.K_DOWN:
                        if perm(fig, others_list, 0)==True:
                            if maxList(1, fig.gridList) < screen_height-grid_scale:
                                for i in range(len(fig.gridList)):
                                    fig.gridList[i][1] += grid_scale
                                fig.rootPos = [fig.gridList[1][0], fig.gridList[1][1]]
                            else:
                                fig.isActive = False
                    elif event.key == pygame.K_SPACE:
                        if rotPerm(fig, others_list):
                            fig.rotate()
          
    if fig.isActive == True and perm(fig, others_list, 0)==True: # down 0, right 1, left 2
            if maxList(1, fig.gridList) < screen_height-grid_scale:
                for i in range(len(fig.gridList)):
                    fig.gridList[i][1] += grid_scale
                fig.rootPos = [fig.gridList[1][0], fig.gridList[1][1]]
            else:
                fig.isActive = False

    fig.update()
    for object_ in others_list:
        object_.update()
    
    pygame.display.update()
    clock.tick(fps)
