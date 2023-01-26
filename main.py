import tkinter
from interface import Interface


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

    # надпись
    labelframe = tkinter.Frame(root, bg="black")
    labelframe.place(relheight=.19, rely=.01, relx=.01)
    label = tkinter.Label(labelframe, text="", font=28, foreground="white", background="black")
    label.pack()

    # кнопки
    inter = Interface(label, frame)

    inter.create_math_button("0", rely=.8)
    inter.create_math_button("1", rely=.6)
    inter.create_math_button("2", rely=.6, relx=.25)
    inter.create_math_button("3", rely=.6, relx=.5)
    inter.create_math_button("4", rely=.4)
    inter.create_math_button("5", rely=.4, relx=.25)
    inter.create_math_button("6", rely=.4, relx=.5)
    inter.create_math_button("7", rely=.2)
    inter.create_math_button("8", rely=.2, relx=.25)
    inter.create_math_button("9", rely=.2, relx=.5)
    inter.create_math_button(".", rely=.8, relx=.25)

    inter.create_math_button("+", rely=.8, relx=.75, background="#1B1BB3")
    inter.create_math_button("-", rely=.6, relx=.75, background="#1B1BB3")
    inter.create_math_button("*", rely=.4, relx=.75, background="#1B1BB3")
    inter.create_math_button("/", rely=.2, relx=.75, background="#1B1BB3")

    inter.create_math_button("(")
    inter.create_math_button(")", relx=.25)

    inter.create_math_button("=", command=inter.calculate, rely=.8, relx=.5, background="#FFE800")
    inter.create_math_button("c", inter.clear, relx=.5, background="#FF9200")
    inter.create_math_button("<-", inter.backspace, relx=.75, background="#FF9200")

    root.mainloop()
