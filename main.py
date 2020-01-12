import tkinter


class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.configure(background='#f5f5f5')
        self.geometry("{0}x{1}+0+0".format(int(self.winfo_screenwidth() * 0.5), int(self.winfo_screenheight() * 0.5)))
        self.bind('<Escape>', lambda e: self.destroy())

        self.title("Calculator")


if __name__ == '__main__':
    app = Application()
    app.mainloop()