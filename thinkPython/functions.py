
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


"""
Exercise 3.5. This exercise can be done using only the statements and other features we have learned
so far.

Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""


def do_four_with_two_arg(fn, valueone, valuetwo):
    fn(valueone, valuetwo)
    fn(valueone, valuetwo)
    fn(valueone, valuetwo)
    fn(valueone, valuetwo)


def print_grid_head(spacing, col_number):
    rep = " - " * spacing + "+"
    print("+", rep * col_number)


def print_grid_line(count, col_number):
    rep = "   " * count + "|"
    print("|", rep * col_number)


def generate_grid(spacing, col_number):
    print_grid_head(spacing, col_number)
    do_four_with_two_arg(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    do_four_with_two_arg(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)


#generate_grid(4, 2)


"""
run: generate_grid(4, 2)
result: 
+  -  -  -  -  +  -  -  -  -  +
|              |              |
|              |              |
|              |              |
|              |              |
+  -  -  -  -  +  -  -  -  -  +
|              |              |
|              |              |
|              |              |
|              |              |
+  -  -  -  -  +  -  -  -  -  +

"""
# Write a function that draws a similar grid with four rows and four columns.


def generate_four_rows_for_columns(repfn, spacing, col_number):
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)


#generate_four_rows_for_columns(do_four_with_two_arg, 4, 4)

"""
run: generate_four_rows_for_columns(do_four_with_two_arg, 4, 4)
result:

+  -  -  -  - + -  -  -  - + -  -  -  - + -  -  -  - +
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
+  -  -  -  - + -  -  -  - + -  -  -  - + -  -  -  - +
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
+  -  -  -  - + -  -  -  - + -  -  -  - + -  -  -  - +
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
+  -  -  -  - + -  -  -  - + -  -  -  - + -  -  -  - +
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
|             |            |            |            |
+  -  -  -  - + -  -  -  - + -  -  -  - + -  -  -  - +

"""
