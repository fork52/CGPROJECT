import turtle

try:
    def hilbert(step, rule, angle, depth, t):
       if depth > 0:
          a = lambda: hilbert(step, "a", angle, depth - 1, t)
          b = lambda: hilbert(step, "b", angle, depth - 1, t)
          left = lambda: t.left(angle)
          right = lambda: t.right(angle)
          forward = lambda: t.forward(step)
          if rule == "a":
            left(); b(); forward(); right(); a(); forward(); a(); right(); forward(); b(); left();
          if rule == "b":
            right(); a(); forward(); left(); b(); forward(); b(); left(); forward(); a(); right();

    turt = turtle.Turtle()
    turt.speed('fastest')
    hilbert(10, "a", 90, 10, turt)

except:
    pass

