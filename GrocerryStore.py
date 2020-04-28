from tkinter import *

root = Tk()
root.title("Grocerry Store Management")
root.geometry("200x250")
scvalue = StringVar()
scvalue.set("")


f = Frame(root, bg="grey")
f.pack()

screen = Entry(f, textvar=scvalue, font="lucida 15 bold")
screen.pack()

cart = []

def add():
	e = screen.get()
	appended = cart.append(e)
	scvalue.set("")
	screen.update()


def remove():
	cart.pop()


def show():
	print(cart)

def length():
	length = len(cart)
	print("Total items you purchsed - ",length)

btnAdd = Button(f, text="Add item", font="lucida 20 bold", command=add)
btnRemove = Button(f, text="Remove item", font="lucida 20 bold", command=remove)
btnShow = Button(f, text="Show", font="lucida 20 bold",command=show)
btnLen= Button(f, text="Length", font="lucida 20 bold",command=length)

btnRemove.pack()
btnAdd.pack()
btnShow.pack()
btnLen.pack()

root.mainloop()