import tkinter

from tkinter import Label
from tkinter import Button
from PIL import ImageTk, Image

from subprocess import call

menu_window = tkinter.Tk()
menu_window.title("Menu")
menu_window.attributes('-fullscreen',False)
menu_window.geometry('%dx%d+%d+%d' % (371, 640, -7, 0))
menu_window.configure(background = "#FFFFFF")

temp_image = Image.open("lib/menu_background.png")
resized_image = temp_image.resize((367, 645), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_image)
background_image_label = Label(menu_window, image = background_image)
background_image_label.place(x = 0, y = 0)

def helmet():
    menu_window.destroy()
    call(["python", "helmet_detection.py"])
    
def number_plate():
    menu_window.destroy()
    call(["python", "main.py"])

page_title = Label(menu_window, text = "- Helmet Detection and License Plate Recognition System -", width = "60", height = "1", fg = "WHITE", bg = "BLACK", font = ('STENCIL', 17, ''))    
page_title.place(x = 373, y = 2)

menu_title = Label(menu_window, text = "- Menu -", font = ('ARIAL BLACK', 19, ''), bg = "YELLOW", fg = "BLACK", width = "20")
menu_title.place(x = 12, y = 10)

helmet_button = Button(menu_window, text="Helmet Detection", width = "25", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = helmet)
helmet_button.place(x = 720, y = 250)

number_plate_button = Button(menu_window, text="Number Plate Recognition", width = "25", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = number_plate)
number_plate_button.place(x = 720, y = 350)

exit_button = Button(menu_window, text="X", width = "5", fg = "WHITE", bg = "RED", font = ('ARIAL BLACK', 10, ''), cursor = "hand2", command = menu_window.destroy)
exit_button.place(x = 1222, y = 2)

menu_window.mainloop()