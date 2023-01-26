"""contains class Interface"""
import tkinter
from tkinter import messagebox


class Interface:
    """
    class to change the interface.
    contains functions for creating buttons and changing the string with the expression
    """

    def __init__(self, label: tkinter.Label, frame: tkinter.Frame):
        self.label = label
        self.__line = ''
        self.frame = frame

    @property
    def line(self):
        """Get and set expression"""
        return self.__line

    @line.setter
    def line(self, value: str):
        self.__line = value
        self.label.config(text=self.line)

    def create_math_button(self, text, /, command=None, rely=0., relx=0., background="#f0f0f0"):
        """creates a button on the frame that changes the line"""
        if command is None:
            command = self.standard_command(text)
        btn = tkinter.Button(self.frame, text=text, command=command, background=background, font=28)
        btn.place(relheight=.2, relwidth=.25, relx=relx, rely=rely)

    def clear(self):
        """clear the line"""
        self.line = ''

    def backspace(self):
        """removes the last character of the line"""
        self.line = self.line[:-1]

    def calculate(self):
        """replaces the line with the calculated value"""
        try:
            self.line = str(eval(self.line))
        except Exception as exc:
            messagebox.showerror(title="ошибка", message=str(exc))

    def standard_command(self, char):
        """returns a function that adds a character to a line"""
        def command():
            self.line += char
        return command
