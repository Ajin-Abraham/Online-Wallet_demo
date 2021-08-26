from os import name
from tkinter import *

if __name__ == "__main__":

    # Main Frame config
    mainFrame = Tk()
    mainFrame.config(background="#FE9898")
    mainFrame.geometry("1150x650")
    mainFrame.title("FiT wallet")
    mainFrame.resizable(0, 0)

    textLabel1 = Label(mainFrame, text="Welcome Back ,",
                       background="#FE9898", foreground="#FFFFFF")
    textLabel1.config(font=('Bahnschrift SemiBold', 46))
    textLabel1.place(x=100, y=100)

    textLabel2 = Label(mainFrame, text="Sign in to continue access",
                       background="#FE9898", foreground="#FFFFFF")
    textLabel2.config(font=('Bahnschrift Light SemiCondensed', 26))
    textLabel2.place(x=100, y=200)

    textLabel3 = Label(mainFrame, text="___________________   www.FiTbank.com",
                       background="#FE9898", foreground="#FFFFFF")
    textLabel3.config(font=('Bahnschrift Light SemiCondensed', 26))
    textLabel3.place(x=100, y=500)
    # Frame for Labels
    frame = Frame(mainFrame, width=600, height=650, background="#F5F5F5")
    frame.place(x=650, y=0)

    pic3 = PhotoImage(file="photos\padlock.png")
    mpic = Label(frame, image=pic3, background="#F5F5F5").place(x=320, y=100)
    # Header Config
    Label1 = Label(frame, text="Sign In",
                   background="#F5F5F5", foreground="#000000")
    Label1.config(font=('Arial Rounded MT Bold', 46))
    Label1.place(x=100, y=100)

    # unameField config
    pic1 = PhotoImage(file="photos\\Username_pic.png")
    upic = Label(frame, image=pic1, background="#F5F5F5").place(x=130, y=255)
    unameField = Entry(frame, font=('Helvatical bold', 20), background="#D3D3D3",
                       foreground="#BFA2DB").place(x=200, y=250, height=50, width=250)

    # passwordField config
    pic2 = PhotoImage(file="photos\\Password_pic.png")
    ppic = Label(frame, image=pic2, background="#F5F5F5").place(x=130, y=365)
    passField = Entry(frame, font=('Helvatical bold', 30), show="*", background="#D3D3D3",
                      foreground="#E5FBB8").place(x=200, y=360, height=50, width=250)

    submitButton = Button(frame, text='Sumbit', font=('Bahnschrift SemiBold', 20),
                          background='#BFA2DB', height=1, width=10)
    submitButton.place(x=250, y=450)

    mainFrame.mainloop()
