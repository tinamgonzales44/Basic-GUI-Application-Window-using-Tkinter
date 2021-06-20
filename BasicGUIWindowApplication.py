#Just Plain GUI Window

from tkinter import * #import tkinter module
window = Tk() #call tkinter function for GUI window

window.title("Hello Python") #Title of the Message Window // Will appear on the Top // title widget
window.geometry('350x200+10+20') #Defines the width, height and coordinates of the top left corner of the frame as below in pixels | (width x height + XPOS + YPOS) //geometry widget

window.mainloop() #event listening loop // it waits for other events such as radio buttons et al // will close on x // main loop widget // needed for the GUI to pop-up

""" 
Sources: 

https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

"""

