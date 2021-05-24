from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import random
import string

SYMBOLS = string.punctuation
NUMBERS = string.digits
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.has_symbols = IntVar()
        self.has_uppercase = IntVar()
        self.has_lowercase = IntVar()
        self.has_numbers = IntVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='Password Generator')
        self.label.grid(row=0, column=0, ipadx=40, ipady=15)

        self.symbols = tk.Checkbutton(self, variable=self.has_symbols)
        self.symbols["text"] = "! @ # $ % ^ & * () [] "
        self.symbols.grid(row=1, column=0, ipadx=40, ipady=2)

        self.uppercase = tk.Checkbutton(self, variable=self.has_uppercase)
        self.uppercase["text"] = "A B C D E..."
        self.uppercase.grid(row=2, column=0, ipadx=40, ipady=2)

        self.lowercase = tk.Checkbutton(self, variable=self.has_lowercase)
        self.lowercase["text"] = "a b c d e..."
        self.lowercase.grid(row=3, column=0, ipadx=40, ipady=2)

        self.numbers = tk.Checkbutton(self, variable=self.has_numbers)
        self.numbers["text"] = "1 2 3 4 5 6 7 8 9 0"
        self.numbers.grid(row=4, column=0, ipadx=40, ipady=2)

        self.pl_label = tk.Label(self, text='Password length (5-45)')
        self.pl_label.grid(row=5, column=0, ipadx=40)

        self.password_length = tk.Spinbox(self, from_=5.0, to=20.0)
        self.password_length.grid(row=6, column=0, ipady=2)

        self.generate = tk.Button(self)
        self.generate["text"] = "Generate Password"
        self.generate["command"] = self.generate_password
        self.generate.grid(row=7, column=0, ipadx=40, ipady=10)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=9, column=0, ipadx=40)

    def generate_password(self):
        self.generate = set()

        if self.has_symbols.get() == 1:
            self.generate.update(SYMBOLS)

        if self.has_uppercase.get() == 1:
            self.generate.update(UPPERCASE)

        if self.has_lowercase.get() == 1:
            self.generate.update(LOWERCASE)

        if self.has_numbers.get() == 1:
            self.generate.update(NUMBERS)

        if len(self.generate) == 0:
            tk.messagebox.showerror("Password Generator", "Password cannot be empty")
            return
        elif int(self.password_length.get()) < 5 or int(self.password_length.get()) > 45:
            tk.messagebox.showerror("Password Generator", "Password must be between 5-45 characters long")
            return
        else:
            self.password = random.choices(tuple(self.generate), k=int(self.password_length.get()))
            # Convert password to a string 
            self.password = ''.join([str(c) for c in self.password])
        
        tk.messagebox.showinfo("Password Created", f"Your Password is: {self.password}")
        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy)
        self.copy_button.grid(row=8, column=0, ipadx=40)

    def copy(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.password)
        self.master.update()
        tk.messagebox.showinfo("Password Generator", "Password Copied to Clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("215x310") 
app = Application(master=root)
app.mainloop()
