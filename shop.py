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
            lable5=tk.Label(lable4,text=item['name'], font=('Arial',14))
            lable5.pack(side='left',padx=10)
            lable6=tk.Label(lable4,text=f"{item['price']} грн.", font=('Arial',14))
            lable6.pack(side='left',padx=10)
            lable7=tk.Button(lable4,text='добавить в корзину ',command=lambda i=item:self.add(i))
            lable7.pack(side='right')
    def update_cap(self):
        for widget in self.lable1.winfo_children():
            widget.destroy()
        for item in self.cart:
            lable4=tk.Frame(self.lable1)
            lable4.pack(fill='x',pady=5)
            lable5=tk.Label(lable4,text=item['name'],font=('Ariel',14))
            lable5.pack(side='left',padx=10)
            lable6=tk.Label(lable4,text=f"{item['price']}грн", font=('Ariel',14))
            lable6.pack(side='left',padx=10)
            lable17=tk.Button(lable4,text='убрать',command=lambda i=item:self.delet(i))
            lable17.pack(side='right')
        self.lable2.config(text=f"total price:{self.total}грн")
    def add(self,item):
        self.cart.append(item)
        self.total +=item['price']
        self.update_cap()
    def delet(self,item):
        self.cart.remove(item)
        self.total -=item['price']
        self.update_cap()
    def checkout(self):
        if self.cart:
            messagebox.showinfo('оформление заказа',f'ваш заказа на суму {self.total}грн.оформлен')
            self.cart=[]
            self.total=0
            self.update_cap()
        else:
            messagebox.showwarning('ошыбка','ваша корзина пустая')









if __name__ =='__main__':
    q=tk.Tk()
    app=shop(q)
    q.mainloop()