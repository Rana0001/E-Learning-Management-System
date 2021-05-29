# from index import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

home = Tk()
home.title("Self Learner")
home.geometry("1290x1080")
home.iconbitmap("icon/title_icon.ico")



# Defining function for buttons

def update_data():
    key = Toplevel()
    key.geometry("600x500")
    key.title("Confirmation Alert")
    key.iconbitmap("icon/title_icon.ico")
    key.config(bg="#d7e9ff")
    key.resizable(0, 0)

    def edit_data():
        edit = Toplevel()
        edit.geometry("1366x736")
        edit.iconbitmap("icon/title_icon.ico")
        edit.config(bg="#d7e9ff")
        # Inserting images
        conn = sqlite3.connect("registration.db")
        c = conn.cursor()
        record_id = special_id.get()

        c.execute("SELECT * FROM signup_form WHERE oid = " + record_id)

        newrecord = c.fetchall()
        conn.commit()
        conn.close()

        update_image = Image.open("images/update.png")
        update_resized = update_image.resize((500, 600), Image.ADAPTIVE)
        update_real = ImageTk.PhotoImage(update_resized)
        update_label = Label(edit, image=update_real, bg="#ffffff")
        update_label.place(x=200, y=50)
        edit_frame = Frame(edit, height=605, width=500, bg="#0e77f7")
        edit_frame.place(x=720, y=50)
        edit_label = Label(edit, text="  Update your Information  ", bg="#0e77f7", fg="#ffffff",
                           font=("Ariel", 18, "bold italic"))
        edit_label.place(x=840, y=50)

        avatar_icon = PhotoImage(file="images/avatar.png")
        avatar_icon_label = Label(edit, image=avatar_icon, bg="#0e77f7")
        avatar_icon_label.place(x=890, y=80)

        # Inserting Entry field and Button
        first_name = Label(edit, text="First Name: ", width=10, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                           bg="#0e77f7")
        first_name.place(x=750, y=205)
        first_input = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
        first_input.place(x=760, y=235, height=25)
        last_name = Label(edit, text="Last Name: ", width=10, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                          bg="#0e77f7")
        last_name.place(x=980, y=205)
        last_input = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
        last_input.place(x=990, y=235, height=25)
        email_name = Label(edit, text="Email: ", width=5, font=("Ariel", 13, "bold"), fg="#fbfbfd", bg="#0e77f7")
        email_name.place(x=754, y=275)
        email_input = Entry(edit, width=40, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
        email_input.place(x=760, y=305, height=25)

        new_password = Label(edit, text="New Password: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                             bg="#0e77f7")
        new_password.place(x=757, y=345)
        new_password_input = Entry(edit, width=25, font=("Ariel", 11), show="*", relief=GROOVE, bg="#f7f7f7",
                                   fg="black")
        new_password_input.place(x=760, y=375, height=25)
        postal_code = Label(edit, text="Postal Code: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                            bg="#0e77f7")
        postal_code.place(x=981, y=345)
        postal_code_input = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
        postal_code_input.place(x=990, y=375, height=25)
        address_name = Label(edit, text="Address: ", width=8, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                             bg="#0e77f7")
        address_name.place(x=750, y=415)
        address_input = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
        address_input.place(x=760, y=445, height=25)
        contact_no = Label(edit, text="Contact No: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                           bg="#0e77f7")
        contact_no.place(x=976, y=415)
        contact_input = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
        contact_input.place(x=990, y=445, height=25)
        for newRecord in newrecord:
            first_input.insert(0, newRecord[0])
            last_input.insert(0, newRecord[1])
            email_input.insert(0, newRecord[2])
            new_password_input.insert(0, newRecord[3])
            postal_code_input.insert(0, newRecord[4])
            address_input.insert(0, newRecord[5])
            contact_input.insert(0, newRecord[6])
        btn_save = Button(edit, command=exit, text="Save", width=15, relief=RAISED, bg="#0254b7",
                          fg="#fafafc", activebackground="#0254b7", activeforeground="#fafafc",
                          font=("Ariel", 10, "bold"))
        btn_save.place(x=920, y=535, height=40)

        edit.mainloop()

    def confirm():
        conn = sqlite3.connect("registration.db")
        c = conn.cursor()
        c.execute('SELECT *,oid FROM signup_form')
        data = c.fetchall()

        for user_data in data:
            if str(user_data[3]) == password_id.get() and str(user_data[-1])== special_id.get():
                try:
                    key.withdraw()
                    return edit_data()
                finally:
                    pass
        messagebox.showinfo("    Incorrect Password!!    ", "Please! Retry your password.", parent=key)

        conn.commit()
        conn.close()

    password_image = Image.open("images/password.png")
    password_resized = password_image.resize((600, 500), Image.ADAPTIVE)
    password_real = ImageTk.PhotoImage(password_resized)
    password_img_label = Label(key, image=password_real, bg="#dc2d66", bd=0)
    password_img_label.place(x=0, y=0)
    label_password = Label(key, text="Enter your password:", bg="#015ceb", fg="white")
    label_password.place(x=195, y=212)
    password_id = Entry(key, width=19, show="*")
    password_id.place(x=195, y=239)
    special_id = Entry(key, width=19)
    special_id.place(x=195, y =260)
    special_id.insert(0,"Enter your uid number")
    confirm_btn = Button(key, command=confirm, text="Confirm", width=10, bd=3, relief=RAISED,
                         font=("Ariel", 8, "bold"),
                         bg="#fd9745", fg="white", activebackground="#fd9745", activeforeground="white")
    confirm_btn.place(x=205, y=283)

    key.mainloop()


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
home_label = Label(home, text="Welcome to Online Education", bg="#ff583b", fg="#F4FCFE",
                   font=("Ariel", 28, "bold italic"))
home_label.place(x=450)

# Inserting Avatar and Name of the user
avatar_icon = PhotoImage(file="images/avatar.png")
avatar_icon_label = Label(home, image=avatar_icon, bg="#ff583b")
avatar_icon_label.place(x=1150, y=25)
update_button = Button(home, text="UPDATE PROFILE", bg="#29bdd7", fg="white", activebackground="#29bdd7",
                       activeforeground="white", relief=RAISED, command=update_data)
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
