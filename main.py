import tkinter
from tkinter import messagebox


def create_math_button(text, /, command=None, rely=0., relx=0., background="#f0f0f0"):
    if command is None:
        def command():
            global line
            line += text
            label.config(text=line)

    btn = tkinter.Button(frame, text=text, command=command, background=background)
    btn.place(relheight=.2, relwidth=.25, relx=relx, rely=rely)


def clear():
    global line
    line = ""
    label.config(text=line)


def backspace():
    global line
    line = line[:-1]
    label.config(text=line)


def calculate():
    global line
    try:
        line = str(eval(line))
    except Exception as e:
        messagebox.showerror(title="ошибка", message=str(e))
    label.config(text=line)


if __name__ == "__main__":
    root = tkinter.Tk()

    HEIGHT = 630
    WIDTH = 400
    line = ""

    root.title("Калькулятор")
    root["bg"] = "black"
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(width=False, height=False)

    canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH, background="black")
    canvas.pack()

    frame = tkinter.Frame(root, bg="white")
    frame.place(relheight=.8, relwidth=1, rely=.2)

    labelframe = tkinter.Frame(root, bg="black")
    labelframe.place(relheight=.2)
    label = tkinter.Label(labelframe, text="", font=28)
    label.pack()

    # кнопки
    create_math_button("0", rely=.8)
    create_math_button('1', rely=.6)
    create_math_button("2", rely=.6, relx=.25)
    create_math_button("3", rely=.6, relx=.5)
    create_math_button("4", rely=.4)
    create_math_button("5", rely=.4, relx=.25)
    create_math_button("6", rely=.4, relx=.5)
    create_math_button("7", rely=.2)
    create_math_button("8", rely=.2, relx=.25)
    create_math_button("9", rely=.2, relx=.5)
    create_math_button(".", rely=.8, relx=.25)

    create_math_button("+", rely=.8, relx=.75, background="blue")
    create_math_button("-", rely=.6, relx=.75, background="blue")
    create_math_button("*", rely=.4, relx=.75, background="blue")
    create_math_button("/", rely=.2, relx=.75, background="blue")

    create_math_button("(")
    create_math_button(")", relx=.25)

    create_math_button("=", command=calculate, rely=.8, relx=.5, background="yellow")
    create_math_button("c", clear, relx=.5, background="red")
    create_math_button("<-", backspace, relx=.75, background="red")

    root.mainloop()
