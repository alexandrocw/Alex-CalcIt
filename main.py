import tkinter as tk

root = tk.Tk()
root.title("Alex CalcIt A.002")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

array = []


def button_click(number):
    entry.insert('end', number)

def button_clear():
    entry.delete(0, 'end')

def add():
    try:
        current = int(entry.get())
        array.append(current)
        entry.delete(0, 'end')
    except ValueError:
        entry.insert(0, "Insert Number First!")
        entry.delete(0, 'end')

def result():
    sum = 0
    current = int(entry.get())
    array.append(current)
    for num in array:
        sum+=num
    entry.delete(0, 'end')
    array.clear()
    entry.insert(0, sum)


# Make button

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=add)
button_equal = tk.Button(root, text="=", padx=90, pady=20, command=result)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)


# Show button on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
