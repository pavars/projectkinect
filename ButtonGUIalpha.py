from Tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

#top = Label(m2, text="top pane")
#m2.add(top)

#bottom = Label(m2, text="bottom pane")
#m2.add(bottom)


import tkMessageBox

def exerciseSelect1():
            execfile("vpycount.py")           

def exerciseSelect2():
           tkMessageBox.showinfo( "Exercise selection", "Exercise 2 activated")

def exerciseSelect3():
           tkMessageBox.showinfo( "Exercise selection", "Exercise 3 activated")

def exerciseSelect4():
           tkMessageBox.showinfo( "Exercise selection", "Exercise 4 activated")

B1 = Menubutton(left, text ="Exercise 1", relief=RAISED)
B1.grid()
B1.menu=Menu(B1,tearoff=0)
B1["menu"] = B1.menu
B1.menu.add_checkbutton(label="Biceps exercise 1", command=exerciseSelect1)

#B2 = Button(top, text ="Exercise 2", command = exerciseSelect2)
#B3 = Button(left, text ="Exercise 3", command = exerciseSelect3)
#B4 = Button(top, text ="Exercise 4", command = exerciseSelect4)

B1.pack()
#B2.pack()
#B3.pack()
#B4.pack()

mainloop()
