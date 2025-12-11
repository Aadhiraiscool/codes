import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")

window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")

description = tk.Label(window, text="This application multiplies two numbers.")
description.pack(pady=5)

label1 = tk.Label(window, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Calculate Product", command=calculate)
button.pack(pady=5)

result_box = tk.Text(window, height=2, width=30)
result_box.pack()

window.mainloop()
