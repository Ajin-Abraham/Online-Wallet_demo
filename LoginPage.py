import psycopg2
from tkinter import *
from tkinter import messagebox
#**********our package**********#
from registerAuth import registerDb


def gotoLoginPage0():
    registerFrame.destroy()
    loginpageMain()


def gotoRegister():
    mainFrame.destroy()
    registerloginpageMain()

#==========================================================  Login  ===============================================================#
#==========================================================  Page   ===============================================================#
#==========================================================  Config ===============================================================#


def auth():

    username = unameField.get()
    password = passField.get()
    loop_number = 0

    if(username == "" or password == ""):
        messagebox.showerror(
            "Error !", "Please Enter Valid Username or Pass Word !")
    else:

        try:
            db_name = "euwpundj"
            db_user = "euwpundj"
            db_pass = "7qn7J2u4TvroHViI889U2pMnOopIr1S1"
            db_host = "rosie.db.elephantsql.com"
            db_port = "5432"
            conn = psycopg2.connect(database=db_name,
                                    user=db_user,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port
                                    )
            cur = conn.cursor()
            cur.execute(
                "select * from details where username=%s and password=%s", (username, password))
            res = cur.fetchone()
            loop_number = len(username) if len(
                username) >= len(password) else len(password)
            if res == None:
                messagebox.showerror("Error", "Please enter valid field")
                for i in range(0, loop_number):
                    passField.delete(0)
                    unameField.delete(0)
            else:
                messagebox.showinfo(
                    "Success", "               Welcome               ")
                mainFrame.destroy()
                menu(username)
            conn.commit()

        except Exception as e:
            messagebox.showerror("Error", "Database Error ")
            for i in range(0, loop_number):
                passField.delete(0)
                unameField.delete(0)

        finally:
            conn.close()


def loginpageMain():
    global mainFrame
    mainFrame = Tk()
    mainFrame.config(background="#D8A7B1")
    mainFrame.geometry("1150x650")
    mainFrame.title("FiTbank")
    mainFrame.resizable(0, 0)

    pic0 = PhotoImage(file="photos\\Tab_icon.png")
    mainFrame.iconphoto(True, pic0)

    textLabel1 = Label(mainFrame, text="Welcome Back ,",
                       background="#D8A7B1", foreground="#FFFFFF")
    textLabel1.config(font=('Bahnschrift SemiBold', 46))
    textLabel1.place(x=100, y=100)

    textLabel2 = Label(mainFrame, text="Sign in to continue access",
                       background="#D8A7B1", foreground="#FFFFFF")
    textLabel2.config(font=('Bahnschrift Light SemiCondensed', 26))
    textLabel2.place(x=100, y=200)

    textLabel3 = Label(mainFrame, text="___________________   www.FiTbank.com",
                       background="#D8A7B1", foreground="#FFFFFF")
    textLabel3.config(font=('Bahnschrift Light SemiCondensed', 26))
    textLabel3.place(x=100, y=500)

    # secondFrame for Labels
    frame = Frame(mainFrame, width=600, height=650, background="#FFFFFF")
    frame.place(x=650, y=0)

    # icon config
    pic1 = PhotoImage(file="photos\\Username_pic.png")
    upic = Label(frame, image=pic1, background="#FFFFFF").place(x=130, y=255)
    pic2 = PhotoImage(file="photos\\Password_pic.png")
    ppic = Label(frame, image=pic2, background="#FFFFFF").place(x=130, y=365)
    pic3 = PhotoImage(file="photos\\padlock.png")
    mpic = Label(frame, image=pic3, background="#FFFFFF").place(x=320, y=100)

    # Header Config
    Label1 = Label(frame, text="Sign In",
                   background="#FFFFFF", foreground="#000000")
    Label1.config(font=('Arial Rounded MT Bold', 46))
    Label1.place(x=100, y=100)

    # textField Config
    global unameField
    unameField = Entry(frame, font=('Helvatical bold', 20), background="#D3D3D3",
                       foreground="#000000")
    unameField.place(x=200, y=250, height=50, width=250)
    global passField
    passField = Entry(frame, font=('Helvatical bold', 30), show="•", background="#D3D3D3",
                      foreground="#000000")
    passField.place(x=200, y=360, height=50, width=250)

    signinButton = Button(frame, text='Sign in', font=('Bahnschrift SemiBold', 20),
                          background='#BFA2DB', height=1, width=10, command=auth)
    signinButton.place(x=250, y=420)

    orLabel = Label(frame, text="or",
                    background="#FFFFFF", foreground="#000000")
    orLabel.config(font=('Bahnschrift SemiBold', 18))
    orLabel.place(x=310, y=480)

    signupButton = Button(frame, text='Sign Up', font=('Bahnschrift SemiBold', 20),
                          background='#BFA2DB', height=1, width=10, command=gotoRegister)
    signupButton.place(x=250, y=520)

    mainFrame.mainloop()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++  Register +++++++++++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++   Page    +++++++++++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++  Config   +++++++++++++++++++++++++++++++++++++++++++++++#


