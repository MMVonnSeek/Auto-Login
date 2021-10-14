# importing the tkinter module
from tkinter import *

# defining a function
def fun():
    # defining autologin function and upon calling this function        
    # values for username and password will be autowritten
    def autologin():
        # setting username as coding community
        username.set("coding community")
        # setting secret password
        password.set("****************")

    # initializing tkinter
    login_screen = Tk()

    # setting gui title
    login_screen.title("Auto login with python")
    # setting gui geometry
    login_screen.geometry("300x250")

    # creating a text label widget and packing it
    Label(login_screen, text="Please enter login details").pack()

    # creating a text label widget and packing it
    Label(login_screen, text="Username").pack()
    # declaring a string type variable to store username from 
    # entry widget
    username = StringVar()

    # declaring a string type variable to store password from
    # entry widget
    password = StringVar()

    # creating a entry widget to take username 
    username_login_entry = Entry(login_screen, textvariable=username)
    # packing entry widget on gui screen
    username_login_entry.pack()

    # creating a text label widget and packing it
    l1 = Label(login_screen, text="Password").pack()

    # creating an entry widget to take password from user
    password_login_entry = Entry(login_screen, textvariable=password)

    # packing the entry widget
    password_login_entry.pack()

    # adding button to application screen to call autologin     
    # function
    Button(login_screen, text="Apply auto fill", command=autologin).pack()
    
    # adding button to applicaton screen to ask user to login
    Button(login_screen, text="Login Now", width=10, height=1).pack(pady=10)

    # running the mainloop when the code is ready
    login_screen.mainloop()

fun()

# By : Max Müller
