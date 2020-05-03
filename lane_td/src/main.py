"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import tkinter as tk
from tkinter import Canvas
import util

root = tk.Tk()

window_width = 1000
window_height = 600

canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack()
root.resizable(False, False)

#scale_coeff = 8
#side_length = window_height / scale_coeff
side_length = 75

print(side_length)
grid_height = 6
grid_width = 9

for j in range(grid_width):
    for i in range(grid_height):
        #Start point
        x1 = 10 + (side_length * j)
        y1 = 80 + (side_length * i)
        
        util.draw_square(x1, y1, side_length, canvas)


while True:
    root.update_idletasks()
    root.update()






















    
    
    
    