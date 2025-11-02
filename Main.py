from Enkrip.scenes.SettingUI import SettingUI
from Enkrip.scenes.DecryptUI import DecryptUI
from tkinter import ttk
import tkinter as tk

class SceneManger(ttk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.grid(sticky="nsew")
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (DecryptUI, SettingUI):
            frame = F(self, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show("DecryptUI")

    def show(self,name):
        self.frames[name].tkraise()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Enkrip")
    root.geometry("800x600")

    SceneManger(root)
    root.mainloop()

