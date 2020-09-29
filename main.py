import tkinter as tk
import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv}

root = tk.Tk()
root.title("Alex CalcIt A.003")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

expression = ''


def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)


def eval_(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def button_click(number):
    entry.insert('end', number)


def clear():
    global expression
    entry.delete(0, 'end')
    expression = ''


def add():
    global expression
    if expression:
        expression += '+'
        return
    try:
        current = entry.get()
        expression += current
        expression += '+'
        entry.delete(0, 'end')
    except ValueError:
        pass


def subtract():
    global expression
    try:
        current = entry.get()
        expression += current
        expression += '-'
        entry.delete(0, 'end')
    except ValueError:
        pass


def multiply():
    global expression
    try:
        current = entry.get()
        expression += current
        expression += '*'
        entry.delete(0, 'end')
    except ValueError:
        pass


def divide():
    global expression
    try:
        current = entry.get()
        expression += current
        expression += '/'
        entry.delete(0, 'end')
    except ValueError:
        pass


def result():
    global expression
    try:
        last = entry.get()
        expression += last
        entry.delete(0, 'end')
        res = eval_expr(expression)
        entry.insert('end', res)
        expression = ''
        expression += res
    except (ValueError, TypeError):
        pass


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
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=clear)

button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=multiply)
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=divide)

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

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
