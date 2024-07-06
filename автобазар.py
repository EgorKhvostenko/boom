import tkinter as tk

from PIL import Image,ImageTk

root = tk.Tk()

root.title('автодром')
root.geometry('1920x1080')

label = tk.Label(root, text='автодром', font=('Ariel',20))
label.pack(pady=20)

lable1 = tk.Label(root, text='Продажа Mitsubishi ASX, 2012 год', font=('Ariel',20), anchor='w')
lable1.pack(fill='x', padx=1)

image=Image.open('download.jpg')
foto=ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=foto)
image_label.pack(pady=20)

lable2 = tk.Label(root, text='цена 12000$', font=('Ariel',15), anchor='w')
lable2.pack(fill='x', padx=1)

leble3 = tk.Label(root, text='Пробег   182 289 км', font=('Ariel',15), anchor='w')
leble3.pack(fill='x', padx=1)

lable4 = tk.Label(root, text='Двигатель бензин   1.8 л',font=('Ariel',15), anchor='w')
lable4.pack(fill='x', padx=1)

lable5 = tk.Label(root, text='Мощность   140 л.с',font=('Ariel',15), anchor='w')
lable5.pack(fill='x', padx=1)

def on_button_click():
    label6.config(text="куплена")

button = tk.Button(root, text='купить', command=on_button_click, font=('Ariel',15), anchor='w')
button.pack(anchor='w', padx=1, pady=15)

label6 = tk.Label(root, text='купить',font=('Ariel',15), anchor='w')
label6.pack(fill='x', padx=1)

lable8 = tk.Label(root, text='Subaru Outback 2018', font=('Ariel', 20), anchor='w')
lable8.pack(fill='x', padx=1)

label7 = tk.Label(root, text='61 тыс. км пробег', font=('Ariel', 15), anchor='w')
label7.pack(fill='x', padx=1)

lable9 = tk.Label(root, text='мощность 130 л.с', font=('Ariel',15), anchor='w')
lable9.pack(fill='x', padx=1)

lable10 = tk.Label(root, text='15 900 $', font=('Ariel',15), anchor='w')
lable10.pack(fill='x', padx=1)

def on_click_button():
    lable11.config(text='куплена')

button1 = tk.Button(root, text='купить', command=on_click_button, font=('Ariel',15), anchor='w')
button1.pack(anchor='w',padx=1, pady=15)

lable11 = tk.Label(root, text='купить', font=('Ariel',15),anchor='w')
lable11.pack(fill='x', padx=1)







root.mainloop()