from tkinter import *
from decimal import *

window = Tk()
window.title('Calculator')
window.geometry('350x250')  

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

panel = ''
lst = []

def calculator():
    global label
    global lst 
    num2 = Decimal(lst.pop())
    operand = lst.pop()
    num1 = Decimal(lst.pop())
    if operand == '+':
        res = num1 + num2
    elif operand == '-':
        res = num1 - num2
    elif operand == '/':
        res = num1 / num2
    elif operand == '*':
        res = num1 * num2

    label.configure(text = str(res))

def click(text):
    global lst
    global panel
    if text == 'CE':
        lst.clear()
        panel = ''
        label.configure(text = '0')
    elif '0' <= text <= '9':
        panel += text
        label.configure(text = panel)
    elif text == '.':
        if panel.find('.') == -1:
            panel += text 
            label.configure(text = panel)
    else:
        if len(lst) >= 2:
            lst.append(label['text'])
            calculator()
            lst.clear()
            lst.append(label['text'])
            panel = ''
            if text != '=':
                lst.append(text)
        else:
            if text != '=':
                lst.append(label['text'])
                lst.append(text)
                panel = ''
                label.configure(text = '0')

            

label = Label(window, text = '0', width = 100)
label.grid(row = 0, column =0, columnspan = 4, sticky = 'NSEW')

button = Button(window, text = 'CE', command = lambda text = 'CE': click(text))
button.grid(row = 2, column = 4, rowspan = 4, columnspan = 4, sticky = 'NSEW')
for row in range(4):
    for col in range(4):
        button = Button(window, text = buttons[row][col], command = lambda row=row, col = col: click(buttons[row][col]))
        button.grid(row = row + 2, column=col, sticky="NSEW")

window.rowconfigure(tuple(range(6)), weight=1)
window.columnconfigure(tuple(range(6)), weight=1)


window.mainloop()




