from index import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

home = Tk()
home.title("Self Learner")
home.geometry("1290x1080")
home.iconbitmap("icon/title_icon.ico")

# Defining function for buttons
def ask_pass(e):
    e.insert(0,"Enter your password")
def update_data():

    info_box = messagebox.askquestion("Confirmation Message","Enter your password")
    conn = sqlite3.connect("registration.db")
    c = conn.cursor()
    record_pass =
    c.execute("SELECT * ,oid FROM signup_form WHERE password = " + new_password)
    record = c.fetchall()


# Inserting Background Image
main_image = Image.open("images/bg.png")
main_resized = main_image.resize((1365, 768), Image.ADAPTIVE)
main_final_image = ImageTk.PhotoImage(main_resized)
main_image_label = Label(home, image=main_final_image)
main_image_label.place(x=0, y=0, relheight=1, relwidth=1)

# Inserting Banner
banner_img = Image.open("images/Banner.png")
banner_img_resized = banner_img.resize((830, 350), Image.ADAPTIVE)
banner_real = ImageTk.PhotoImage(banner_img_resized)
banner_label = Label(home, image=banner_real, bd=0, bg="#dc2d66")
banner_label.place(x=300, y=50)

# Inserting Label
home_label = Label(home, text="Welcome to Online Education", bg="#ff583b", fg="#f4fcfe",
                   font=("Ariel", 28, "bold italic"))
home_label.place(x=450)

# Inserting Avatar and Name of the user
avatar_icon = PhotoImage(file="images/avatar.png")
avatar_icon_label = Label(home, image=avatar_icon, bg="#ff583b")
avatar_icon_label.place(x=1150, y=25)
update_button = Button(home, text="UPDATE PROFILE", bg="#29bdd7", fg="white", activebackground="#bfe484",
                       activeforeground="#29bdd7", relief=RAISED, command = update_data)
update_button.place(x=1165, y=160)

# Inserting Frames with images and button
# Inserting Frames and label
main_frame1 = Frame(home, height=250, width=830, bg="#dc2d66")
main_frame1.place(x=300, y=400)
label_1 = Label(home, text="Recently Added Course:", bg="#dc2d66", fg="white", font=("Ariel", 15, "bold italic"))
label_1.place(x=305, y=400)
menu_frame2 = Frame(home, height=800, width=260, bg="#fd9745")
menu_frame2.place(x=10, y=50)
menu_label = Label(home, text=" Menu ", bg="#fd9745", fg="white", font=("Ariel", 15, "bold italic"))
menu_label.place(x=90, y=50)

# Inserting Images
image1 = Image.open("images/python.png")
image1_resized = image1.resize((250, 200), Image.ADAPTIVE)
image1_real = ImageTk.PhotoImage(image1_resized)
image1_label = Label(home, image=image1_real, bg="#dc2d66")
image1_label.place(x=315, y=440)

image2 = Image.open("images/java.png")
image2_resized = image2.resize((250, 200), Image.ADAPTIVE)
image2_real = ImageTk.PhotoImage(image2_resized)
image2_label = Label(home, image=image2_real, bg="white")
image2_label.place(x=580, y=440)

image3 = Image.open("images/ethical.png")
image3_resized = image3.resize((250, 200), Image.ADAPTIVE)
image3_real = ImageTk.PhotoImage(image3_resized)
image3_label = Label(home, image=image3_real, bg="#dc2d66")
image3_label.place(x=850, y=440)

# Inserting Button
btn_home = Button(home, command=exit, text="Home", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                  bg="#59b1f0", fg="white", activebackground="#59b1f0", activeforeground="white")
btn_home.place(x=50, y=100, height=35)
btn_course = Button(home, command=exit, text="Courses", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                  bg="#59b1f0", fg="white", activebackground="#59b1f0", activeforeground="white")
btn_course.place(x=50, y=150, height=35)
btn_contact = Button(home, command=exit, text="Contact us", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                  bg="#59b1f0", fg="white", activebackground="#59b1f0", activeforeground="white")
btn_contact.place(x=50, y=200, height=35)

logout_btn = Button(home, command=exit, text="Log out", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                    bg="#ff0b53", fg="white", activebackground="#ff0b53", activeforeground="white")
logout_btn.place(x=50, y=650, height=35)

home.mainloop()
