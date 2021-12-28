#!/usr/bin/python3
from random import *
import requests
from tkinter import *
from PIL import ImageTk, Image 
root = Tk()

colors_written = ['orange','blue','red','purple', 'green', 'yellow', 'black']
rand_color1 = choice(colors_written)
my_canvas1 = Canvas(root, bg=rand_color1, height= 200, width=200)
my_canvas1.grid(row=0, column=0)
print(rand_color1)

rand_color2 = choice(colors_written)
my_canvas2 = Canvas(root, bg=rand_color2, height= 200, width=200)
my_canvas2.grid(row=0, column=1)
print(rand_color2)

rand_color3 = choice(colors_written)
my_canvas3 = Canvas(root, bg=rand_color3, height=200, width=200)
my_canvas3.grid(row=1, column=1)
print(rand_color3)

rand_color4 = choice(colors_written)
my_canvas4 = Canvas(root, bg=rand_color4, height=200, width=200)
my_canvas4.grid(row=1, column=0)
print(rand_color4)

##testing pushing from pi3 to github

root.mainloop()
