from tkinter import *

def button_click(char):
    global expression
    expression = expression + str(char)
    input_field.set(expression)

def button_clear():
    global expression
    expression = ""
    input_field.set(expression)

def button_equal():
    try:
        global expression
        result = str(eval(expression))
        input_field.set(result)
        expression = result
    except:
        input_field.set("Error")

expression = ""

calculator = Tk()
calculator.title("Simple Calculator")

input_field = StringVar()
input_entry = Entry(calculator, font=('arial', 16, 'bold'), textvariable=input_field, width=35, borderwidth=5)
input_entry.grid(columnspan=4, ipadx=70)

button_7 = Button(calculator, text='7', padx=16, pady=8, command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(calculator, text='8', padx=16, pady=8, command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(calculator, text='9', padx=16, pady=8, command=lambda: button_click(9)).grid(row=1, column=2)
button_div = Button(calculator, text='/', padx=16, pady=8, command=lambda: button_click('/')).grid(row=1, column=3)

button_4 = Button(calculator, text='4', padx=16, pady=8, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(calculator, text='5', padx=16, pady=8, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(calculator, text='6', padx=16, pady=8, command=lambda: button_click(6)).grid(row=2, column=2)
button_mul = Button(calculator, text='*', padx=16, pady=8, command=lambda: button_click('*')).grid(row=2, column=3)

button_1 = Button(calculator, text='1', padx=16, pady=8, command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(calculator, text='2', padx=16, pady=8, command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(calculator, text='3', padx=16, pady=8, command=lambda: button_click(3)).grid(row=3, column=2)
button_sub = Button(calculator, text='-', padx=16, pady=8, command=lambda: button_click('-')).grid(row=3, column=3)

button_0 = Button(calculator, text='0', padx=16, pady=8, command=lambda: button_click(0)).grid(row=4, column=0)
button_dot = Button(calculator, text='.', padx=16, pady=8, command=lambda: button_click('.')).grid(row=4, column=1)
button_clear = Button(calculator, text='C', padx=16, pady=8, command=button_clear).grid(row=4, column=2)
button_add = Button(calculator, text='+', padx=16, pady=8, command=lambda: button_click('+')).grid(row=4, column=3)

button_equal = Button(calculator, text='=', padx=16, pady=8, command=button_equal).grid(row=4, column=4)

calculator.mainloop()

