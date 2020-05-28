from tkinter import *

root = Tk()

root.title("DropDown Menu")
root.geometry("400x400")

def show():
    myChoice = Label(root, text = clicked.get()).pack()



options = [
    "Novi Sad",
    "New York",
    "Valjevo",
    "Wuhan",
    "Svet"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

button = Button(root, text = "Selection", command = show).pack()
"""menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)

menu.add_cascade(label = "city", menu = subMenu)
subMenu.add_command(label = "Novi Sad")
subMenu.add_command(label = "Wuhan")
subMenu.add_command(label = "New York")
subMenu.add_command(label = "Valjevo")
subMenu.add_command(label = "Svet")
"""

def showMask():
    labelm = Label(root, text = var2.get()).pack()
def showGloves():
    labelr = Label(root, text = var.get()).pack()

var = IntVar()
var2 = IntVar()

c = Checkbutton(root, text = "Cekiraj, da bi stavio svima rukavice", variable=var).pack()
c2 = Checkbutton(root, text = "Cekiraj, da bi stavio svima maske", variable = var2).pack()

buttonGloves = Button(root, text = "showCheckGloves", command = showGloves).pack()
buttonMasks = Button(root, text = "showCheckMask", command = showMask).pack()

root.mainloop()