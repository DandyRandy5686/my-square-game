#!/usr/bin/python3
from random import *
import requests
from tkinter import *
from PIL import ImageTk, Image 
root = Tk()

root.title("Sqaure Slots")

score = 0

def shuffle_colors():
    global score
    global user_display
    to_display = ""
    small_winner = False
    my_canvas1['bg']= choice(colors_written)
    my_canvas2['bg']= choice(colors_written)
    my_canvas3['bg']= choice(colors_written)
    my_canvas4['bg']= choice(colors_written)
    print("button pushed")
    if my_canvas1['bg'] == my_canvas2['bg'] == my_canvas3['bg'] == my_canvas4['bg']:
        to_display= "All four squares match! 1000 points!!"
        score = score + 1000
        big_winner = True
    elif my_canvas1['bg'] == my_canvas2['bg'] == my_canvas3['bg']: 
        to_display ="Squares 1, 2, and 3 match. 100 POINTS!"
        score = score + 100
        big_winner = True
    elif my_canvas1['bg'] == my_canvas3['bg'] == my_canvas4['bg']: 
        to_display="Squares 1, 3, and 4 match. 100 POINTS!"
        score = score + 100
        big_winner = True
    elif my_canvas1['bg'] == my_canvas2['bg'] == my_canvas4['bg']: 
        to_display="Squares 1, 2, and 4 match. 100 POINTS!"
        score = score + 100
        big_winner = True
    elif my_canvas2['bg'] == my_canvas3['bg'] == my_canvas4['bg']: 
        to_display="Squares 1, 2, and 3 match. 100 POINTS!"
        score = score + 100
        big_winner = True
    elif my_canvas1['bg'] == my_canvas2['bg'] and my_canvas3['bg'] == my_canvas4['bg']:
        to_display="Doubles! 500 points"
        score = score + 500
        big_winner = True
    elif my_canvas1['bg'] == my_canvas4['bg'] and my_canvas2['bg'] == my_canvas3['bg']:
        to_display="Doubles! 500 points"
        score = score + 500
        big_winner = True
    elif my_canvas1['bg'] == my_canvas3['bg'] and my_canvas2['bg'] == my_canvas4['bg']:
        to_display="Doubles! 500 points"
        score = score + 500
        big_winner = True        
        
    
    else:
        big_winner = False
        
       
    
    if my_canvas1['bg'] == my_canvas2['bg'] and big_winner == False:
        to_display="Squares 1 and 2 match. 10 POINTS for you!"
        score = score + 10
        small_winner = True
    if my_canvas1['bg'] == my_canvas3['bg'] and big_winner == False:
        to_display="Squares 1 and 3 match. 10 POINTS for you!"
        score = score + 10
        small_winner = True
    if my_canvas1['bg'] == my_canvas4['bg'] and big_winner == False:
        to_display="Squares 1 and 4 match. 10 POINTS for you!"
        score = score + 10
        small_winner = True
    if my_canvas2['bg'] == my_canvas3['bg'] and big_winner == False:
        to_display="Squares 2 and 3 match. 10 POINTS for you!"
        score = score + 10
        small_winner = True
    if my_canvas2['bg'] == my_canvas4['bg'] and big_winner == False:
        to_display="Squares 2 and 4 match. 10 POINTS for you!"
        score = score + 10
        small_winner = True
    if my_canvas3['bg'] == my_canvas4['bg'] and big_winner == False:
        to_display ="Squares 3 and 4 match. 10 POINTS for you!"
        score = score + 10
        small_winner = True
    
#     my_canvas1['bg'] == my_canvas2['bg'] == my_canvas3['bg']    
    
    if small_winner == False and big_winner == False:
        to_display ="No points this turn"      
        
    user_display['text']= to_display
    
    score_label['text']=  ("Your \n score \n is \n" + str(score)) 

colors_written = ['orange','blue','red','purple', 'green', 'yellow', 'black']



game_name = Label(root, bg="green", text= "Slot Squares", font="FreeMono 40",height=1, width=45)
game_name.grid(row=0, column=0, columnspan=2)

rand_color1 = choice(colors_written)
my_canvas1 = Canvas(root, bg=rand_color1, height= 200, width=200)
my_canvas1.grid(row=1, column=0)
print(rand_color1)

rand_color2 = choice(colors_written)
my_canvas2 = Canvas(root, bg=rand_color2, height= 200, width=200)
my_canvas2.grid(row=1, column=1)
print(rand_color2)


shuffle_button = Button(root, bg="green", text= "SHUFFLE", command=shuffle_colors,  font="FreeMono 20",height=5, width=30)
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

user_display = Label(root, text="The user has: \n 0 POINTS", font="FreeMono 40",  bg="black", fg="green", height=3, width=45)
user_display.grid(row=4, column=0, columnspan=2)

score_label = Label(root, text="The user \n has: \n 0 POINTS", font="FreeMono 40",  bg="black", fg="green", height=15, width=10)
score_label.grid(row=0, column=3, rowspan=4)

#lambda : shuffle_colors()


root.mainloop()
