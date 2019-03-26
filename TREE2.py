import turtle,os

try:
    t = turtle.Turtle()
    turtle.bgcolor('grey')
    t.lt(90)

    t.penup()
    t.back(60)
    t.pendown()

    lv = 11
    l = 120
    s = 17

    t.width(lv)

    t.penup()
    t.bk(l)
    t.pendown()
    t.fd(l)
except:
    pass

def draw_tree(l, level):
    try:
        width = t.width()  # save the current pen width

        t.width(width * 3.0 / 4.0)  # narrow the pen width

        l = 3.0 / 4.0 * l

        t.lt(s)
        t.fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        t.bk(l)
        t.rt(2 * s)
        t.fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        t.bk(l)
        t.lt(s)

        t.width(width)  # restore the previous pen width
    except:
        pass

try:
    t.speed("fastest")

    draw_tree(l, 2)

    turtle.done()
except:
    pass



os.system('python Mainpage.py')


