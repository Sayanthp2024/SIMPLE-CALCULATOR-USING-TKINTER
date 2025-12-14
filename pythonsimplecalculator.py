import tkinter as tk

def calculate():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        op = operation.get()

        if op == "Add":
            result.set(x + y)
        elif op == "Subtract":
            result.set(x - y)
        elif op == "Multiply":
            result.set(x * y)
        elif op == "Divide":
            result.set("Error" if y == 0 else x / y)
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

operation = tk.StringVar(value="Add")
tk.OptionMenu(root, operation, "Add", "Subtract", "Multiply", "Divide").pack()

tk.Button(root, text="Calculate", command=calculate).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
