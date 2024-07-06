import tkinter as tk
from tkinter import messagebox
import random
def qe():
    global random_number
    random_number=random.randint (1,100)
def er():
    try:
        number=int(lable4.get())
        if number<random_number:
           qr.config(text='число слишком маленькое', fg='red')
        elif number>random_number:
            qr.config(text='число слишком большое', fg='red')
        else:
            qr.config(text='вы угадали число', fg='green')
            messagebox.showinfo('вы угадали начните новую игру')
            qe()
    except ValueError:
        messagebox.showerror('пожайлуста водите числа')

def newgame():
    qe()
    lable4.delete(0,tk.END)
    qr.config(text='')

root=tk.Tk()
root.title('игра угадай число')
root.geometry('1000x1000')
lable1=tk.Frame(root,bg='#0000CD',bd=20)
lable1.pack(fill=tk.X)
lable2=tk.Label(lable1,text='угадайте число от 1-100',font=('Ariel',25,),bg='#0000CD')
lable2.pack(pady=10)
lable3=tk.Frame(root,bd=5)
lable3.pack(pady=20)
lable4=tk.Entry(lable3,font=('Ariel',25))
lable4.pack(pady=10)
button1=tk.Button(lable3,text='угадать',command=er,font=('Ariel',25),bg='#00FF00')
button1.pack(pady=10)
button2=tk.Button(lable3,text="новая игра",command=er,font=('Ariel',25),bg='#FFFF00')
button2.pack(pady=5)
qr=tk.Label(lable3,text='',font=('Ariel',25))
qr.pack(pady=10)







qe()
root.mainloop()