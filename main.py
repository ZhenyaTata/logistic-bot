from tkinter import *
import random


def generate_color():
    entryColor.delete(0, END)
    color = "#{:02x}{:02x}{:02x}".format(*map(lambda x: random.randint(0, 255), range(3)))
    labelColor["bg"] = color
    entryColor.insert(0, color)



root = Tk()
root.title("Генератор цветов")
root.geometry("200x300")
root.resizable(0, 0)
labelColor = Label(root, bg="white")
labelColor.place(relx=0.5, rely=0.3, anchor=CENTER, width=150, height=130)

entryColor = Entry(root, borderwidth=4)
entryColor.place(relx=0.5, rely=0.6, anchor=CENTER, width=150, height=30)

btnGenerate = Button(root, text="Сгенерировать", font="Arial 13 bold", borderwidth=4, command=generate_color)
btnGenerate.place(relx=0.5, rely=0.8, anchor=CENTER, width=150, height=60)
root.mainloop()
