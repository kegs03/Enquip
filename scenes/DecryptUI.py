# decrypt_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from Ekrip import *

class DecryptUI(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=16)
        self.controller = controller

        self.word_var = tk.StringVar()
        self.key_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.encrypt_var = tk.StringVar()

        self._build_ui()

    def containKey(self):
        key = generateKey()
        self.key_var.set(key)

    def _build_ui(self):
        self.grid_rowconfigure(99, weight=1)  # spacer row
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="Word (encrypted or plain):").grid(row=0, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.word_var, width=40).grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0,8))

        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, columnspan=2, sticky="w", pady=(4,8))
        ttk.Button(button_frame, text="Decrypt", command=self.on_decrypt).grid(row=0, column=0, padx=(0,8))
        ttk.Button(button_frame, text="Encrypt", command=self.on_encrypt).grid(row=0, column=1)

        ttk.Label(self, text="Enter keycode (digits)").grid(row=3, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.key_var, width=20).grid(row=4, column=0, sticky="w", pady=(0, 8))

        ttk.Label(self, text="Output:").grid(row=5, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.output_var, width=40, state="readonly").grid(row=6, column=0, columnspan=2, sticky="ew")

        button_frame2 = ttk.Frame(self)
        button_frame2.grid(row=7, column=0, columnspan=2, sticky="w", padx=(0,8))
        ttk.Button(button_frame2, text="Settings", command=lambda: self.controller.show("SettingUI"), width=40).grid(row=0, column=0, columnspan=2, sticky="ew")

        for i in range(2):
            self.columnconfigure(i, weight=1)


    def on_decrypt(self):
        word = self.word_var.get()
        key = int(self.key_var.get())
        encrypted_word = self.encrypt_var.get()

        if not word:
            messagebox.showwarning("Missing input", "Please enter the encrypted word.")
            return

        try:
            decrypted = encrypt_word(encrypted_word, key)
            self.output_var.set(decrypted)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt: {e}")

    def on_encrypt(self):
        word = self.word_var.get().strip()
        key = self.key_var.get()

        if type(key) == str:
            key = generateKey()
        else:
            key = int(key)


        if not word:
            messagebox.showwarning("Missing input", "Please enter the plaintext word.")
            return

        try:
            self.key_var.set(key)
            encrypted = encrypt_word(word, key)
            self.output_var.set(encrypted)
            self.encrypt_var.set(encrypted)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt: {e}")


