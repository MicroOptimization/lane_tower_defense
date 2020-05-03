"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import tkinter as tk
from tkinter import Canvas

root = tk.Tk()

window_width = 1000
window_height = 600

canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack()
"""
#Draws 20 x 20px square
canvas.create_line(20, 20, 20, 40)
canvas.create_line(20, 40, 40, 40)
canvas.create_line(40, 40, 40, 20)
canvas.create_line(40, 20, 20, 20)
"""



def draw_square(start_x, start_y, side_length, canvas):
    canvas.create_line(start_x, start_y, start_x, start_y + side_length)
    canvas.create_line(start_x, start_y + side_length, start_x + side_length, start_y + side_length)
    canvas.create_line(start_x + side_length, start_y + side_length, start_x + side_length, start_y)
    canvas.create_line(start_x + side_length, start_y, start_x, start_y)

scale_coeff = 8

side_length = window_height / scale_coeff
start_x = 10
start_y = 10

#draw_square(start_x, start_y, side_length, canvas)

grid_height = 6
grid_width = 9

for j in range(grid_width):
    for i in range(grid_height):
        #Start point
        x1 = 10 + (side_length * j)
        y1 = 80 + (side_length * i)
        
        draw_square(x1, y1, side_length, canvas)


while True:
    root.update_idletasks()
    root.update()