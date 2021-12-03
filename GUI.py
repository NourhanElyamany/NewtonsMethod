#Python GUI Programming With Tkinter
from tkinter import Tk, Menu, StringVar, BooleanVar, Label, Entry, Checkbutton, Button
import tkinter.messagebox

from matplotlib.pyplot import xticks
from method import start
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")

root.title("Newton Method")

root.resizable(False, False)


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
err = StringVar()
cbG = BooleanVar()
cbT = BooleanVar()



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

label4 = Label(root, text="Enter the stoping error:", width=19, font=("arial", 9, "bold"))
label4.place(x=80, y=260)

entry_4 = Entry(root, textvar=err)
entry_4.place(x=220, y=265)


c1 = Checkbutton(root, text="graph", variable=cbG, onvalue=True, offvalue=False).place(x=235, y=300)
c2 = Checkbutton(root, text="table", variable=cbT, onvalue=True, offvalue=False).place(x=300, y=300)


label3 = Label(root, text="Output :", width=20, font=("arial", 10, "bold"))
label3.place(x=73, y=300)

but_calculate = Button(root, text="Calculate", width=12, bg='brown', fg='white' , command = lambda : start(equ.get(),xi.get(),itr.get(),err.get(),cbT.get(),cbG.get())).place(x=150, y=400)

but_close = Button(root, text="quit", width=12, bg='brown', fg='white', command=exit1).place(x=280, y=400)

root.mainloop()