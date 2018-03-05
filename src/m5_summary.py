"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Aaron Kondrat.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

zebra = rg.SimpleTurtle('turtle')
zebra.pen = rg.Pen('red', 15)
zebra.speed = 40
zebra.forward(60)
zebra.right(37)
zebra.forward(55)
zebra.right(37)
zebra.forward(50)
zebra.right(37)
zebra.forward(45)
zebra.right(37)
zebra.forward(40)
zebra.right(37)
zebra.forward(35)

########################################################################
# DONE: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################
window.close_on_mouse_click()
