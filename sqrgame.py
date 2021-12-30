#!/usr/bin/python3
from random import *
import requests
from tkinter import *
from PIL import ImageTk, Image 
root = Tk()

root.title("Sqaure Slots")

def shuffle_colors():
    my_canvas1['bg']= choice(colors_written)
    my_canvas2['bg']= choice(colors_written)
    my_canvas3['bg']= choice(colors_written)
    my_canvas4['bg']= choice(colors_written)
    print("button pushed")


colors_written = ['orange','blue','red','purple', 'green', 'yellow', 'black']


game_name = Label(root, bg="green", text= "Slot Squares", font="FreeMono 40",height=1, width=20)
game_name.grid(row=0, column=0, columnspan=2)

rand_color1 = choice(colors_written)
my_canvas1 = Canvas(root, bg=rand_color1, height= 200, width=200)
my_canvas1.grid(row=1, column=0)
print(rand_color1)

rand_color2 = choice(colors_written)
my_canvas2 = Canvas(root, bg=rand_color2, height= 200, width=200)
my_canvas2.grid(row=1, column=1)
print(rand_color2)


shuffle_button = Button(root, bg="green", text= "Space for Button", command=shuffle_colors,  font="FreeMono 10",height=5, width=20)
shuffle_button.grid(row=2, column=0, columnspan=2)

#lambda : shuffle_colors()
#This also works with the command key pair, but I don't understand it so I'll use shuffle colors.
#I remember in other contexts, the lambda was used because otherwise we couldn't pass anything in when we ran the funciton. 



rand_color3 = choice(colors_written)
my_canvas3 = Canvas(root, bg=rand_color3, height=200, width=200)
my_canvas3.grid(row=3, column=0)
print(rand_color3)

rand_color4 = choice(colors_written)
my_canvas4 = Canvas(root, bg=rand_color4, height=200, width=200)
my_canvas4.grid(row=3, column=1)
print(rand_color4)

#lambda : shuffle_colors()


root.mainloop()
