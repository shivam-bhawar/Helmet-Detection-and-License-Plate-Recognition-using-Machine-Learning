import tkinter

from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox
from PIL import ImageTk, Image

from subprocess import call

import sqlite3

login_window = tkinter.Tk()
login_window.title("Login")
login_window.attributes('-fullscreen',False)
login_window.geometry('%dx%d+%d+%d' % (371, 640, -7, 0))
login_window.configure(background = "#FFFFFF")

username = tkinter.StringVar()
password = tkinter.StringVar()

def login():
    uname = username.get()
    passw = password.get()
    
    if (uname.isdigit() or (uname == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Username ! \n - Username must not be Empty.")
    elif (((len(str(passw))) < 8) or (passw == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Password ! \n - Password must not be Empty, \n - Length of Password must be greater than 8.")
    else:
        with sqlite3.connect('Database.db') as db:
            c = db.cursor()

        con = sqlite3.connect('Database.db')
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Admin" "(FirstName TEXT, LastName TEXT, EmailId TEXT, UserName TEXT, Password TEXT, ConfirmPassword TEXT)")
        con.commit()
        
        find_entry = ('SELECT * FROM Admin WHERE UserName = ? and Password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()

        if result:
            msg = ""
            print(msg)
            messagebox.showinfo("Congratulations", "Login Successful")
            login_window.destroy()
            call(["python", "menu.py"])
        else:
            messagebox.showwarning("Error", "Something Wrong !")
            messagebox.showerror('Oops!', 'Username Or Password Did Not Found / Match.')

temp_image = Image.open("lib/login_background.png")
resized_image = temp_image.resize((367, 645), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_image)
background_image_label = Label(login_window, image = background_image)
background_image_label.place(x = 0, y = 0)

page_title = Label(login_window, text = "- Helmet Detection and License Plate Recognition System -", width = "60", height = "1", bg = "BLACK", fg = "WHITE", font = ('STENCIL', 17, ''))    
page_title.place(x = 373, y = 2)

login_title = Label(login_window, text = "- SIGN IN -", font = ('ARIAL BLACK', 19, ''), bg = "YELLOW", fg = "BLACK", width = "20")
login_title.place(x = 12, y = 10)

username_label = Label(login_window, text = "USERNAME :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
username_label.place(x = 710, y = 180)

username_input = Entry(login_window, textvar = username, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
username_input.place(x = 710, y = 230)

password_label = Label(login_window, text = "PASSWORD :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
password_label.place(x = 710, y = 310)

password_input = Entry(login_window, textvar = password, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE", show = "*")
password_input.place(x = 710, y = 350)

submit_button = Button(login_window, text="SUBMIT", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = login)
submit_button.place(x = 765, y = 450)

exit_button = Button(login_window, text="X", width = "5", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = login_window.destroy)
exit_button.place(x = 1222, y = 2)

login_window.mainloop()