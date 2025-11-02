from tkinter import ttk
import tkinter as tk

class SettingUI(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=16)
        self.controller = controller

        ttk.Label(self, text="Settings", font=("Segoe UI", 14, "bold")).pack(pady=8)
        ttk.Button(self, text="Say Hi",
                   command=lambda: controller.shared["msg"].set("Hi from Settings!")
                   ).pack(fill="x", pady=6)
        ttk.Button(self, text="← Back",
                   command=lambda: controller.show("DecryptUI")).pack(fill="x", pady=6)
