# -----------------------------
#           Lesson 2
# -----------------------------
# External modules

# External modules are made by other programmers
# They give us a huge amount of extra functionality
# For example, game development, data analysis, machine learning,
# graphics user interfaces etc are all functionalities we get from external modules
# These modules are imported like the standard modules. However, we first need to install them. This usually happens in the powershell or the terminal
# The powershell(Windows) and the terminal (MacOs) are command line interfaces
# They are a way to interact with your computer by writing text

# install the certain module
# pip install {name}

# show installed modules
# pip list

# uninstall certain module
# pip uninstall {name}


import pyautogui
from time import sleep

# sleep(1)
# pyautogui.write('This is written by a computer', interval = 0.25)


print('\n'*2)
# -----------------------------
#           Exercise
# -----------------------------
# Create a graph from any of the examples below
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

# we are not importing all library, we just getting one sub part of it (library.sub_part)
import matplotlib.pyplot as plt

# we only specified y-axis, x-axis is deafult = [0, 1, 2, 3]
# plt.plot([1, 2, 3, 4])

# first x-axis then y-axis
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.ylabel('some numbers for the y-axis')
# plt.xlabel('some numbers for the x-axis')
# plt.show()

# thrid argument indicate color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string.
# The default format string is 'b-', which is a solid blue line. In our case "ro" r - red, o - circle line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# set the limit of axis [start-x, end-x, start-y, end-y]
plt.axis([0, 6, 0, 20])
plt.show()

