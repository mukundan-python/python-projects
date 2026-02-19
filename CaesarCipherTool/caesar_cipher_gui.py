import tkinter as tk
from tkinter import messagebox

# ---------- Encryption Logic ----------

def text_to_cipher(text, key):
    code = ""
    key %= 26
    for i in text:
        if i.isupper():
            code += chr((ord(i)-ord("A") + key) % 26 + ord("A"))
        elif i.islower():
            code += chr((ord(i)-ord("a") + key) % 26 + ord("a"))
        else:
            code += i
    return code

def cipher_to_text(text, key):
    code = ""
    key %= 26
    for i in text:
        if i.isupper():
            code += chr((ord(i)-ord("A") - key) % 26 + ord("A"))
        elif i.islower():
            code += chr((ord(i)-ord("a") - key) % 26 + ord("a"))
        else:
            code += i
    return code

def process_text():
    mode = mode_var.get()
    text = text_entry.get()
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Key must be a number")
        return

    if mode == "Encrypt":
        result = text_to_cipher(text, key)
    else:
        result = cipher_to_text(text, key)

    result_label.config(text=result)

# ---------- GUI Setup ----------

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("450x300")
root.configure(bg="#d3e893")

tk.Label(root, text="Enter text:", bg="#d3e893", fg="#243b2c").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

tk.Label(root, text="Enter key (number):", bg="#d3e893", fg="#243b2c").pack(pady=5)
key_entry = tk.Entry(root, width=10)
key_entry.pack(pady=5)

mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt", bg="#d3e893").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt", bg="#d3e893").pack()

tk.Button(root, text="Process", command=process_text, bg="#f9eed6", fg="#243b2c").pack(pady=10)

tk.Label(root, text="Result:", bg="#d3e893", fg="#243b2c").pack()
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#d3e893", fg="#243b2c")
result_label.pack(pady=5)

root.mainloop()
