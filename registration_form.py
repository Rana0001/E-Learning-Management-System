from tkinter import *
from tkinter import messagebox


def form():
    register_win = Toplevel()
    register_win.geometry("1366x736")
    register_win.title("Sign Up")
    register_win.iconbitmap("icon/title_icon.ico")
    def destroyinfo():
        messagebox.showinfo("Sign Up", "Registration Successful")
        register_win.withdraw()
    messagebox.showinfo("Login Information","Login Successful",parent =register_win)
    btn_exit = Button(register_win,text = "Destroy", command = destroyinfo)
    btn_exit.place(x = 5 , y =10)
    register_win.mainloop()

