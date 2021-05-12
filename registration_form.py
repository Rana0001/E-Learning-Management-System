from tkinter import *
from tkinter import messagebox


def form():
    #Creating new windows for registration form
    register_win = Toplevel()
    register_win.geometry("1366x736")
    register_win.title("Sign Up")
    register_win.iconbitmap("icon/title_icon.ico")

     #Defining fucntion for message and destroying registration windows
    def destroyinfo():
        messagebox.showinfo("Sign Up", "Registration Successful")
        register_win.withdraw()

    #Inserting Background image and resizing its height and width


    messagebox.showinfo("Login Information","Login Successful",parent =register_win)
    btn_exit = Button(register_win,text = "Destroy", command = destroyinfo)
    btn_exit.place(x = 5 , y =10)
    register_win.mainloop()

