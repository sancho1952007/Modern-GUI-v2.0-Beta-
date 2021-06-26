"""
====== GUI Design By: Sancho Godinho (sanchogodinho98@gmail.com) ======
====== Images By: Flaticon (https://flaticon.com) ======

\\ Please Do Not Delete the Images Folder!

\\ Please Do Not Clear This Comment!

\\ You Are Allowed to Customize this Script.

\\ If you want to share this script or Customize and share: You Should Keep this comment with it.

"""

from tkinter import *
from tkinter.font import *
import os
path=os.path.dirname(os.path.realpath(__file__))+"\\"
app=Tk()
app.overrideredirect(True)
app.geometry("300x200")
app.config(bg="#d3d3d3")
app.config(bd=1)

def detect_key_press(event):
    if event.keysym=='F5':
        big_screen()
    elif event.keysym=="F9":
        small_screen()
    elif event.keysym=="F1":
        app.destroy()

def enter_close(event):
    close.config(image=close2)

def leave_close(event):
    close.config(image=close1)

def move(event):
    app.geometry(f"+{event.x_root-145}+{event.y_root-7}")

def small_screen():
    app.state('normal')
    size.config(image=maximize, command=big_screen)
    title.place(anchor=CENTER, relx=0.5, rely=0.5)

def big_screen():
    app.state("zoomed")
    size.config(image=minimize, command=small_screen)
    title.grid(row=0, column=2, sticky=W, padx=700)

close1=PhotoImage(file=path+"images\\close-1.png")
close2=PhotoImage(file=path+"images\\close-2.png")
minimize=PhotoImage(file=path+"images\\minimize.png")
maximize=PhotoImage(file=path+"images\\maximize.png")
Hide=PhotoImage(file=path+"images\\Hide.png")
Show=PhotoImage(file=path+"images\\Show.png")

Top=Frame(app, bd=2, bg="grey")
close=Button(Top, image=close1, bg="grey", bd=0,command=app.destroy)
close.grid(row=0, column=0)

size=Button(Top, image=maximize, bg='grey',bd=0 ,  command=big_screen)
size.grid(row=0, column=1)

hs=Button(Top, image=Hide, bg="grey", bd=0)
hs.grid(row=0, column=3)

title=Label(Top, text="Title", bg="grey", font=("Comic Sans MS", 12))
title.place(anchor=CENTER, relx=0.5, rely=0.5)
Top.pack(fill=X, side='top')

root=Frame(app, bd=2, bg='#d3d3d3')
Label(root, text="Contents!", bg='#d3d3d3', font="10").grid()
root.pack()

#Bindings
app.attributes("-topmost", True)
app.bind("<Key>", detect_key_press)
close.bind("<Enter>", enter_close)
close.bind("<Leave>", leave_close)
Top.bind("<B1-Motion>", move)
title.bind("<B1-Motion>", move)

app.mainloop()
