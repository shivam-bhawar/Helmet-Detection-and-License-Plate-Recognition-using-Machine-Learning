import tkinter

from tkinter import Label
from tkinter import Button
from PIL import ImageTk, Image

from subprocess import call

home_window = tkinter.Tk()
home_window.title("Home")
home_window.attributes('-fullscreen',False)
home_window.geometry('%dx%d+%d+%d' % (371, 640, -7, 0))
home_window.configure(background = "#FFFFFF")

temp_image = Image.open("lib/home_background.png")
resized_image = temp_image.resize((367, 645), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_image)
background_image_label = Label(home_window, image = background_image)
background_image_label.place(x = 0, y = 0)

def login():
    home_window.destroy()
    call(["python", "login.py"])
    
def register():
    home_window.destroy()
    call(["python", "register.py"])
    
def contact():
    home_window.destroy()
    call(["python", "contact.py"])

page_title = Label(home_window, text = "- Helmet Detection and License Plate Recognition System -", width = "60", height = "1", fg = "WHITE", bg = "BLACK", font = ('STENCIL', 17, ''))    
page_title.place(x = 373, y = 2)

home_title = Label(home_window, text = "- Home -", font = ('ARIAL BLACK', 19, ''), bg = "YELLOW", fg = "BLACK", width = "20")
home_title.place(x = 12, y = 10)

login_button = Button(home_window, text="LOGIN", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = login)
login_button.place(x = 829, y = 40)

register_button = Button(home_window, text="REGISTER", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = register)
register_button.place(x = 980, y = 40)

contact_button = Button(home_window, text="CONTACT US", width = "15", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = contact)
contact_button.place(x = 1131, y = 40)

info_label = Label(home_window, text = " -: ACT OF 1988 :- \n\n A recent study shows that 6 motorcycle riders face accidents every hour. As of 2019, \n over 37% of road accidents involved two-wheelers (1). \n\n Among the alarming rate of casualties, most are a result of head injuries, which reflects \n the remarkable neglect of helmet usage among two-wheeler riders. While several factors \n are responsible for individuals driving without helmets, 16% revealed to be under the \n impression that helmets are not mandated by law, which is completely untrue (2). \n\n While your love for comfort may win over the need for safety precautions, it can never be \n a preference over law mandates. The need for more stringent implementation of traffic \n laws was observed due to an increasing number of road accidents every year. While 2017 \n saw 35,975 deaths due to non-use of helmets, the number further rose to 43,614 in \n 2018 (3). \n\n Probably, this appalling number of casualties, which riders could prevent only with the use \n of headgear, prompted the government to improvise on already existing helmet laws in \n India. To discourage riders from riding without a helmet, the initial Motor Vehicles Act of \n 1988 introduced Rs.1000 as a fine for not wearing a helmet .", width = "77", height = "21", fg = "BLACK", bg = "LIGHTGRAY", font = ('INK FREE', 16, ''))    
info_label.place (x = 373, y = 93)

exit_button = Button(home_window, text="X", width = "5", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = home_window.destroy)
exit_button.place(x = 1222, y = 2)

home_window.mainloop()