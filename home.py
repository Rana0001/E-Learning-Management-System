from index import *


def data_insert(first, last, user_name, password):
    conn7 = sqlite3.connect("registration.db")
    c7 = conn7.cursor()
    query = ("INSERT INTO signup_form"
             "(first_name,last_name,user_name,new_password)"
             "VALUES(?,?,?,?)")
    values = (first, last, user_name, password)
    c7.execute(query, values)


def show_login_result(user_name, password):
    conn6 = sqlite3.connect("registration.db")
    c6 = conn6.cursor()
    c6.execute("SELECT * FROM signup_form WHERE user_name = ? and new_password = ?", (user_name, password))
    check = c6.fetchall()
    if check:
        return "Pass"
    else:
        return "Fail"


def main():
    home = Toplevel()
    home.title("Self Learner")
    home.geometry("1290x1080")
    home.iconbitmap("icon/title_icon.ico")

    # Defining function for buttons
    def link():
        pop = Toplevel()
        pop.title("Courses")
        pop.geometry("800x500")
        pop.iconbitmap("icon/title_icon.ico")
        pop.resizable(0, 0)
        pop_frame = Frame(pop, height=500, width=500, bg="#dc2d66")
        pop_frame.place(x=0, y=0, relheight=1, relwidth=1)
        pop_label = Label(pop, text="!!!!Check it out!!!!", font=("Ariel", 20, "bold"), bg="#dc2d66", fg="white")
        pop_label.place(x=250)
        link_label1 = Label(pop, text="Python Crash Course Link:", font=("Ariel", 12, "bold"), bg="#dc2d66", fg="white")
        link_label1.place(x=20, y=50)
        link_python = Label(pop, text="https://books.goalkicker.com/PythonBook/", font=("Ariel", 12, "bold"),
                            bg="#dc2d66",
                            fg="white")
        link_python.place(x=20, y=70)
        link_label2 = Label(pop, text="Java Crash Course Link:", font=("Ariel", 12, "bold"), bg="#dc2d66", fg="white")
        link_label2.place(x=20, y=100)
        link_java = Label(pop,
                          text="https://1337x.to/torrent/4010337/JavaScript-Programming-A-Step-by-Step-Guide-for-Absolute-Beginners/",
                          font=("Ariel", 11, "bold"), bg="#dc2d66",
                          fg="white")
        link_java.place(x=20, y=120)
        link_label3 = Label(pop, text="Ethical Hacking Crash Course Link:", font=("Ariel", 12, "bold"), bg="#dc2d66",
                            fg="white")
        link_label3.place(x=20, y=150)
        link_ethical = Label(pop,
                             text="https://1337x.to/torrent/3686652/Udemy-Ethical-Hacking-With-Python-JavaScript-and-Kali-Linux/",
                             font=("Ariel", 11, "bold"), bg="#dc2d66",
                             fg="white")
        link_ethical.place(x=20, y=170)
        link_label3 = Label(pop, text="@@@@@@@@@ For More Update Stay Tuned @@@@@@@@@", font=("Ariel", 12, "bold"),
                            bg="#dc2d66",
                            fg="white")
        link_label3.place(x=100, y=250)

        pop.mainloop()

    def fun_home():
        return 0

    def about():
        note = Toplevel()
        note.title("About Us")
        note.geometry("500x300")
        note.resizable(0, 0)
        note.iconbitmap("icon/title_icon.ico")
        about_frame = Frame(note, height=500, width=500, bg="#dc2d66")
        about_frame.place(x=0, y=0, relheight=1, relwidth=1)
        about_label = Label(note, text="About us", font=("Ariel", 20, "bold"), bg="#dc2d66", fg="white")
        about_label.place(x=180)
        about_label2 = Label(note,
                             text="This is only prototype of E-learing Management System.\n This system is still developing.\n"
                                  "So, this is just a demo of this application.\n"
                                  "My name is Prashant Rana Magar.\n I'm the developer of this application.\n\n\n"
                                  "\n\nThank you\n"
                                  "@@@@@@@@@@@@@@@@@@@"

                             , font=("Ariel", 12, "bold"), bg="#dc2d66", fg="white")
        about_label2.place(x=30, y=50)
        note.mainloop()

    def contact():
        phone = Toplevel()
        phone.title("About Us")
        phone.geometry("400x300")
        phone.resizable(0, 0)
        phone.iconbitmap("icon/title_icon.ico")
        phone_frame = Frame(phone, height=500, width=500, bg="#dc2d66")
        phone_frame.place(x=0, y=0, relheight=1, relwidth=1)
        phone_label1 = Label(phone, text="Contact us", font=("Ariel", 20, "bold"), bg="#dc2d66", fg="white")
        phone_label1.place(x=140)
        phone_label2 = Label(phone, text="Facebook: magarXXXXXXXXXXX@gmail.com"
                             , font=("Ariel", 12, "bold"), bg="#dc2d66", fg="white")
        phone_label2.place(x=20, y=50)
        phone_label3 = Label(phone, text="Whatsapp/Viber: 98XXXXXXXXXX", font=("Ariel", 12, "bold"), bg="#dc2d66",
                             fg="white")
        phone_label3.place(x=20, y=90)
        phone_label4 = Label(phone, text="For helpline: 00001000", font=("Ariel", 12, "bold"), bg="#dc2d66", fg="white")
        phone_label4.place(x=20, y=150)

        phone.mainloop()

    def update_data():
        key = Toplevel()
        key.geometry("600x500")
        key.title("Confirmation Alert")
        key.iconbitmap("icon/title_icon.ico")
        key.config(bg="#d7e9ff")
        key.resizable(0, 0)

        def update_new():
            conn1 = sqlite3.connect("registration.db")
            c1 = conn1.cursor()
            data = special_id.get()
            c1.execute("""UPDATE signup_form SET
            first_name = :first,
            last_name = :last,
            user_name = :email,
            new_password = :password,
            postal_number = :postal,
            address_name = :address,
            contact_number = :contact
        
            WHERE oid = :oid""",
                       {'first': first_input_edit.get(),
                        'last': last_input_edit.get(),
                        'email': email_input_edit.get(),
                        'password': new_password_input_edit.get(),
                        'postal': postal_code_input_edit.get(),
                        'address': address_input_edit.get(),
                        'contact': contact_input_edit.get(),
                        'oid': data
                        })

            conn1.commit()
            conn1.close()
            messagebox.showinfo("Data Updated!", "Save Completed....")

        def edit_data():
            edit = Toplevel()
            edit.geometry("1366x736")
            edit.iconbitmap("icon/title_icon.ico")
            edit.config(bg="#d7e9ff")
            conn2 = sqlite3.connect("registration.db")
            c2 = conn2.cursor()
            record_id = special_id.get()

            c2.execute("SELECT * FROM signup_form WHERE oid = " + record_id)

            newrecord = c2.fetchall()
            conn2.commit()
            conn2.close()
            # Creating Global variable to fetch the variable in another function
            global first_input_edit
            global last_input_edit
            global email_input_edit
            global new_password_input_edit
            global postal_code_input_edit
            global address_input_edit
            global contact_input_edit

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
            first_name_edit = Label(edit, text="First Name: ", width=10, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                    bg="#0e77f7")
            first_name_edit.place(x=750, y=205)
            first_input_edit = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
            first_input_edit.place(x=760, y=235, height=25)
            last_name_edit = Label(edit, text="Last Name: ", width=10, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                   bg="#0e77f7")
            last_name_edit.place(x=980, y=205)
            last_input_edit = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
            last_input_edit.place(x=990, y=235, height=25)
            email_name_edit = Label(edit, text="Email: ", width=5, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                    bg="#0e77f7")
            email_name_edit.place(x=754, y=275)
            email_input_edit = Entry(edit, width=40, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
            email_input_edit.place(x=760, y=305, height=25)

            new_password_edit = Label(edit, text="New Password: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                      bg="#0e77f7")
            new_password_edit.place(x=757, y=345)
            new_password_input_edit = Entry(edit, width=25, font=("Ariel", 11), show="*", relief=GROOVE, bg="#f7f7f7",
                                            fg="black")
            new_password_input_edit.place(x=760, y=375, height=25)
            postal_code_edit = Label(edit, text="Postal Code: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                     bg="#0e77f7")
            postal_code_edit.place(x=981, y=345)
            postal_code_input_edit = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
            postal_code_input_edit.place(x=990, y=375, height=25)
            address_name_edit = Label(edit, text="Address: ", width=8, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                      bg="#0e77f7")
            address_name_edit.place(x=750, y=415)
            address_input_edit = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
            address_input_edit.place(x=760, y=445, height=25)
            contact_no_edit = Label(edit, text="Contact No: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",
                                    bg="#0e77f7")
            contact_no_edit.place(x=976, y=415)
            contact_input_edit = Entry(edit, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
            contact_input_edit.place(x=990, y=445, height=25)
            for newRecord in newrecord:
                first_input_edit.insert(0, newRecord[0])
                last_input_edit.insert(0, newRecord[1])
                email_input_edit.insert(0, newRecord[2])
                new_password_input_edit.insert(0, newRecord[3])
                postal_code_input_edit.insert(0, newRecord[4])
                address_input_edit.insert(0, newRecord[5])
                contact_input_edit.insert(0, newRecord[6])
            btn_save = Button(edit, command=update_new, text="Save", width=15, relief=RAISED, bg="#0254b7",
                              fg="#fafafc", activebackground="#0254b7", activeforeground="#fafafc",
                              font=("Ariel", 10, "bold"))
            btn_save.place(x=920, y=535, height=40)

            edit.mainloop()

        def confirm():
            conn3 = sqlite3.connect("registration.db")
            c3 = conn3.cursor()
            c3.execute('SELECT *,oid FROM signup_form')
            data = c3.fetchall()

            for user_data in data:
                if str(user_data[3]) == password_id.get() and str(user_data[-1]) == special_id.get():
                    try:
                        key.withdraw()
                        return edit_data()
                    finally:
                        pass
            messagebox.showinfo("    Incorrect Password!!    ", "Please! Retry your password.", parent=key)

            conn3.commit()
            conn3.close()

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
        special_id.place(x=195, y=260)
        special_id.insert(0, "Enter your uid number")
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
    image1_button = Button(home, command=link, image=image1_real, bd=0, relief=RAISED)
    image1_button.place(x=315, y=440)

    image2 = Image.open("images/java.png")
    image2_resized = image2.resize((250, 200), Image.ADAPTIVE)
    image2_real = ImageTk.PhotoImage(image2_resized)
    image2_button = Button(home, command=link, image=image2_real, bg="white", bd=0, relief=RAISED)
    image2_button.place(x=580, y=440)

    image3 = Image.open("images/ethical.png")
    image3_resized = image3.resize((250, 200), Image.ADAPTIVE)
    image3_real = ImageTk.PhotoImage(image3_resized)
    image3_button = Button(home, command=link, image=image3_real, bg="#dc2d66", relief=RAISED)
    image3_button.place(x=850, y=440)

    # Inserting Button
    btn_home = Button(home, command=fun_home, text="Home", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                      bg="#59b1f0", fg="white", activebackground="#59b1f0", activeforeground="white")
    btn_home.place(x=50, y=100, height=35)
    btn_about = Button(home, command=about, text="About us", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                       bg="#59b1f0", fg="white", activebackground="#59b1f0", activeforeground="white")
    btn_about.place(x=50, y=150, height=35)
    btn_contact = Button(home, command=contact, text="Contact us", width=20, bd=1, relief=RAISED,
                         font=("Ariel", 10, "bold"),
                         bg="#59b1f0", fg="white", activebackground="#59b1f0", activeforeground="white")
    btn_contact.place(x=50, y=200, height=35)

    logout_btn = Button(home, command=exit, text="Log out", width=20, bd=1, relief=RAISED, font=("Ariel", 10, "bold"),
                        bg="#ff0b53", fg="white", activebackground="#ff0b53", activeforeground="white")
    logout_btn.place(x=50, y=650, height=35)

    home.mainloop()
