from os import name
from tkinter import *
import tkinter

mainFrame = Tk(baseName="jin")
mainFrame.config(background="pink")
mainFrame.geometry("1014x650")

Label1 = Label(mainFrame, text="LoginPage", background="#000fff000")
Label1.config(font=('Helvatical bold', 46))
Label1.place(x=423, y=20)


mainFrame.mainloop()
