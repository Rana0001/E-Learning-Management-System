from registration_form import *
from tkinter import *
from PIL import ImageTk,Image

#Creating Tkinter Windows
root = Tk()
root.title("Self Learner")
root.geometry("1280x1080")
root.iconbitmap("icon/title_icon.ico")
#Adding Background Image
bg_image = Image.open("images/newback.png")
bg_image_resized = bg_image.resize((1366,768),Image.ADAPTIVE)
resized = ImageTk.PhotoImage(bg_image_resized)
bgImg = Label(root,image = resized)
bgImg.place(x = 0, y = 0,relheight = 1 , relwidth = 1)
frame = Frame(root,width = 425, height = 500,bg = "#b7e3f0")
frame.place(x = 465, y = 140)
label = Label(root, text = "Login", font = ("Ariel",20,"bold italic"),fg ="#133342",bg = "#b7e3f0")
label.place(x = 625, y = 200)

#Adding Icon
user_icon = ImageTk.PhotoImage(Image.open("icon/user.png"))
user_icon_label = Label(root, image = user_icon, bg="#b7e3f0")
user_icon_label.place(x = 595 , y = 70)

#Adding Widgets and Field
username_label = Label(root, text = "Username/Email:",border = 0,font = ("Ariel",13,"bold"), fg ="#133342",bg ="#b7e3f0" )
username_label.place(x = 500, y = 260)
username_field = Entry(root, width = 35, border = 0 , fg ="#133342",bg = "#b7e3f0", font=("Ariel",12))
username_field.place(x = 540, y = 295)
Frame(root,width = 300, borderwidth = 0 ,bg = "black").place(x = 540, y = 315)
password_label = Label(root, text = "Password:",border = 0,font = ("Ariel",13,"bold"), fg ="#133342",bg ="#b7e3f0")
password_label.place(x = 500, y = 340)
password_field = Entry(root, width = 35,bg = "#b7e3f0", border = 0 , fg ="#133342", font=("Ariel",12), show = "*")
password_field.place(x = 540, y = 375)
Frame(root,width = 300, borderwidth = 0 ,bg = "black").place(x = 540, y = 395)

#Adding Icons of username and password
username_icon = PhotoImage(file = "icon/username.png")
username_icon_label = Label(root, image = username_icon,bg = "#b7e3f0", fg ="#133342")
username_icon_label.place(x =500, y = 285)
password_icon = PhotoImage(file = "icon/password.png")
password_icon_label = Label(root, image = password_icon,bg = "#b7e3f0", fg ="#133342")
password_icon_label.place(x =500, y = 365)

#Creating Home Windows
def login():
    root.withdraw()
    login_win = Toplevel()
    login_win.geometry("1366x736")
    login_win.title("Welcome to Online Education")
    login_win.iconbitmap("icon/title_icon.ico")
    messagebox.showinfo("Welcome","LOLOL",parent = login_win)
    login_win.mainloop()


#Adding Sign in button and registration form
btn_signin = Button(root,command = login,text = "Log in",width = 15,bd = 3,relief =RAISED,font=("Ariel",10,"bold"), bg = "#f98135",fg = "#133342",activebackground = "#f98135",activeforeground = "#133342")
btn_signin.place(x = 615, y = 430)
btn_signup = Button(root,command = form, text = "Create a new account",font=("Ariel",10,"bold"), bg = "#b7e3f0",fg = "#133342",borderwidth = 0,relief = RIDGE,activebackground = "#b7e3f0",activeforeground = "#133342")
btn_signup.place(x = 500, y = 490)
# Adding icon of facebook,twitter, instagram and linkedin
facebook_icon = PhotoImage(file = "social_icon/facebook.png")
btn_facebook = Button(root, image = facebook_icon , bg = "#b7e3f0", relief =GROOVE,borderwidth = 0,activebackground = "#b7e3f0",activeforeground = "#133342")
btn_facebook.place(x = 505, y = 520)
google_icon = PhotoImage(file = "social_icon/google.png")
btn_google = Button(root, image = google_icon , bg = "#b7e3f0", relief =GROOVE,borderwidth = 0,activebackground = "#b7e3f0",activeforeground = "#133342")
btn_google.place(x = 560, y = 520)
instagram_icon = PhotoImage(file = "social_icon/instagram.png")
btn_instagram = Button(root, image = instagram_icon , bg = "#b7e3f0", relief =GROOVE,borderwidth = 0,activebackground = "#b7e3f0",activeforeground = "#133342")
btn_instagram.place(x = 610, y = 520)
twitter_icon = PhotoImage(file = "social_icon/twitter.png")
btn_twitter = Button(root, image = twitter_icon , bg = "#b7e3f0", relief =GROOVE,borderwidth = 0,activebackground = "#b7e3f0",activeforeground = "#133342")
btn_twitter.place(x = 660, y = 520)

root.mainloop()