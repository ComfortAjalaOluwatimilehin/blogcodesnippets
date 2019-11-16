from swampy.TurtleWorld import *
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


def square(bob, length, n):
    for i in range(1, n + 1):
        angle = 360 / n
        fd(bob, length)
        lt(bob, angle)


#square(bob, 50, 15)
wait_for_user()
