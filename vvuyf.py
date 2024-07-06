import tkinter as tk

class Calculator:
    def init(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")

        self.expression = ""

        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=25, bd=5, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.add_buttons()

    def add_buttons(self):
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
            btn = tk.Button(self.buttons_frame, text=button, width=5, height=2, bd=1, font=('arial', 18, 'bold'), command=lambda button=button: self.click(button))
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, item):
        if item == 'C':
            self.expression = ""
            self.input_text.set("")
        elif item == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Ошибка")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()