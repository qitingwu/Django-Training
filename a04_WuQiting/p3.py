# name: Qiting Wu   netId: qitwu    Student ID: 112064080
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry("200x180")

expre = StringVar()
expre.set('0')

expression = Label(root,textvariable=expre)
expression.grid(row=1, column=0,rowspan=1,columnspan=12,sticky="E", padx=5, pady=5)

def append_num(num):
    if expre.get()[-1] == ")":
        messagebox.showerror("Error", "Number cannot be right after )")
        return
    if expre.get() == '0':
        expre.set(num)
    else:
        expre.set(expre.get() + num)

def append_sym(sym):
    if sym == '(' and expre.get()[-1] in '+-*/(':
        expre.set(expre.get() + sym)
    elif sym == ')' and expre.get()[-1] in '0123456789)':
        if expre.get().count('(') > expre.get().count(')'):
            expre.set(expre.get() + sym)
        else:
            messagebox.showerror("Error", "Unbalanced parentheses!")
    elif sym in '+-*/' and not expre.get()[-1] in '+-*/(':
        expre.set(expre.get() + sym)
    else:
        messagebox.showerror("Error", "Invalid syntax!")

def delete():
    if expre.get() != '0':
        expre.set(expre.get()[0:-1])
    if len(expre.get()) == 1:
        expre.set("0")

def calculate():
    try:
        expre.set(eval(expre.get()))
    except:
        messagebox.showerror("Error", "Invalid syntax!")

zero = Button(root, text = "0", command=lambda: append_num("0"))
zero.grid(row = 2, column = 0, rowspan=1, columnspan=3,sticky="NSWE")
one = Button(root, text = "1", command=lambda: append_num("1"))
one.grid(row = 2, column = 3, rowspan=1, columnspan=3,sticky="NSWE")
two = Button(root, text = "2", command=lambda: append_num("2"))
two.grid(row = 2, column = 6, rowspan=1, columnspan=3,sticky="NSWE")
three = Button(root, text = "3", command=lambda: append_num("3"))
three.grid(row = 2, column = 9, rowspan=1, columnspan=3,sticky="NSWE")
four = Button(root, text = "4", command=lambda: append_num("4"))
four.grid(row = 3, column = 0, rowspan=1, columnspan=3,sticky="NSWE")
five = Button(root, text = "5", command=lambda: append_num("5"))
five.grid(row = 3, column = 3, rowspan=1, columnspan=3,sticky="NSWE")
six = Button(root, text = "6", command=lambda: append_num("6"))
six.grid(row = 3, column = 6, rowspan=1, columnspan=3,sticky="NSWE")
seven = Button(root, text = "7", command=lambda: append_num("7"))
seven.grid(row = 3, column = 9, rowspan=1, columnspan=3,sticky="NSWE")
eight = Button(root, text = "8", command=lambda: append_num("8"))
eight.grid(row = 4, column = 0, rowspan=1, columnspan=3,sticky="NSWE")
nine = Button(root, text = "9", command=lambda: append_num("9"))
nine.grid(row = 4, column = 3, rowspan=1, columnspan=3,sticky="NSWE")
left = Button(root, text = "(", command=lambda: append_sym("("))
left.grid(row = 4, column = 6, rowspan=1, columnspan=3,sticky="NSWE")
right = Button(root, text = ")", command=lambda: append_sym(")"))
right.grid(row = 4, column = 9, rowspan=1, columnspan=3,sticky="NSWE")
plus = Button(root, text = "+", command=lambda: append_sym("+"))
plus.grid(row = 5, column = 0, rowspan=1, columnspan=3,sticky="NSWE")
minus = Button(root, text = "-", command=lambda: append_sym("-"))
minus.grid(row = 5, column = 3, rowspan=1, columnspan=3,sticky="NSWE")
mult = Button(root, text = "*", command=lambda: append_sym("*"))
mult.grid(row = 5, column = 6, rowspan=1, columnspan=3,sticky="NSWE")
div = Button(root, text = "/", command=lambda: append_sym("/"))
div.grid(row = 5, column = 9, rowspan=1, columnspan=3,sticky="NSWE")
clear = Button(root, text = "CLEAR", command=lambda: expre.set("0"))
clear.grid(row = 6, column = 0, rowspan=1, columnspan=4,sticky="NSWE")
calc = Button(root, text = "CALC", command=lambda: calculate())
calc.grid(row = 6, column = 4, rowspan=1, columnspan=4,sticky="NSWE")
dele = Button(root, text = "DEL", command=lambda: delete())
dele.grid(row = 6, column = 8, rowspan=1, columnspan=4,sticky="NSWE")


for i in range(12):
    root.columnconfigure(i, weight=1)
for i in range(1,7):
    root.rowconfigure(0, weight=1)

root.mainloop()