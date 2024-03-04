import tkinter as tk
from yml_configuration import Config
from tkinter import messagebox

class TkinterApp:
    def __init__(self, master):
        self.master = master
        self.config = Config("config.yml")

        self.button = tk.Button(self.master, text="Войти", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        try:
            message = self.config.get("Messages", "Error")
            messagebox.showerror("Error", message)
        except KeyError:
            messagebox.showerror("Error", "Error key not found in config.yml")

root = tk.Tk()
app = TkinterApp(root)
root.mainloop()