import pygame, math ,sys,os

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 30)
window = pygame.display.set_mode((1000, 690))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()



def waitwithCurrentScreen(timeInmilliSecs):
    '''A WAIT FUNCTION'''
    FPSCLOCK = pygame.time.Clock()
    while timeInmilliSecs>=0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # QUIT CONDITION
                pygame.quit()
                os.system('python Mainpage.py')
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(250)
        timeInmilliSecs = timeInmilliSecs-1


def Tree(x1, y1, angle, depth,key=True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT CONDITION
            pygame.quit()
            os.system('python Mainpage.py')
            sys.exit()
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 8.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 8.0)
        if key:
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * 30.0)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * 30.0)
            pygame.draw.line(screen, (139,69,19), (x1, y1), (x2, y2), depth)
        elif depth==1:
            pygame.draw.line(screen, (50,205,50), (x1, y1), (x2, y2), depth)
        else:
            pygame.draw.line(screen, (128,128,0), (x1, y1), (x2, y2), depth)
        Tree(x2, y2, angle - 10, depth - 1,key=False)
        Tree(x2, y2, angle + 30, depth - 1,key=False)
        waitwithCurrentScreen(5)
        pygame.display.flip()


def input(event):
    if event.type == pygame.QUIT:
        exit(0)

Tree(500, 680, -90, 10)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT CONDITION
            pygame.quit()
            os.system('python Mainpage.py')
            sys.exit()
    pygame.display.update()




