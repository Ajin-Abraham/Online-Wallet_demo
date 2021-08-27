import psycopg2
import tkinter as tk
from tkinter import messagebox

username = ""
password = ""


def auth():

    username = unameField.get()
    password = passField.get()

    if(username == "" or password == ""):
        messagebox.showerror(
            "Error !", "Please Enter Valid Username or Pass Word !")
    else:

        try:
            db_name = "gbgesjnp"
            db_user = "gbgesjnp"
            db_pass = "oeoPIH_GSeWRcCC6CBB_vQEOGvEnt9Lx"
            db_host = "arjuna.db.elephantsql.com"
            db_port = "5432"

            print(passField)
            conn = psycopg2.connect(database=db_name,
                                    user=db_user,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port
                                    )
            cur = conn.cursor()
            cur.execute
            conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", "    Connection Error   ")
            loop_number = len(username) if len(
                username) >= len(password) else len(password)
            for i in range(0, loop_number):
                passField.delete(0)
                unameField.delete(0)


# Main Frame config
mainFrame = tk.Tk()
mainFrame.config(background="#FE9898")
mainFrame.geometry("1150x650")
mainFrame.title("FiT wallet")
mainFrame.resizable(0, 0)
textLabel1 = tk.Label(mainFrame, text="Welcome Back ,",
                      background="#FE9898", foreground="#FFFFFF")
textLabel1.config(font=('Bahnschrift SemiBold', 46))
textLabel1.place(x=100, y=100)

textLabel2 = tk.Label(mainFrame, text="Sign in to continue access",
                      background="#FE9898", foreground="#FFFFFF")
textLabel2.config(font=('Bahnschrift Light SemiCondensed', 26))
textLabel2.place(x=100, y=200)

textLabel3 = tk.Label(mainFrame, text="___________________   www.FiTbank.com",
                      background="#FE9898", foreground="#FFFFFF")
textLabel3.config(font=('Bahnschrift Light SemiCondensed', 26))
textLabel3.place(x=100, y=500)

# secondFrame for Labels
frame = tk.Frame(mainFrame, width=600, height=650, background="#F5F5F5")
frame.place(x=650, y=0)

# icon config
pic1 = tk.PhotoImage(file="photos\\Username_pic.png")
upic = tk.Label(frame, image=pic1, background="#F5F5F5").place(x=130, y=255)
pic2 = tk.PhotoImage(file="photos\\Password_pic.png")
ppic = tk.Label(frame, image=pic2, background="#F5F5F5").place(x=130, y=365)
pic3 = tk.PhotoImage(file="photos\padlock.png")
mpic = tk.Label(frame, image=pic3, background="#F5F5F5").place(x=320, y=100)

# Header Config
Label1 = tk.Label(frame, text="Sign In",
                  background="#F5F5F5", foreground="#000000")
Label1.config(font=('Arial Rounded MT Bold', 46))
Label1.place(x=100, y=100)

# textField Config
unameField = tk.Entry(frame, font=('Helvatical bold', 20), background="#D3D3D3",
                      foreground="#BFA2DB")
unameField.place(x=200, y=250, height=50, width=250)
passField = tk.Entry(frame, font=('Helvatical bold', 30), show="*", background="#D3D3D3",
                     foreground="#E5FBB8")
passField.place(x=200, y=360, height=50, width=250)


submitButton = tk.Button(frame, text='Sumbit', font=('Bahnschrift SemiBold', 20),
                         background='#BFA2DB', height=1, width=10, command=auth)
submitButton.place(x=250, y=450)

mainFrame.mainloop()
