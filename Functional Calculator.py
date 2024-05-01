#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox

def on_button_click(key):
    current = entry.get()
    if key == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "DEL":
        entry.delete(len(current)-1)
    else:
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Helvetica", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("DEL", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("/", 4, 2), ("*", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("=", 5, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=("Helvetica", 14), command=lambda key=text: on_button_click(key), bd=5)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(6):
    root.rowconfigure(i, weight=1)

for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()


# In[ ]:




