import turtle as tu,time

tu.title('Fractal')

tu.bgcolor("green")
foo = tu.Turtle()
foo.left(90)
foo.speed(20)

#recursion
def draw(l):
    if(l<4):
        return
    else:
        foo.forward(l)
        foo.left(30)
        draw(l*0.67)
        foo.right(60)
        draw(l*0.67)
        foo.left(30)
        foo.backward(l)

draw(100)


time.sleep(10)