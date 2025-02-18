import tkinter as tk

class Calculator:
    def __init__(self):
        self.myWin = tk.Tk()
        self.myWin.title("Calculator")
        self.myWin.geometry("300x250")

        # Entry widgets
        self.entry1 = tk.Entry(self.myWin, width=15)
        self.entry1.pack(pady=5)
        self.entry2 = tk.Entry(self.myWin, width=15)
        self.entry2.pack(pady=5)

        # Result variable
        self.result = tk.StringVar()
        self.result_label = tk.Label(self.myWin, textvariable=self.result, font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Buttons
        self.btn_frame = tk.Frame(self.myWin)
        self.btn_frame.pack(pady=5)

        self.btn_add = tk.Button(self.btn_frame, text="+", command=self.add)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        self.btn_subtract = tk.Button(self.btn_frame, text="-", command=self.subtract)
        self.btn_subtract.pack(side=tk.LEFT, padx=5)
        self.btn_multiply = tk.Button(self.btn_frame, text="x", command=self.multiply)
        self.btn_multiply.pack(side=tk.LEFT, padx=5)
        self.btn_divide = tk.Button(self.btn_frame, text="/", command=self.divide)
        self.btn_divide.pack(side=tk.LEFT, padx=5)

    def add(self):
        try:
            self.result.set(int(self.entry1.get()) + int(self.entry2.get()))
        except ValueError:
            self.result.set("Error")

    def subtract(self):
        try:
            self.result.set(int(self.entry1.get()) - int(self.entry2.get()))
        except ValueError:
            self.result.set("Error")

    def multiply(self):
        try:
            self.result.set(int(self.entry1.get()) * int(self.entry2.get()))
        except ValueError:
            self.result.set("Error")

    def divide(self):
        try:
            self.result.set(int(self.entry1.get()) / int(self.entry2.get()))
        except (ValueError, ZeroDivisionError):
            self.result.set("Error")

    def run(self):
        self.myWin.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()