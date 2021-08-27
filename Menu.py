from tkinter import *


def menu(uname):
    #=====mainFrame config=======#
    menuFrame = Tk()
    menuFrame.config(background="#D8A7B1")
    menuFrame.geometry("700x700")
    menuFrame.title("FiT wallet")
    menuFrame.resizable(0, 0)

    pic0 = PhotoImage(file="photos\\Tab_icon.png")
    menuFrame.iconphoto(True, pic0)
    header = f'Welcome Back ,{uname}'
    headerLabel = Label(menuFrame, text=header,
                        background="#DEDEDE", foreground="#000000")
    headerLabel.config(font=('Bahnschrift', 32))
    headerLabel.place(x=0, y=20)

    #____________pictures_________#
    pic1 = PhotoImage(file="photos\\withdrawal.png")
    pic2 = PhotoImage(file="photos\\deposit.png")
    pic3 = PhotoImage(file="photos\\balance.png")
    pic4 = PhotoImage(file="photos\\exit.png")

    #++++++++++BUTTONS++++++++++#
    withdrawButton = Button(menuFrame, text='WITHDRAWAL', image=pic1,
                            background='#F5F5F5', height=150, width=150)
    withdrawButton.place(x=140, y=150)
    depositButton = Button(menuFrame, text='deposit', image=pic2,
                           background='#F5F5F5', height=150, width=150)
    depositButton.place(x=370, y=150)
    balanceButton = Button(menuFrame, text='deposit', image=pic3,
                           background='#F5F5F5', height=150, width=150)
    balanceButton.place(x=140, y=450)
    exitButton = Button(menuFrame, text='deposit', image=pic4,
                        background='#F5F5F5', height=150, width=150)
    exitButton.place(x=370, y=450)

    #=================Labels==============#
    menuFrame.mainloop


def main(username):
    uname = username
    menu(uname)
