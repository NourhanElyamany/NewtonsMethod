#Python GUI Programming With Tkinter
from tkinter import *
import tkinter.messagebox

from matplotlib.pyplot import xticks
from method import start
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")

root.title("USER LOGIN")


menu = Menu(root)
root.config(menu=menu)


def exit1():
    exit()


def abt():
    tkinter.messagebox.showinfo("Welcome to authors", "this is demo for menu fields")


def ext_1():
    exit()


subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=abt)


equ = StringVar()
xi = StringVar()
itr = StringVar()
country = StringVar()
var_c1 = "Table"
var_c2 = "Graph"
radio_var = StringVar()




label_0 = Label(root, text="Newton Method", relief="solid", width=20, font=("arial", 19, "bold"))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Enter the equation:", width=20, font=("arial", 9, "bold"))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=equ)
entry_1.place(x=220, y=135)

label2 = Label(root, text="Enter the starting point:", width=20, font=("arial", 9, "bold"))
label2.place(x=80, y=180)

entry_2 = Entry(root, textvar=xi)
entry_2.place(x=220, y=185)

label3 = Label(root, text="Enter number of iter:", width=20, font=("arial", 9, "bold"))
label3.place(x=80, y=220)

entry_3 = Entry(root, textvar=itr)
entry_3.place(x=220, y=225)

label4 = Label(root, text="Select table color:", width=19, font=("arial", 9, "bold"))
label4.place(x=80, y=260)

list_1 = ['Pakistan', 'India', 'UAE', 'Iran', 'China']
droplist = OptionMenu(root, country, *list_1)
country.set("Select Country")
droplist.config(width=15)
droplist.place(x=220, y=255)



c1 = Checkbutton(root, text="graph", variable=var_c1).place(x=235, y=300)
c2 = Checkbutton(root, text="table", variable=var_c2).place(x=300, y=300)


label3 = Label(root, text="Output :", width=20, font=("arial", 10, "bold"))
label3.place(x=73, y=300)

but_singup = Button(root, text="Calculate", width=12, bg='brown', fg='white' , command = lambda : start(equ.get(),xi.get(),itr.get())).place(x=150, y=400)

but_close = Button(root, text="quit", width=12, bg='brown', fg='white', command=exit1).place(x=280, y=400)

root.mainloop()