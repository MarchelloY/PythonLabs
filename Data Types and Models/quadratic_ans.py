import cmath
import math
import sys

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

#1
print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

#2
x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
  x1 = -(b / (2 * a))
else:
  if discriminant < 0:
    root = cmath.sqrt(discriminant)
  if discriminant > 0:
    root = math.sqrt(discriminant)
  x1 = (-b + root) / (2 * a)
  x2 = (-b - root) / (2 * a)

#3
equation = ""

if a != 0:
    equation += ("{0}x\N{SUPERSCRIPT TWO}").format(a)

if b < 0:
    equation += (" {0}x").format(b)
elif b > 0:
    equation += (" +{0}x").format(b)

if c < 0:
    equation += (" {0}").format(c)
elif c > 0:
    equation += (" +{0}").format(c)

equation += (" = 0 \N{RIGHTWARDS ARROW} x = {0}").format(x1)
if x2 is not None:
    equation += (" or x = {0}").format(x2)
print(equation)