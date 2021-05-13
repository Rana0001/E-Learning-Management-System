from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def form():
    #Creating new windows for registration form
    register_win = Toplevel()
    register_win.geometry("1366x736")
    register_win.title("Sign Up")
    register_win.iconbitmap("icon/title_icon.ico")
    register_win.config(bg = "#eae8ed")
     #Defining fucntion for message and destroying registration windows
    def signup():
        messagebox.showinfo("         Sign up        ", " Sign up Successful ",parent = register_win)
        register_win.withdraw()

    #Adding Images
    signup_image = Image.open("background_images/page1.png")
    signup_image_resize = signup_image.resize((550,550),Image.ADAPTIVE)
    signup_resized = ImageTk.PhotoImage(signup_image_resize)
    signup_image_label = Label(register_win,image = signup_resized)
    signup_image_label.place(x = 200,y=100)

    #Creating A Frame for Sign up Form
    signup_frame = Frame(register_win,bg = "#bfb5f4",height = 550, width = 500)
    signup_frame.place(x = 755,y = 100)

    #Inserting Label for title
    signup_label = Label(register_win,text = "Let's Start",fg ="#785dae",bg = "#bfb5f4",font = ("Ariel",20,"bold"),width = 15)
    signup_label.place(x =870, y = 140)
    signup_name = Label(register_win,text = "Hurry up! and Sign up",fg ="#785dae",bg = "#bfb5f4",font = ("Ariel",20,"bold italic"))
    signup_name.place(x =860, y = 100)

    #Inserting Label (Name,password ,Phone Number) and Entry Widget
    first_name = Label(register_win,text = "First Name: ", width = 10,font =("Ariel",13,"bold"),fg = "#fbfbfd",bg="#bfb5f4")
    first_name.place(x = 755,y = 200)
    first_input = Entry(register_win, width = 25,font=("Ariel",11),relief = GROOVE,bg = "#f7f7f7",fg ="black")
    first_input.place(x = 760, y = 230,height = 25)
    last_name = Label(register_win, text="Last Name: ", width=10, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    last_name.place(x=985, y=200)
    last_input = Entry(register_win, width = 25,font=("Ariel",11),relief = GROOVE,bg = "#f7f7f7",fg ="black")
    last_input.place(x = 990, y = 230,height = 25)
    Email_name = Label(register_win, text="Email: ", width=5, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    Email_name.place(x=759, y=270)
    Email_input = Entry(register_win, width=40, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
    Email_input.place(x=760, y=300, height = 25)

    #Creating drop down for Gender(Male/ Female)
    gender_list = ["Male","Female","Not Specified"]
    clicked = StringVar()  #StingVar is used to store string values
    clicked.set("Male")
    gender_name = Label(register_win, text="Gender: ", width=8, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    gender_name.place(x=1085, y=270)
    gender_drop = OptionMenu(register_win,clicked, *gender_list)
    gender_drop.place(x = 1100,y = 300,height = 25)


    new_password = Label(register_win, text="New Password: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    new_password.place(x=762, y=340)
    new_password_input = Entry(register_win, width=25, font=("Ariel", 11),show="*", relief=GROOVE, bg="#f7f7f7", fg="black")
    new_password_input.place(x=760, y=370, height=25)
    postal_code = Label(register_win, text="Postal Code: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    postal_code.place(x=981, y=340)
    postalcode_input = Entry(register_win, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
    postalcode_input.place(x=990, y=370,height = 25)
    address_name = Label(register_win, text="Address: ", width=8, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    address_name.place(x=755, y=410)
    address_input = Entry(register_win, width=25, font=("Ariel", 11), show="*", relief=GROOVE, bg="#f7f7f7",fg="black")
    address_input.place(x=760, y=440, height=25)
    contact_no = Label(register_win, text="Contact No: ", width=12, font=("Ariel", 13, "bold"), fg="#fbfbfd",bg="#bfb5f4")
    contact_no.place(x=981, y=410)
    contact_input = Entry(register_win, width=25, font=("Ariel", 11), relief=GROOVE, bg="#f7f7f7", fg="black")
    contact_input.place(x=990, y=440,height = 25)

    #Inserting check box
    check_terms = Checkbutton(register_win,font = ("Ariel",12,"bold"),activebackground = "#bfb5f4",activeforeground = "black",fg = "black", bg = "#bfb5f4", text = "I agree the Terms and Conditions and Privacy Policy.",onvalue = "ON",offvalue = "OFF")
    check_terms.deselect()
    check_terms.place(x= 760, y = 480,height = 35)


    btn_signup = Button(register_win,command = signup,text = "Sign Up" ,width = 15, relief = RAISED,bg = "#785dae",fg = "#fafafc",activebackground = "#785dae",activeforeground ="#fafafc",font = ("Ariel",10,"italic"))
    btn_signup.place(x = 920 , y =530,height  = 40)
    register_win.mainloop()

