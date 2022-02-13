import tkinter
import pyperclip
from tkinter import *
import time
#Clipboard Function
clipboard = {}
msg = "Hi"

if msg.lower() == "load":
    if len(clipboard) < 1:
        print("You have nothing in your clipboard.")
    else:
        key = (input("What key would you like to access?")).lower()
        print(clipboard[key] + " has been copied to your clipboard!")
        pyperclip.copy(clipboard[key])


def readFunction():
     if len(clipboard) < 1:
         print("You have nothing in your clipboard.")
     else:
         for key in clipboard:
             label = Label(win, text=key+" "+ clipboard[key])
             label.pack()


def saveFunction():
    clipboard[key.get()] = message.get()
    message.delete(0, 'end')
    key.delete(0, 'end')
    label = Label(win, text="Your item has been saved!")
    label.pack()

def loadFunction():
    label = Label(win, text=clipboard[userkey.get()])
    label.pack()


#Frontend
#Window
win = Tk()
win.title("MultiClipboard")
win.geometry("700x400")
#Read Button
readButton = tkinter.Button(win, text = "Read", command = readFunction)
readButton.pack()


#Save Button + TextBoxes
message = Entry(win, width = 50, bg = "blue", fg = "white", borderwidth = 5)
message.pack()
key = Entry(win, width = 30, bg = "red", fg = "white", borderwidth = 5)
key.pack()
saveButton = tkinter.Button(win, text = "Save", command = saveFunction)
saveButton.pack()


#Load Button
userkey = Entry(win, width = 50, bg = "green", fg = "white", borderwidth = 5)
userkey.pack()
loadButton = tkinter.Button(win, text = "Load", command = loadFunction)
loadButton.pack()

#Window Loop
win.mainloop()