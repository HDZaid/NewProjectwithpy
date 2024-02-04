from tkinter import font, messagebox
from tkinter import *
import random

def obvio():
    messagebox.showinfo(message = "JAJAJA SABÍA QUE SI QUERIAS SER MI AMIGO :3", title="")
    root.destroy() 
    
def Button_hover(event):
    X = random.randint(10,700)
    Y = random.randint(10,400)
    my_button2.place(x=X, y=Y)
    
def exit_(event):
    X = random.randint(10,700)
    Y = random.randint(10,400)
    my_button2.place(x=X, y=Y)
    
def on_closing():
    # Esta función se llama cuando se intenta cerrar la ventana
    messagebox.showinfo(message="¡SABIA QUE LO INTENTARIAS, CONTESTA LA PREGUNTA POR FAVOR :c !", title="")

root = Tk ()
root.geometry("790x500")
root.configure(background='#F4D03F')
root.title('RESPONDEME')

label_0 = Label(root, text= "quieres ser mi amigo?", bg = '#F4D03F', fg = 'black', width=0, font=("Comic Sans MS", 40))
label_0.place(x=100, y=70)

my_button1 = Button(root, text="CHI UwU", width=7, height=1, font=("Comic Sans MS", 30), bg = '#FF4141', fg='white', command=obvio)
my_button1.place(x=150, y=220)

my_button2 = Button(root, text="ÑO UnU", width=7, height=1, font=("Comic Sans MS", 30), bg = '#FF4141', fg='white')
my_button2.place(x=450, y=220)

my_button2.bind("<Enter>", Button_hover)
my_button2.bind("<Leave>", exit_)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