def passtoRegisterAuth():
    username = rF1.get()
    flag = True
    email = rF3.get()
    age = rF2.get()
    ph = rF4.get()
    password = rF5.get()
    password2 = rF6.get()
    # $$$$$$$conditionCheck for register

    if (username == ""):
        messagebox.showerror(
            "Error !", "Please Enter Username")
        registerFrame.destroy()
        loginpageMain()
    if(age == ""):
        messagebox.showerror(
            "Error !", "Enter your age")
        registerFrame.destroy()
        loginpageMain()
    if(age != ""):
        if(int(age) < 18):
            messagebox.showerror(
                "Error !", "You are not eligable for account")
            registerFrame.destroy()
            loginpageMain()

    if (password == ""):
        messagebox.showerror(
            "Error !", "Please Enter Password")
        registerFrame.destroy()
        loginpageMain()
    if(password != password2):
        messagebox.showerror(
            "Error !", "Please Enter valid Password")
        registerFrame.destroy()
        loginpageMain()

    check = registerDb(username, email,
                       int(age), ph, password)
    check = int(check)
    if(check == 1):
        registerFrame.destroy()
        loginpageMain()


def registerloginpageMain():
    global registerFrame
    registerFrame = Tk()
    registerFrame.config(background="#D8A7B1")
    registerFrame.geometry("1150x650")
    registerFrame.title("FiT wallet")
    registerFrame.resizable(0, 0)

    textLabel1 = Label(registerFrame, text="FiTbank",
                       background="#FFFFFF", foreground="#000000")
    textLabel1.config(font=('Cascadia Code', 35), justify=LEFT)
    textLabel1.place(x=0, y=0, height=61, width=1150)

    textLabel2 = Label(registerFrame, text="Registration",
                       background="#D8A7B1", foreground="#000000")
    textLabel2.config(font=('Bahnschrift SemiBold', 40))
    textLabel2.place(x=15, y=61)

    textLabel3 = Label(registerFrame, text="Join the world's most secure Online Payment Platform!",
                       background="#D8A7B1", foreground="#000000")
    textLabel3.config(font=('Arial', 18), justify='right')
    textLabel3.place(x=15, y=140,)

    #======================LABELS============#
    Label1 = Label(registerFrame, text="Username:",
                   background='#D8A7B1', foreground="#000000")
    Label1.config(font=('Bahnschrift SemiBold', 30))
    Label1.place(x=15, y=190)

    Label2 = Label(registerFrame, text="Age:",
                   background='#D8A7B1', foreground="#000000")
    Label2.config(font=('Bahnschrift SemiBold', 30))
    Label2.place(x=555, y=190)

    Label3 = Label(registerFrame, text="E-mail:",
                   background='#D8A7B1', foreground="#000000")
    Label3.config(font=('Bahnschrift SemiBold', 30))
    Label3.place(x=15, y=290)

    Label4 = Label(registerFrame, text="Phone Number:",
                   background='#D8A7B1', foreground="#000000")
    Label4.config(font=('Bahnschrift SemiBold', 30))
    Label4.place(x=555, y=290)

    Label5 = Label(registerFrame, text="Password:",
                   background='#D8A7B1', foreground="#000000")
    Label5.config(font=('Bahnschrift SemiBold', 30))
    Label5.place(x=15, y=390)

    Label6 = Label(registerFrame, text="Retype Password:",
                   background='#D8A7B1', foreground="#000000")
    Label6.config(font=('Bahnschrift SemiBold', 30))
    Label6.place(x=555, y=390)

    #+++++++++++++++TextFields++++++++++++#
    global rF1
    global rF2
    global rF3
    global rF4
    global rF5
    global rF6
    rF1 = Entry(registerFrame, font=('Helvatical bold', 20), background="#FFFFFF",
                foreground="#000000")
    rF1.place(x=225, y=190, height=50, width=250)

    rF2 = Entry(registerFrame, font=('Helvatical bold', 20), background="#FFFFFF",
                foreground="#000000")
    rF2.place(x=890, y=195, height=50, width=250)

    rF3 = Entry(registerFrame, font=('Helvatical bold', 20), background="#FFFFFF",
                foreground="#000000")
    rF3.place(x=225, y=290, height=50, width=250)

    rF4 = Entry(registerFrame, font=('Helvatical bold', 20), background="#FFFFFF",
                foreground="#000000")
    rF4.place(x=890, y=295, height=50, width=250)

    rF5 = Entry(registerFrame, font=('Helvatical bold', 20), background="#FFFFFF", show="•",
                foreground="#000000")
    rF5.place(x=225, y=390, height=50, width=250)

    rF6 = Entry(registerFrame, font=('Helvatical bold', 20), background="#FFFFFF",
                foreground="#000000")
    rF6.place(x=890, y=390, height=50, width=250)

    #==========Buttons=============#
    pic1 = PhotoImage(file="photos\\back.png")
    submitButton = Button(registerFrame, text='Submit', font=('Bahnschrift SemiBold', 20),
                          background='#BFA2DB', height=1, width=10, activebackground="pink", activeforeground="red", command=passtoRegisterAuth)
    submitButton.place(x=450, y=480)

    returnButton = Button(registerFrame, image=pic1,
                          background='#BFA2DB', height=45, width=100, command=gotoLoginPage0)
    returnButton.place(x=50, y=550)

    registerFrame.mainloop()

