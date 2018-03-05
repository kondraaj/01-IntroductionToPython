"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Aaron Kondrat.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

pepperoni = rg.SimpleTurtle()
pepperoni.pen = rg.Pen('black', 5)
pepperoni.speed = 35

size = 90

for k in range(16):
    pepperoni.draw_circle(size)
    pepperoni.pen_up()
    pepperoni.left(37)
    pepperoni.forward(7)
    pepperoni.right(12)
    pepperoni.pen_down()
    size = size + 10

sausage = rg.SimpleTurtle()
sausage.pen = rg.Pen('blue', 2)
sausage.speed = 20

size_1 = 90

for x in range(17):
    sausage.draw_square(size_1)
    sausage.pen_up()
    sausage.right(45)
    sausage.forward(7)
    sausage.right(50)
    sausage.pen_down()
    size_1 = size_1 - 5

window.close_on_mouse_click()
