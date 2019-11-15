
"""
Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
the value of len("allen") is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.
"""


def right_justify(s):
    print((" " * 70) + s)

# right_justify("allen")


"""
Exercise 3.4. A function object is a value you can assign to a variable or pass as an argument. For
example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
f()
f()
Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
print 'spam'
do_twice(print_spam)

"""


def do_four(fn, value):
    fn(value)
    fn(value)
    fn(value)
    fn(value)


#do_four(print, "My name is Comfort Ajala")
