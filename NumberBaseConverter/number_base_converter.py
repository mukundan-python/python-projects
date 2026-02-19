import tkinter as tk
from tkinter import messagebox


# ---------- Conversion Logic ----------

def convert_base(value, from_base, to_base):
    decimal_value = int(value, from_base)

    if to_base == 2:
        return format(decimal_value, 'b')
    elif to_base == 16:
        return format(decimal_value, 'X')
    elif to_base == 10:
        return str(decimal_value)


# ---------- Conversion Handler ----------

def handle_conversion(from_base, to_base):
    value = entry.get().strip()

    if value == "":
        messagebox.showerror("Error", "Please enter a value.")
        return

    try:
        result = convert_base(value, from_base, to_base)
        result_label.config(text="Result: " + result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for selected base.")


# ---------- Individual Button Functions ----------

def binary_to_decimal():
    handle_conversion(2, 10)

def binary_to_hex():
    handle_conversion(2, 16)

def decimal_to_binary():
    handle_conversion(10, 2)

def decimal_to_hex():
    handle_conversion(10, 16)

def hex_to_decimal():
    handle_conversion(16, 10)

def hex_to_binary():
    handle_conversion(16, 2)


# ---------- GUI Setup ----------

root = tk.Tk()
root.title("Number Base Converter")
root.geometry("420x300")
root.configure(bg="#d3e893")

tk.Label(root, text="Enter value:", bg="#d3e893", fg="#243b2c").pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12),
                        bg="#d3e893", fg="#243b2c")
result_label.pack(pady=10)


# ---------- Buttons ----------

button_frame = tk.Frame(root, bg="#d3e893")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Binary → Decimal",
          width=18, command=binary_to_decimal).grid(row=0, column=0, padx=5, pady=5)

tk.Button(button_frame, text="Binary → Hex",
          width=18, command=binary_to_hex).grid(row=0, column=1, padx=5, pady=5)

tk.Button(button_frame, text="Decimal → Binary",
          width=18, command=decimal_to_binary).grid(row=1, column=0, padx=5, pady=5)

tk.Button(button_frame, text="Decimal → Hex",
          width=18, command=decimal_to_hex).grid(row=1, column=1, padx=5, pady=5)

tk.Button(button_frame, text="Hex → Decimal",
          width=18, command=hex_to_decimal).grid(row=2, column=0, padx=5, pady=5)

tk.Button(button_frame, text="Hex → Binary",
          width=18, command=hex_to_binary).grid(row=2, column=1, padx=5, pady=5)


root.mainloop()
