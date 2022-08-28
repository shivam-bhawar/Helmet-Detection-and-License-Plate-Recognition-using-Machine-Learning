import tkinter

from tkinter import Label
from tkinter import Button
from PIL import ImageTk, Image

from subprocess import call

contact_window = tkinter.Tk()
contact_window.title("Contact Us")
contact_window.attributes('-fullscreen',False)
contact_window.geometry('%dx%d+%d+%d' % (371, 640, -7, 0))
contact_window.configure(background = "#FFFFFF")

temp_image = Image.open("lib/contact_background.png")
resized_image = temp_image.resize((367, 645), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_image)
background_image_label = Label(contact_window, image = background_image)
background_image_label.place(x = 0, y = 0)

def login():
    contact_window.destroy()
    call(["python", "login.py"])
    
def register():
    contact_window.destroy()
    call(["python", "register.py"])

def home():
    contact_window.destroy()
    call(["python", "home.py"])
    
page_title = Label(contact_window, text = "- Helmet Detection and License Plate Recognition System -", width = "60", height = "1", fg = "WHITE", bg = "BLACK", font = ('STENCIL', 17, ''))    
page_title.place(x = 373, y = 2)

contact_title = Label(contact_window, text = "- Contact Us -", font = ('ARIAL BLACK', 19, ''), bg = "YELLOW", fg = "BLACK", width = "20")
contact_title.place(x = 12, y = 10)

login_button = Button(contact_window, text="LOGIN", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = login)
login_button.place(x = 829, y = 40)

register_button = Button(contact_window, text="REGISTER", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = register)
register_button.place(x = 980, y = 40)

home_button = Button(contact_window, text="HOME", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = home)
home_button.place(x = 1131, y = 40)

info_label = Label(contact_window, text = "- Do reach us at - \n\n Pranavi Pote : pranavipote5464@gmail.com\n\n Shivam Bhawar : shivambhawar07@gmail.com\n\n\n Pratiksha Jadhav : pratikshajadhav@gmail.com \n\n Nikita Gite : nikitagite@gmail.com", width = "77", height = "21", fg = "BLACK", bg = "LIGHTGRAY", font = ('INK FREE', 16, ''))    
info_label.place (x = 373, y = 93)

exit_button = Button(contact_window, text="X", width = "5", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = contact_window.destroy)
exit_button.place(x = 1222, y = 2)

contact_window.mainloop()