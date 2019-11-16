from swampy.TurtleWorld import *
from IPython.core.display import Math
world = TurtleWorld()
bob = Turtle()
"""
   Write a function called square that takes a parameter named t, which is a turtle. It
   should use the turtle to draw a square.
   Write a function call that passes bob as an argument to square, and then run the
   program again.

"""


def square(bob):
    for i in range(4):
        fd(bob, 100)
        lt(bob)

# square(bob)


"""
Add another parameter, named length, to square. Modify the body so length of the
sides is length, and then modify the function call to provide a second argument. Run
the program again. Test your program with a range of values for length.
"""


def square(bob, length):
    for i in range(4):
        fd(bob, length)
        lt(bob)


#square(bob, 5)

"""
The functions lt and rt make 90-degree turns by default, but you can provide a
second argument that specifies the number of degrees. For example, lt(bob, 45)
turns bob 45 degrees to the left.
Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
"""


def polygon(bob, length, n):
    angle = 360 / n
    for i in range(1, n + 1):
        fd(bob, length)
        lt(bob, angle)


#polygon(bob, 10, 15)

"""
Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by invoking polygon with an appropriate length
and number of sides. Test your function with a range of values of r.

Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
"""


def circle(bob, radius):
    diameter = 2 * radius
    polygon(bob, radius, diameter)


#circle(bob, 20)

"""
Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle.

"""


def arc(bob, radius, angle):
    diameter = 2 * radius
    for i in range(1, diameter + 1):
        fd(bob, radius)
        lt(bob, angle / diameter)


#arc(bob, 5, 76)

wait_for_user()