#------------------------------------------------------   Menu   ---------------------------------------------#
#------------------------------------------------------   Page   ---------------------------------------------#
#------------------------------------------------------   config ---------------------------------------------#


def gotoLoginPage1():
    menuFrame.destroy()
    loginpageMain()


def menu(uname):
    #=====mainFrame config=======#
    global menuFrame
    menuFrame = Tk()
    menuFrame.config(background="#D8A7B1")
    menuFrame.geometry("700x700")
    menuFrame.title("FiTbank")
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

    #----------Method-----------#

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
                        background='#F5F5F5', height=150, width=150, command=gotoLoginPage1)
    exitButton.place(x=370, y=450)

    #++++++++++++Label config+++++++++++#
    wLabel = Label(menuFrame, text="WITHDRAW",
                   background="#F5F5F5", foreground="#000000")
    wLabel.config(font=('Arial Narrow', 23))
    wLabel.place(x=140, y=320, width=157)

    dLabel = Label(menuFrame, text="DEPOSIT",
                   background="#F5F5F5", foreground="#000000")
    dLabel.config(font=('Arial Narrow', 23))
    dLabel.place(x=370, y=320, width=157)
    bLabel = Label(menuFrame, text="BALANCE",
                   background="#F5F5F5", foreground="#000000")
    bLabel.config(font=('Arial Narrow', 23))
    bLabel.place(x=140, y=620, width=157)
    eLabel = Label(menuFrame, text="EXIT",
                   background="#F5F5F5", foreground="#000000")
    eLabel.config(font=('Arial Narrow', 23))
    eLabel.place(x=370, y=620, width=157)

    menuFrame.mainloop()


loginpageMain()

#
