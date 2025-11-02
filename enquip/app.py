import tkinter as tk
import sys
import os
from tkinter import ttk
from .scenes.DecryptUI import DecryptUI
from .scenes.SettingUI import SettingUI

def run():
    root = tk.Tk()
    root.title("Enquip")

    icon_path = resource_path("enquip/assets/icon.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    container = ttk.Frame(root, padding=0)
    container.grid(sticky="nsew")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frames = {}
    for FrameClass in (DecryptUI, SettingUI):
        f = FrameClass(container, controller=SimpleController(frames, root))
        frames[FrameClass.__name__] = f
        f.grid(row=0, column=0, sticky="nsew")

    sc = SimpleController(frames, root)
    for f in frames.values():
        f.controller = sc

    sc.show("DecryptUI")
    root.mainloop()

class SimpleController:
    def __init__(self, frames, root):
        self.frames = frames
        self.root = root

    def show(self, name: str):
        self.frames[name].tkraise()

def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, rel)
