import tkinter as tk
from tkinter import messagebox
class shop:
    def __init__(self, q):
        self.q = q
        self.q.title = 'shop'
        self.q.geometry = ('300x400')

        self.items = [
            {'name':'apple','price':50},
            {'name':'orange','price':60},
            {'name':'milk','price':100}
]
        self.cart = []
        self.total = 0
        self.create_widgets()
    def create_widgets(self):
        self.lable=tk.Frame(self.q)
        self.lable.pack(pady=10,fill='x')
        self.lable1=tk.Frame(self.q)
        self.lable1.pack(pady=10,fill='x')
        self.lable2= tk.Label(self.q, text=f"Общая сумма: {self.total} грн.", font=("Arial", 14))
        self.lable2.pack(pady=10)
        self.lable3=tk.Button(self.q, text='оформить заказ',command=self.checkout)
        self.lable3.pack(pady=10)
        self.item_list()
        self.update_cap()
    def item_list(self):
        for widget in self.lable.winfo_children():
            widget.destroy()
        for item in self.items:
            lable4=tk.Frame(self.lable)
            lable4.pack(fill='x',pady=5)






if __name__ =='__main__':
    q=tk.Tk()
    app=shop(q)
    q.mainloop()