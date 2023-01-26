import tkinter
from tkinter import messagebox


class Interface:
    def __init__(self, label: tkinter.Label, frame: tkinter.Frame):
        self.label = label
        self.__line = ''
        self.frame = frame

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value: str):
        self.__line = value
        self.label.config(text=self.line)

    def create_math_button(self, text, /, command=None, rely=0., relx=0., background="#f0f0f0"):
        if command is None:
            command = self.standard_command(text)
        btn = tkinter.Button(self.frame, text=text, command=command, background=background, font=28)
        btn.place(relheight=.2, relwidth=.25, relx=relx, rely=rely)

    def clear(self):
        self.line = ''

    def backspace(self):
        self.line = self.line[:-1]

    def calculate(self):
        try:
            self.line = str(eval(self.line))
        except Exception as e:
            messagebox.showerror(title="ошибка", message=str(e))

    def standard_command(self, text):
        def command():
            self.line += text
        return command
