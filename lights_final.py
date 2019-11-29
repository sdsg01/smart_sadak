from tkinter import *
import tkinter as tk
import sys, tkinter
from database import *
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=950)
canvas.pack()
canvas.create_rectangle(75, 25, 425, 925, fill="black")


def red(a):
	canvas.create_oval(125, 50, 375, 300, fill="red")
	canvas.create_oval(125, 350, 375, 600, fill="white")
	canvas.create_oval(125, 650, 375, 900, fill="white")
	time.sleep(a)
	light = "red"
	ref.update({'Traffic_light': light})
	tk.update()

def amber(a):
	canvas.create_oval(125, 50, 375, 300, fill="white")
	canvas.create_oval(125, 350, 375, 600, fill="yellow")
	canvas.create_oval(125, 650, 375, 900, fill="white")
	time.sleep(a)
	light = "yellow"
	ref.update({'Traffic_light': light})
	tk.update()

def green(a):
	canvas.create_oval(125, 50, 375, 300, fill="white")
	canvas.create_oval(125, 350, 375, 600, fill="white")
	canvas.create_oval(125, 650, 375, 900, fill="forestgreen")
	time.sleep(a)
	light = "green"
	ref.update({'Traffic_light': light})
	tk.update()

def lights():
	canvas.create_oval(125, 50, 375, 300, fill="white")
	canvas.create_oval(125, 350, 375, 600, fill="white")
	canvas.create_oval(125, 650, 375, 900, fill="white")

while True:
	lights()
	red(3)
	green(3)
	amber(3)

#tk.mainloop()



#while True:
	#tk.update_idletasks()
	#tk.update()




