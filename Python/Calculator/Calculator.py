from tkinter import *
import math
import sys

text_color = "tan"
back_color = "#292421"
expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def log():
    try:

        global expression

        expression = str(math.log10(float(expression)))

        equation.set(expression)

    except:
        equation.set("Cannot Log BEANS")
        expression = ""


def exponential():
    try:
        global expression

        expression = str(math.exp(float(expression)))

        equation.set(expression)

    except:

        equation.set("WHERE ARE MY BEANS!")
        expression = ""


def back():
    try:
        global expression

        length = len(expression)

        expression = str(expression[:-1])

        equation.set(expression)

    except:

        equation.set("CANNOT TAKE AWAY MY BEANS!")
        expression = ""


def calculate():
    try:

        global expression

        answer = str(eval(expression))

        equation.set(answer)

        expression = " "

    except:

        equation.set("UNABLE TO FIND BEANS!")
        expression = ""


if __name__ == "__main__":
    # Initialize GUI
    gui = Tk()

    gui.configure(background="grey10")

    gui.title("Calculator")

    gui.maxsize(323, 210)
    gui.minsize(323, 210)

    equation = StringVar()

    title_label = Label(gui, text="Calculator", font='Helvetica 18 bold', borderwidth=2, bg='tan')
    title_label.grid(row=0, column=0, columnspan=4, ipadx=100)

    expression_field = Entry(gui, textvariable=equation, fg='beige', bg='ivory4')

    expression_field.grid(row=1, column=0, columnspan=4, ipadx=100)

    # Create Buttons
    b1 = Button(gui, text='1', fg=text_color, bg=back_color, width=10,
                command=lambda: press(1))
    b1.grid(row=3, column=0)
    b2 = Button(gui, text='2', fg=text_color, bg=back_color, width=10,
                command=lambda: press(2))
    b2.grid(row=3, column=1)
    b3 = Button(gui, text='3', fg=text_color, bg=back_color, width=10,
                command=lambda: press(3))
    b3.grid(row=3, column=2)
    b4 = Button(gui, text='4', fg=text_color, bg=back_color, width=10,
                command=lambda: press(4))
    b4.grid(row=4, column=0)
    b5 = Button(gui, text='5', fg=text_color, bg=back_color, width=10,
                command=lambda: press(5))
    b5.grid(row=4, column=1)
    b6 = Button(gui, text='6', fg=text_color, bg=back_color, width=10,
                command=lambda: press(6))
    b6.grid(row=4, column=2)
    b7 = Button(gui, text='7', fg=text_color, bg=back_color, width=10,
                command=lambda: press(7))
    b7.grid(row=5, column=0)
    b8 = Button(gui, text='8', fg=text_color, bg=back_color, width=10,
                command=lambda: press(8))
    b8.grid(row=5, column=1)
    b9 = Button(gui, text='9', fg=text_color, bg=back_color, width=10,
                command=lambda: press(9))
    b9.grid(row=5, column=2)
    b0 = Button(gui, text='0', fg=text_color, bg=back_color, width=10,
                command=lambda: press(0))
    b0.grid(row=6, column=1)
    b_equals = Button(gui, text='=', fg='yellow', bg=back_color, width=10,
                      command=lambda: calculate())
    b_equals.grid(row=7, column=3)
    b_clear = Button(gui, text='Clear', fg='darkred', bg=back_color, width=10,
                     command=lambda: clear())
    b_clear.grid(row=8, column=3)
    b_add = Button(gui, text='+', fg=text_color, bg=back_color, width=10,
                   command=lambda: press("+"))
    b_add.grid(row=3, column=3)
    b_subtract = Button(gui, text='-', fg=text_color, bg=back_color, width=10,
                        command=lambda: press("-"))
    b_subtract.grid(row=4, column=3)
    b_multiply = Button(gui, text='*', fg=text_color, bg=back_color, width=10,
                        command=lambda: press("*"))
    b_multiply.grid(row=5, column=3)
    b_division = Button(gui, text='/', fg=text_color, bg=back_color, width=10,
                        command=lambda: press("/"))
    b_division.grid(row=6, column=3)
    b_point = Button(gui, text='.', fg=text_color, bg=back_color, width=10,
                     command=lambda: press("."))
    b_point.grid(row=6, column=2)
    b_sqrd = Button(gui, text='x^', fg=text_color, bg=back_color, width=10,
                    command=lambda: press("**"))
    b_sqrd.grid(row=7, column=2)
    b_sqrt = Button(gui, text='_/x', fg=text_color, bg=back_color, width=10,
                    command=lambda: press("**0.5"))
    b_sqrt.grid(row=7, column=1)
    b_openbracket = Button(gui, text='(', fg=text_color, bg=back_color, width=10,
                           command=lambda: press("("))
    b_openbracket.grid(row=8, column=1)
    b_closedbracket = Button(gui, text=')', fg=text_color, bg=back_color, width=10,
                             command=lambda: press(")"))
    b_closedbracket.grid(row=8, column=2)
    b_log = Button(gui, text='Log10', fg=text_color, bg=back_color, width=10,
                   command=lambda: log())
    b_log.grid(row=8, column=0)
    b_expo = Button(gui, text='e', fg=text_color, bg=back_color, width=10,
                    command=lambda: exponential())
    b_expo.grid(row=7, column=0)
    b_back = Button(gui, text='<-', fg=text_color, bg=back_color, width=10,
                    command=lambda: back())
    b_back.grid(row=6, column=0)

    gui.mainloop()
