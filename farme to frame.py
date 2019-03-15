from tkinter import *
def raise_frame(frame):
    frame.tkraise()
root=Tk()
f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)
for frame in (f1,f2,f3,f4):
    frame.grid(row=0,column=0,sticky='News')

Button(f1,text='Go to Frame', command=lambda:raise_frame(f2)).pack()
Label(f1,text="Frame1").pack()

Label(f2,text="Frame2").pack()
Button(f2,text='Go to Frame3', command=lambda:raise_frame(f3)).pack()

Label(f3,text="Frame3").pack()
Button(f3,text='Go to Frame4', command=lambda:raise_frame(f4)).pack()

Label(f4,text="Frame4").pack()
Button(f4,text='Go to Frame4', command=lambda:raise_frame(f4)).pack()

raise_frame(f1)
root.mainloop()