import tkinter

from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox
from PIL import ImageTk, Image

from subprocess import call

import sqlite3

import smtplib

register_window = tkinter.Tk()
register_window.title("Register")
register_window.attributes('-fullscreen',False)
register_window.geometry('%dx%d+%d+%d' % (371, 640, -7, 0))
register_window.configure(background = "#FFFFFF")

first_name = tkinter.StringVar()
last_name = tkinter.StringVar()
mail_id = tkinter.StringVar()
username = tkinter.StringVar()
password = tkinter.StringVar()
confirm_password = tkinter.StringVar()

db = sqlite3.connect('Database.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Admin" "(FirstName TEXT, LastName TEXT, EmailId TEXT, UserName TEXT, Password TEXT, ConfirmPassword TEXT)")
db.commit()

def register():
    fname = first_name.get()
    lname = last_name.get()
    mail = mail_id.get()
    uname = username.get()
    passw = password.get()
    confpassw = confirm_password.get()
        
    if ((fname.isdigit()) or (fname == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid First Name ! \n - First Name must not be Empty, \n - First Name must not contain any Digits.")
    elif ((lname.isdigit()) or (lname == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Last Name ! \n - Last Name must not be Empty, \n - Last Name must not contain any Digits.")
    elif ((mail == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Mail ID ! \n - Mail ID must not be Empty.")
    elif (uname.isdigit() or (uname == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Username ! \n - Username must not be Empty.")
    elif (((len(str(passw))) < 8) or (passw == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Password ! \n - Password must not be Empty, \n - Length of Password must be greater than 8.")
    elif (((len(str(confpassw))) < 8) or (confpassw == "")):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Please, Enter a valid Password ! \n - Password must not be Empty, \n - Length of Password must be greater than 8.")
    elif (passw != confpassw):
        messagebox.showerror("ERROR", "Invalid Input !")
        messagebox.showinfo("Message", "Password and Confirm password must be same !")
    else:
        con = sqlite3.connect('Database.db')
        with con:
            cursor = con.cursor()
            cursor.execute('INSERT INTO Admin(FirstName, LastName, EmailId, UserName, Password, ConfirmPassword) VALUES(?, ?, ?, ?, ?, ?)', (fname, lname, mail, uname, passw, confpassw))

            con.commit()
            db.close()
            
            messagebox.showinfo("Congratulations", "Registration Successful.")
            
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            
            # start TLS for security
            s.starttls()
            
            # Authentication
            s.login("helmetdetectionsys@gmail.com", "Helmet@123")
            
            # message to be sent
            message = "You have successfully created an account in our Helmet Detection and License Plate Recognition System."
            
            # sending the mail
            temp = s.sendmail("helmetdetectionsys@gmail", mail, message)
            
            messagebox.showinfo("Congratulations", "A mail has been sent to your Gmail Account.")
            
            # terminating the session
            s.quit()

            
            register_window.destroy()
            call(["python", "Login.py"])
    
temp_image = Image.open("lib/register_background.png")
resized_image = temp_image.resize((367, 645), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_image)
background_image_label = Label(register_window, image = background_image)
background_image_label.place(x = 0, y = 0)

page_title = Label(register_window, text = "- Helmet Detection and License Plate Recognition System -", width = "60", height = "1", fg = "WHITE", bg = "BLACK", font = ('STENCIL', 17, ''))    
page_title.place(x = 373, y = 2)

register_title = Label(register_window, text = "- SIGN UP -", font = ('ARIAL BLACK', 19, ''), fg = "BLACK", bg = "YELLOW", width = "20")
register_title.place(x = 12, y = 10)

first_name_label = Label(register_window, text = "FIRST NAME :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
first_name_label.place(x = 560, y = 150)

first_name_input = Entry(register_window, textvar = first_name, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
first_name_input.place(x = 560, y = 200)

last_name_label = Label(register_window, text = "LAST NAME :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
last_name_label.place(x = 850, y = 150)

last_name_input = Entry(register_window, textvar = last_name, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
last_name_input.place(x = 850, y = 200)

mail_id_label = Label(register_window, text = "MAIL-ID :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
mail_id_label.place(x = 560, y = 280)

mail_id_input = Entry(register_window, textvar = mail_id, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
mail_id_input.place(x = 560, y = 320)

username_label = Label(register_window, text = "USERNAME :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
username_label.place(x = 850, y = 280)

username_input = Entry(register_window, textvar = username, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
username_input.place(x = 850, y = 320)

password_label = Label(register_window, text = "PASSWORD :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
password_label.place(x = 560, y = 410)

password_input = Entry(register_window, textvar = password, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
password_input.place(x = 560, y = 450)

confirm_password_label = Label(register_window, text = "CONFIRM PASSWORD :", font = ('CENTURI GOTHIC', 15, ''), bg = "WHITE")
confirm_password_label.place(x = 850, y = 410)

confirm_password_input = Entry(register_window, textvar = confirm_password, width = 20, font = ('COURIER', 15, ''), bg = "WHITESMOKE")
confirm_password_input.place(x = 850, y = 450)

submit_button = Button(register_window, text="SUBMIT", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = register)
submit_button.place(x = 755, y = 550)

exit_button = Button(register_window, text="X", width = "5", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = register_window.destroy)
exit_button.place(x = 1222, y = 2)

register_window.mainloop()