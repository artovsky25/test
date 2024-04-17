from tkinter import *
import tkinter.messagebox

root = tkinter.Tk()

root.title("Test")
root.geometry('100x100')

def onClick():
    tkinter.messagebox.showinfo("test", "Hi. It looks like you are runnig a test script from the test repository.")


button = Button(root, text="Click Me", command=onClick, height=5, width=10)

button.pack(side='bottom')
root.mainloop() 