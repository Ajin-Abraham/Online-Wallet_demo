from os import name
from tkinter import *
from functools import partial

# Main Frame config
mainFrame = Tk()
mainFrame.config(background="#212121")
mainFrame.geometry("1014x650")
mainFrame.title("Sign In")

# Header Config
Label1 = Label(mainFrame, text="Sign In",
               background="#222831", foreground="#0D7377")
Label1.config(font=('Helvatical bold', 46))
Label1.place(x=380, y=30)

pic1 = PhotoImage(file="photos\\Username_pic.png")
upic = Label(image=pic1, background="#212121").place(x=180, y=245)
# usernmaeLabel config
UnameLabel = Label(mainFrame, text="UserName",
                   background="#212121", foreground="#FF4C29")
UnameLabel.config(font=('Helvatical bold', 28))
UnameLabel.place(x=250, y=250)

# unameField config
unameField = Entry(mainFrame, font=('Helvatical bold', 20), background="#334756",
                   foreground="#F7F6F2").place(x=500, y=250, height=50, width=200)


pic2 = PhotoImage(file="photos\\Password_pic.png")
ppic = Label(image=pic2, background="#212121").place(x=185, y=365)
# passWord style config
passLabel = Label(mainFrame, text="Password",
                  background="#212121", foreground="#FF4C29")
passLabel.config(font=('Helvatical bold', 28))
passLabel.place(x=250, y=360)

# passwordField config
passField = Entry(mainFrame, font=('Helvatical bold', 30), show="*", background="#334756",
                  foreground="#F7F6F2").place(x=500, y=360, height=50, width=200)


mainFrame.mainloop()
