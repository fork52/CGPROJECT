import random,pygame,os,sys

YELLOW = (255, 255, 0)
BLACK = (0,0,0)
OCHRE = (179, 143, 0)
GREEN = (45, 134, 45)
BROWN = (128, 60, 0)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#Generating the huge point list
X = [0]
Y = [0]

for n in range(100000):
    r = random.uniform(0, 100)
    if r < 1.0:
        x = 0
        y = 0.16*Y[n-1]
    elif r < 86.0:
        x = 0.85*X[n-1] + 0.04*Y[n-1]
        y = -0.04*X[n-1] + 0.85*Y[n-1]+1.6
    elif r < 93.0:
        x = 0.2*X[n-1] - 0.26*Y[n-1]
        y = 0.23*X[n-1] + 0.22*Y[n-1] + 1.6
    else:
        x = -0.15*X[n-1] + 0.28*Y[n-1]
        y = 0.26*X[n-1] + 0.24*Y[n-1] + 0.44
    X.append(x)
    Y.append(y)



def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 50)

    pygame.init()

    pygame.display.set_caption('Bransley_Fern')

    DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    #FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF.fill(BLACK)

    for coordinate in zip(X,Y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT CONDITION
                pygame.quit()
                os.system('python Mainpage.py')
                sys.exit()

        x1 = round(coordinate[0]*70)+400
        y1 = 600-round(coordinate[1]*50) - 30
        pygame.draw.line(DISPLAYSURF, GREEN, (x1, y1), (x1, y1))

        pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT CONDITION
                pygame.quit()
                os.system('python Mainpage.py')
                sys.exit()
        pygame.display.update()



main()