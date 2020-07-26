# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:13:06 2020

@author: Raymart Ballesteros
"""
# Basic Animation in Python 3
# Following tutorials by TokyoEdTech on YouTube

import turtle
#import time  #sleep stops the program for num secs

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

# Register shapes/images
wn.register_shape("invader.gif")
wn.register_shape("invader2.gif")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("invader.gif")
        self.color("blue")
        self.frame = 0
        self.frames = ["invader.gif", "invader2.gif"]
        
    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])
    
        # set timer
        # sets a timer for 500 milliseconds and then calls function
        wn.ontimer(self.animate, 500)
        

player = Player()
player.animate()

player2 = Player()
player2.goto(-100, 0)
player2.animate()

player3 = Player()
player3.goto(0, 100)
player3.animate()

player4 = Player()
player4.goto(100, 0)
player4.animate()

player5 = Player()
player5.goto(0, -100)
player5.animate()


while True:
    wn.update()  # allows loop to break and animation to update
    print("Main Loop")


wn.mainloop()   # keeps window open
# raises tutle.Terminator error; not really an error

