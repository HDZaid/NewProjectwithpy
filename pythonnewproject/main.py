from tkinter import font, messagebox
from tkinter import *
import random
import sys

def obvio():
    messagebox.showinfo(message = "sabia que aceptarias :3 ahora somos amig@s por SIEMPRE :D", title="")
    root.destroy() 
    
def Button_hover(event):
    X = random.randint(10,800)
    Y = random.randint(10,400)
    my_button2.place(x=X, y=Y)
    
def exit_(event):
    X = random.randint(10,800)
    Y = random.randint(10,400)
    my_button2.place(x=X, y=Y)
    
def on_closing():
    #messagebox.showinfo(message="¡SABIA QUE LO INTENTARIAS, CONTESTA LA PREGUNTA POR FAVOR :c !", title="")
    pass

root = Tk ()
root.geometry("900x500")
root.configure(background='#F4D03F')
root.title('RESPONDEME')

label_0 = Label(root, text= "¿QUIERES SER MI AMIG@?", bg = '#F4D03F', fg = 'black', width=0, font=("Comic Sans MS", 40))
label_0.place(x=100, y=70)

my_button1 = Button(root, text="CHI UꞷU", width=7, height=1, font=("Comic Sans MS", 30), bg = '#FF4141', fg='white', command=obvio)
my_button1.place(x=200, y=220)

my_button2 = Button(root, text="ÑO", width=5, height=1, font=("Comic Sans MS", 30), bg = '#FF4141', fg='white')
my_button2.place(x=550, y=220)

my_button2.bind("<Enter>", Button_hover)
my_button2.bind("<Leave>", exit_)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

sys.exit(0)