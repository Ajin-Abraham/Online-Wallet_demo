from os import name
from tkinter import *

# Main Frame config
mainFrame = Tk()
mainFrame.config(background="#212121")
mainFrame.geometry("1014x650")

# Header Config
Label1 = Label(mainFrame, text="LoginPage",
               background="#222831", foreground="#0D7377")
Label1.config(font=('Helvatical bold', 46))
Label1.place(x=380, y=30)

# usernmae style config
pic1 = PhotoImage(file="photos\\Username_pic.png")
upic = Label(image=pic1, background="#212121").place(x=180, y=245)

#
UnameLabel = Label(mainFrame, text="UserName",
                   background="#212121", foreground="#FF4C29")
UnameLabel.config(font=('Helvatical bold', 28))
UnameLabel.place(x=250, y=250)

# passWord style config
pic2 = PhotoImage(file="photos\\Password_pic.png")
ppic = Label(image=pic2, background="#212121").place(x=185, y=365)
#
passLabel = Label(mainFrame, text="Password",
                  background="#212121", foreground="#FF4C29")
passLabel.config(font=('Helvatical bold', 28))
passLabel.place(x=250, y=360)

mainFrame.mainloop()
