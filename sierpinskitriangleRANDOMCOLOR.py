import turtle
import random
c_list= ['blue','red','orange','white','yellow',
                'brown','cyan','skyblue','magenta','chocolate','lightgreen','gold'] #random lsit of colors

def drawTriangle(pts,c,turt):
    turt.fillcolor(c)
    turt.pencolor('black')
    turt.up()
    turt.goto(pts[0][0],pts[0][1])
    turt.down()
    turt.begin_fill()
    turt.goto(pts[1][0],pts[1][1])
    turt.goto(pts[2][0],pts[2][1])
    turt.goto(pts[0][0],pts[0][1])
    turt.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(pts,angle,turt):
    global c_list
    drawTriangle(pts,random.choice(c_list),turt)
    if (angle > 0):
        sierpinski([pts[0],
                        getMid(pts[0], pts[1]),
                        getMid(pts[0], pts[2])],
                   angle-1, turt)
        sierpinski([pts[1],
                        getMid(pts[0], pts[1]),
                        getMid(pts[1], pts[2])],
                   angle-1, turt)
        sierpinski([pts[2],
                        getMid(pts[2], pts[1]),
                        getMid(pts[0], pts[2])],
                   angle-1, turt)

def main():
   turt = turtle.Turtle()
   screen = turtle.Screen()
   Initial_pts = [[-200,-50],[0,200],[200,-50]]
   sierpinski(Initial_pts,5,turt)
   screen.exitonclick()

main()
