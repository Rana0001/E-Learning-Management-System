# Import tkinter,image and sqlite 3
from registration_form import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# import home

# Creating Tkinter Windows
root = Tk()
root.title("Self Learner")
root.geometry("1290x1080")
root.iconbitmap("icon/title_icon.ico")


# Defining funtion for forget password
def forget():
    lost = Toplevel()
    lost.title("Forget your password?")
    lost.iconbitmap("icon/title_icon.ico")
    lost.geometry("600x600")
    lost.resizable(0, 0)

    # Defining function for show password
    def show_pass():
        conn = sqlite3.connect("registration.db")
        c = conn.cursor()
        record_files = uid_user.get()
        c.execute("SELECT *,oid FROM signup_form")
        data = c.fetchall()
        for data_user in data:
            if str(data_user[2]) == forget_user.get() and str(data_user[-1]) == uid_user.get():
                try:
                    messagebox.showinfo("Notice", f"Your password is {data_user[3]}")
                    lost.withdraw()
                    return 0
                except:
                    pass
        messagebox.showinfo("Try Again!", "Please Entered Correct UserName and UID...", parent=lost)

    lost_image = Image.open("images/forget.png")
    lost_resized = lost_image.resize((600, 700), Image.ADAPTIVE)
    lost_real = ImageTk.PhotoImage(lost_resized)
    lost_image_label = Label(lost, image=lost_real, bd=0)
    lost_image_label.place(x=0, y=0, relheight=1, relwidth=1)
    forget_label = Label(lost, text="Enter your username:", bg="white", fg="black", bd=0, font=("Ariel", 11, "bold"))
    forget_label.place(x=265, y=254)
    uid_label = Label(lost, text="  Enter your uid: ", bg="white", fg="black", bd=0, font=("Ariel", 11, "bold"))
    uid_label.place(x=255, y=315)
    forget_user = Entry(lost, width="27", bd=2, font=("Ariel", 10))
    forget_user.place(x=260, y=280, height=30)
    uid_user = Entry(lost, width="27", bd=2, font=("Ariel", 10))
    uid_user.place(x=260, y=340, height=30)
    show_password = Button(lost, command=show_pass, text="Show Password", bg="#fad300", width=18, fg="#ffffff",
                           activebackground="#fad300", activeforeground="#ffffff", relief=RAISED)
    show_password.place(x=285, y=408)
    lost.mainloop()


# Adding Background Image
bg_image = Image.open("images/background.png")
bg_image_resized = bg_image.resize((1366, 768), Image.ADAPTIVE)
resized = ImageTk.PhotoImage(bg_image_resized)
bgImg = Label(root, image=resized)
bgImg.place(x=0, y=0, relheight=1, relwidth=1)
frame = Frame(root, width=425, height=500, bg="#b7e3f0")
frame.place(x=465, y=140)
label = Label(root, text="Login", font=("Ariel", 20, "bold italic"), fg="#133342", bg="#b7e3f0")
label.place(x=625, y=200)

# Adding Icon
user_icon = ImageTk.PhotoImage(Image.open("icon/user.png"))
user_icon_label = Label(root, image=user_icon, bg="#b7e3f0")
user_icon_label.place(x=595, y=70)

# Adding Widgets and Field
username_label = Label(root, text="Username/Email:", border=0, font=("Ariel", 13, "bold"), fg="#133342", bg="#b7e3f0")
username_label.place(x=500, y=260)
username_field = Entry(root, width=35, border=0, fg="#133342", bg="#b7e3f0", font=("Ariel", 12))
username_field.place(x=540, y=295)
Frame(root, width=300, borderwidth=0, bg="black").place(x=540, y=315)
password_label = Label(root, text="Password:", border=0, font=("Ariel", 13, "bold"), fg="#133342", bg="#b7e3f0")
password_label.place(x=500, y=340)
password_field = Entry(root, width=35, bg="#b7e3f0", border=0, fg="#133342", font=("Ariel", 12), show="*")
password_field.place(x=540, y=375)
Frame(root, width=300, borderwidth=0, bg="black").place(x=540, y=395)

# Adding Icons of username and password
username_icon = PhotoImage(file="icon/username.png")
username_icon_label = Label(root, image=username_icon, bg="#b7e3f0", fg="#133342")
username_icon_label.place(x=500, y=285)
password_icon = PhotoImage(file="icon/password.png")
password_icon_label = Label(root, image=password_icon, bg="#b7e3f0", fg="#133342")
password_icon_label.place(x=500, y=365)


# Creating Home Windows
def login():
    conn = sqlite3.connect("registration.db")
    c = conn.cursor()
    c.execute('SELECT *,oid FROM signup_form')
    data = c.fetchall()
    for user_data in data:
        if str(user_data[2]) == username_field.get() and str(user_data[3]) == password_field.get():
            try:
                messagebox.showinfo("      Login        ", "Login Successful")
                root.withdraw()
                return home.main()

            finally:
                pass
    messagebox.showinfo("    Login     ", "Please! Check your email and password.", parent=root)


# Adding Sign in button and registration form
btn_sign_in = Button(root, command=login, text="Log in", width=15, bd=3, relief=RAISED, font=("Ariel", 10, "bold"),
                     bg="#f98135", fg="#133342", activebackground="#f98135", activeforeground="#133342")
btn_sign_in.place(x=615, y=450)
btn_forget = Button(root, command=forget, text="Forget Password?", font=("Ariel", 10, "bold"), bg="#b7e3f0",
                    fg="#133342",
                    borderwidth=0, relief=RIDGE, activebackground="#b7e3f0", activeforeground="#133342")
btn_forget.place(x=500, y=420)

btn_signup = Button(root, command=form, text="Create a new account", font=("Ariel", 10, "bold"), bg="#b7e3f0",
                    fg="#133342", borderwidth=0, relief=RIDGE, activebackground="#b7e3f0", activeforeground="#133342")
btn_signup.place(x=500, y=490)

# Adding icon of facebook,twitter, instagram and linkedin
facebook_icon = PhotoImage(file="social_icon/facebook.png")
btn_facebook = Button(root, image=facebook_icon, command=form, bg="#b7e3f0", relief=GROOVE, borderwidth=0,
                      activebackground="#b7e3f0", activeforeground="#133342")
btn_facebook.place(x=505, y=520)
google_icon = PhotoImage(file="social_icon/google.png")
btn_google = Button(root, image=google_icon, bg="#b7e3f0", command=form, relief=GROOVE, borderwidth=0,
                    activebackground="#b7e3f0", activeforeground="#133342")
btn_google.place(x=560, y=520)
instagram_icon = PhotoImage(file="social_icon/instagram.png")
btn_instagram = Button(root, image=instagram_icon, bg="#b7e3f0", command=form, relief=GROOVE, borderwidth=0,
                       activebackground="#b7e3f0", activeforeground="#133342")
btn_instagram.place(x=610, y=520)
twitter_icon = PhotoImage(file="social_icon/twitter.png")
btn_twitter = Button(root, image=twitter_icon, bg="#b7e3f0", command=form, relief=GROOVE, borderwidth=0,
                     activebackground="#b7e3f0", activeforeground="#133342")
btn_twitter.place(x=660, y=520)

root.mainloop()
