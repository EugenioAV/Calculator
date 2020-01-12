import tkinter
from tkinter import messagebox


class NumberButtons:
    buttons = []

    def __init__(self, tk, entry):
        self.input = entry
        self.get_buttons(tk)

    def get_buttons(self, tk):
        for i in range(0, 10):
            self.buttons.append(tkinter.Button(master=tk, text=i))
            self.buttons[i].config(command=lambda t=i, btn=self.buttons[i]: self.put_number(t))

    def draw_interface(self):
        column = 0
        row = 3
        for i in range(1, 10):
            self.buttons[i].grid(column=column, row=row, sticky='nesw')
            column += 1
            if i % 3 == 0:
                column = 0
                row -= 1
        self.buttons[0].grid(column=0, row=4, sticky='nesw')

    def put_number(self, i):
        self.input.config(state="normal")
        self.input.insert(tkinter.END, i)
        self.input.config(state="disabled")


class Operations:
    buttons = []

    def __init__(self, tk, entry):
        self.input = entry
        self.get_buttons(tk)

    def get_buttons(self, tk):
        operations = ['-', '+', '/', '*']
        for i, text in enumerate(operations):
            self.buttons.append(tkinter.Button(master=tk, text=text))
            self.buttons[i].config(command=lambda t=text, btn=self.buttons[i]: self.put_operation(t))

    def draw_interface(self):
        for i in range(0, 4):
            self.buttons[i].grid(column=3, row=i+1, sticky='nesw')

    def put_operation(self, operation):
        self.input.config(state="normal")
        self.input.insert(tkinter.END, operation)
        self.input.config(state="disabled")


class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.configure(background='#f5f5f5')
        self.bind('<Escape>', lambda e: self.destroy())

        self.title("Calculator")

        self.input = tkinter.Entry(justify=tkinter.CENTER, bd=2, state='disabled')
        self.numbers = NumberButtons(self, self.input)
        self.operations = Operations(self, self.input)
        self.result = tkinter.Button(text='=', command=self.get_result)
        self.ac = tkinter.Button(text='<-', command=self.ac_symbol)

    def draw_interface(self):
        self.input.grid(column=0, row=0, columnspan=4)
        self.result.grid(column=1, row=4, sticky='nesw')
        self.ac.grid(column=2, row=4, sticky='nesw')
        self.numbers.draw_interface()
        self.operations.draw_interface()

    def get_result(self):
        try:
            res = eval(self.input.get())
            self.input.config(state="normal")
            self.input.delete(0, tkinter.END)
            self.input.insert(0, res)
            self.input.config(state="disabled")
        except Exception:
            messagebox.showinfo("Error", "Invalid")

    def ac_symbol(self):
        self.input.config(state="normal")
        self.input.delete(len(self.input.get())-1, tkinter.END)
        self.input.config(state="disabled")


if __name__ == '__main__':
    app = Application()
    app.draw_interface()
    app.mainloop()
