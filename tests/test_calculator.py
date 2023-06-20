import pytest
from tkinter import Tk, Label, Button

def test_addition():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test addition
    clear()
    show("5")
    show("+")
    show("3")
    calculate()
    result = Label_result.cget("text")
    assert result == 8

    clear()
    show("2")
    show("5")
    show("+")
    show("5")
    show("7")
    calculate()
    result = Label_result.cget("text")
    assert result == 82

    clear()
    show("4")
    show("2")
    show("5")
    show("+")
    show("3")
    show("7")
    show("1")
    show("+")
    show("2")
    show("9")
    show("3")
    show("4")
    show("4")
    show("+")
    show("9")
    show("6")
    show("7")
    show("+")
    show("1")
    show("2")
    show("4")
    show("8")
    show("5")
    show("+")
    show("5")
    show("7")
    show("5")
    show("+")
    show("5")
    show("7")
    calculate()
    result = Label_result.cget("text")
    assert result == 44224


def test_subtraction():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test subtraction
    clear()
    show("9")
    show("2")
    show("-")
    show("4")
    show("8")
    calculate()
    result = Label_result.cget("text")
    assert result == 44

    clear()
    show("4")
    show("2")
    show("0")
    show("-")
    show("1")
    show("6")
    show("7")
    show("2")
    calculate()
    result = Label_result.cget("text")
    assert result == -1252

    clear()
    show("6")
    show("9")
    show("9")
    show("-")
    show("6")
    show("9")
    show("9")
    calculate()
    result = Label_result.cget("text")
    assert result == 0


def test_multiplication():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test multiplication 

    clear()
    show("7")
    show("0")
    show("1")
    show("*")
    show("2")
    show("1")
    show("1")
    calculate()
    result = Label_result.cget("text")
    assert result == 147911

    clear()
    show("7")
    show("*")
    show("1")
    show("*")
    show("2")
    show("*")
    show("1")
    calculate()
    result = Label_result.cget("text")
    assert result == 14

    clear()
    show("7")
    show("2")
    show("9")
    show("*")
    show("2")
    show("1")
    show("1")
    show("*")
    show("1")
    show("6")
    show("*")
    show("2")
    show("7")
    show("7")
    calculate()
    result = Label_result.cget("text")
    assert result == 681725808


def test_division():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    clear()
    show("6")
    show("/")
    show("2")
    calculate()
    result = Label_result.cget("text")
    assert result == 3

    clear()
    show("7")
    show("/")
    show("3")
    calculate()
    result = Label_result.cget("text")
    assert result == 2.3333333333333335

    clear()
    show("9")
    show("/")
    show("9")
    calculate()
    result = Label_result.cget("text")
    assert result == 1

    clear()
    show("7")
    show("5")
    show("3")
    show("7")
    show("/")
    show("2")
    show("8")
    show("0")
    show("/")
    show("1")
    show("9")
    show("3")
    calculate()
    result = Label_result.cget("text")
    assert result == 0.13947076239822354


def test_clear():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test clear

    clear()
    show("7")
    show("5")
    show("3")
    show("7")
    show("/")
    show("2")
    show("8")
    show("0")
    show("/")
    show("1")
    show("9")
    show("3")
    clear()
    calculate()
    result = Label_result.cget("text")
    assert result == ""

    clear()
    show("7")
    show("*")
    show("1")
    show("*")
    show("2")
    show("*")
    show("1")
    clear()
    calculate()
    result = Label_result.cget("text")
    assert result == ""


def test_percentage():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                equation = equation.replace("%", "/100")
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test percentage
    clear()
    show("5")
    show("%")
    calculate()
    result = Label_result.cget("text")
    assert result == 0.05

    clear()
    show("1")
    show("0")
    show("0")
    show("%")
    calculate()
    result = Label_result.cget("text")
    assert result == 1


def test_square():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                equation = equation.replace("x²", "**2")
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test square
    clear()
    show("4")
    show("x²")
    calculate()
    result = Label_result.cget("text")
    assert result == 16

    clear()
    show("1")
    show("0")
    show("x²")
    calculate()
    result = Label_result.cget("text")
    assert result == 100

def test_equation():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                equation = equation.replace("%", "/100")
                equation = equation.replace("x²", "**2")
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    clear()
    show("2")
    show("4")
    show("+")
    show("6")
    show("8")
    show("*")
    show("5")
    show("/")
    show("3")
    calculate()
    result = Label_result.cget("text")
    assert result == 137.33333333333331

    clear()
    show("-")
    show("4")
    show("7")
    show("+")
    show("8")
    show("*")
    show("6")
    show("/")
    show("8")
    calculate()
    result = Label_result.cget("text")
    assert result == -41


def test_error():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                equation = equation.replace("%", "/100")
                equation = equation.replace("x²", "**2")
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    clear()
    show("%")
    show("2")
    show("%")
    calculate()
    result = Label_result.cget("text")
    assert result == "ERROR"


pytest.main()