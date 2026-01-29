import tkinter as tk
from tkinter import ttk, messagebox
from forex_python.converter import CurrencyRates

c = CurrencyRates()
currency_list = ['USD', 'INR', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY']

def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()
        converted = c.convert(from_curr, to_curr, amount)
        result_var.set(f"{amount} {from_curr} = {round(converted, 2)} {to_curr}")
    except:
        messagebox.showerror("Error", "Check input or internet connection")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x350")
root.configure(bg="#f2f2f2")
root.resizable(False, False)

tk.Label(root, text="Currency Converter", font=("Helvetica", 16, "bold"), bg="#f2f2f2").pack(pady=20)
tk.Label(root, text="Amount", bg="#f2f2f2").pack()
entry_amount = tk.Entry(root, font=("Helvetica", 12))
entry_amount.pack(pady=5)

tk.Label(root, text="From Currency", bg="#f2f2f2").pack()
combo_from = ttk.Combobox(root, values=currency_list, font=("Helvetica", 12), state="readonly")
combo_from.set("USD")
combo_from.pack(pady=5)

tk.Label(root, text="To Currency", bg="#f2f2f2").pack()
combo_to = ttk.Combobox(root, values=currency_list, font=("Helvetica", 12), state="readonly")
combo_to.set("INR")
combo_to.pack(pady=5)

tk.Button(root, text="Convert", command=convert, bg="black", fg="white", font=("Helvetica", 12)).pack(pady=15)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Helvetica", 14, "bold"), bg="#f2f2f2", fg="green").pack(pady=10)

root.mainloop()