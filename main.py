import tkinter as tk

class calculator:
    def __init__(self, q):
        self.q = q
        self.q.title('calculator')
        self.q.geometry('300x400')

        self.expression = ''
        self.text = tk.StringVar()
        self.text1 = tk.Frame(self.q, width=350, height=200)
        self.text1.pack(side=tk.TOP)
        self.text2 = tk.Entry(self.text1, font=('arial', 15), textvariable=self.text)
        self.text2.grid(row=0, column=0)
        self.text2.pack(ipady=12)
        self.button = tk.Frame(self.q, width=400, height=50, bg='grey')
        self.button.pack()
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]
        row = 0
        col = 0
        for button in buttons:
            if button == "=":
                btn = tk.Button(self.button, text=button, fg="black", width=10, height=3, bd=0, bg="#fff",
                                cursor="hand2", command=self.calculate)
            else:
                btn = tk.Button(self.button, text=button, fg="black", width=10, height=3, bd=0, bg="#fff",
                                cursor="hand2", command=lambda b=button: self.click(b))
            btn.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, item):
        if item == 'C':
            self.expression = ''
            self.text.set('')
        else:
            self.expression += str(item)
            self.text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.text.set(result)
            self.expression = result
        except :
            self.text.set('error')
            self.expression = ''










if __name__ == '__main__':
    q = tk.Tk()
    calculator(q)
    q.mainloop()