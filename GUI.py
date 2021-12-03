from tkinter import Tk, Menu, StringVar, BooleanVar, Label, Entry, Checkbutton, Button, messagebox
from method import start
from helpers import authers, Holder

root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)
root.title("Newton Method")
root.iconbitmap('logo.ico')

root.resizable(False, False)

menu = Menu(root)
root.config(menu=menu)
holder = Holder()

def exitfx():
    exit()


def authList():
    messagebox.showinfo("List of Authers", authers)

def savePlot():
    holder.savePlot()
def saveTable():
    holder.saveTable()


fileSubMenu = Menu(menu)
aboutSubMen = Menu(menu)

menu.add_cascade(label="File", menu=fileSubMenu)
menu.add_cascade(label="About", menu=aboutSubMen)

fileSubMenu.add_command(label="Save graph", command=savePlot)
fileSubMenu.add_command(label="Save table", command=saveTable)
fileSubMenu.add_command(label="Exit", command=exitfx)

aboutSubMen.add_command(label="Authers", command=authList)
aboutSubMen.add_command(label="Documentation", command=exitfx)

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

but_calculate = Button(root, text="Calculate", width=12, bg='brown', fg='white' , command = lambda : start(
                                                                                                    equ.get(),
                                                                                                    xi.get(),
                                                                                                    itr.get(),
                                                                                                    err.get(),
                                                                                                    cbT.get(),
                                                                                                    cbG.get(),
                                                                                                    holder
                                                                                                )).place(x=150, y=400)

but_close = Button(root, text="quit", width=12, bg='brown', fg='white', command=exitfx).place(x=280, y=400)

root.mainloop()