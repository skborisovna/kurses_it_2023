from tkinter import *
import random

def fon1():
    c.config(bg = 'blue')
def fon2():
    c.configure(bg='black')
window=Tk()
window.title("my_image")
window.geometry("500x500")

c=Canvas(width=500, height=500, bg='black')
c.pack()
c.create_oval(250,10,290,50, fill='gold', outline='white')
c.create_rectangle(80,100,220,200, fill='lightblue')
c.create_polygon(150,50,250,100,50,100, fill="lightyellow", outline="lightblue")

i=0
while i<300:
    c.create_arc(i,250,(i+40),170,start=90, extent=93, style=ARC, outline='green', width=2)
    i+=10
j=1
while j<300:
    c.create_line(j,350,j,250, width=2, fill = 'white')
    j+=10
b = Button(window, text = 'фон синій',command = fon1)
b.place(x = 350, y = 100)
button1=Button(window, text= "black", font=('Helvetica 10'), command=fon2)
button1.place(x=350,y=150)
window.mainloop()
