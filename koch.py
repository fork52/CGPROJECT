import turtle,os

try:
    t=turtle.Turtle()

    def snowflake(lengthSide, levels):
        if levels == 0:
            t.forward(lengthSide)
            return
        lengthSide /= 3.0
        snowflake(lengthSide, levels - 1)
        t.left(60)
        snowflake(lengthSide, levels - 1)
        t.right(120)
        snowflake(lengthSide, levels - 1)
        t.left(60)
        snowflake(lengthSide, levels - 1)


    if __name__ == "__main__":

        screen =turtle.Screen()
        t.speed(0)
        length = 300.0

        t.penup()

        t.backward(length / 2.0)

        t.pendown()

        snowflake(length, 4)
        screen.exitonclick()
except:
    pass


os.system('python Mainpage.py')



