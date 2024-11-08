import tkinter as tk
import math
import numpy as np
import sympy as sp

# Funkcja obliczająca wynik
def oblicz():
    try:
        # Pobranie wartości z pola tekstowego i obliczenie wyniku
        wynik = eval(entry.get())
        label_wynik.config(text=f"Wynik: {wynik}")
    except Exception as e:
        label_wynik.config(text=f"Błąd: {str(e)}")

# Funkcja dodawania liczby do pola wejściowego
def dodaj_tekst(tekst):
    entry.insert(tk.END, tekst)

# Funkcja czyszcząca pole wejściowe
def czysc():
    entry.delete(0, tk.END)

# Funkcja obliczająca funkcję matematyczną (pierwiastek, logarytm itd.)
def oblicz_matematyczny(funkcja):
    try:
        num = float(entry.get())
        if funkcja == "pierwiastek":
            wynik = math.sqrt(num)
        elif funkcja == "logarytm":
            if num <= 0:
                wynik = "Błąd! Logarytm z liczby <= 0"
            else:
                wynik = math.log(num)
        label_wynik.config(text=f"Wynik: {wynik}")
    except ValueError:
        label_wynik.config(text="Błąd! Wprowadź liczbę.")

# Funkcja do rozwiązywania równań za pomocą sympy
def rozwiaz_rownanie():
    try:
        x = sp.symbols('x')
        rownanie = sp.Eq(x**2 - 5*x + 6, 0)
        rozwiazanie = sp.solve(rownanie, x)
        label_wynik.config(text=f"Rozwiązanie: {rozwiazanie}")
    except Exception as e:
        label_wynik.config(text=f"Błąd: {str(e)}")

# Funkcja do różniczkowania
def rozniczkowanie():
    try:
        x = sp.symbols('x')
        funkcja = x**3 - 4*x**2 + 6*x - 2
        pochodna = sp.diff(funkcja, x)
        label_wynik.config(text=f"Pochodna: {pochodna}")
    except Exception as e:
        label_wynik.config(text=f"Błąd: {str(e)}")

# Funkcja do całkowania
def calkowanie():
    try:
        x = sp.symbols('x')
        funkcja = x**3 - 4*x**2 + 6*x - 2
        calka = sp.integrate(funkcja, x)
        label_wynik.config(text=f"Całka: {calka}")
    except Exception as e:
        label_wynik.config(text=f"Błąd: {str(e)}")

# Główne okno
root = tk.Tk()
root.title("Kalkulator z GUI")

# Pole wejściowe
entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# Przyciski kalkulatora
button_1 = tk.Button(root, text="1", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("1"))
button_2 = tk.Button(root, text="2", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("2"))
button_3 = tk.Button(root, text="3", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("3"))
button_4 = tk.Button(root, text="4", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("4"))
button_5 = tk.Button(root, text="5", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("5"))
button_6 = tk.Button(root, text="6", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("6"))
button_7 = tk.Button(root, text="7", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("7"))
button_8 = tk.Button(root, text="8", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("8"))
button_9 = tk.Button(root, text="9", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("9"))
button_0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("0"))

button_plus = tk.Button(root, text="+", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("+"))
button_minus = tk.Button(root, text="-", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("-"))
button_mnoz = tk.Button(root, text="*", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("*"))
button_dziel = tk.Button(root, text="/", width=5, height=2, font=("Arial", 14), command=lambda: dodaj_tekst("/"))

button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=czysc)
button_eq = tk.Button(root, text="=", width=5, height=2, font=("Arial", 14), command=oblicz)

# Przyciski do obliczeń matematycznych
button_pierwiastek = tk.Button(root, text="√", width=5, height=2, font=("Arial", 14), command=lambda: oblicz_matematyczny("pierwiastek"))
button_logarytm = tk.Button(root, text="ln", width=5, height=2, font=("Arial", 14), command=lambda: oblicz_matematyczny("logarytm"))
button_rozwiaz = tk.Button(root, text="Rozwiąż", width=5, height=2, font=("Arial", 14), command=rozwiaz_rownanie)
button_rozniczkowanie = tk.Button(root, text="Pochodna", width=5, height=2, font=("Arial", 14), command=rozniczkowanie)
button_calkowanie = tk.Button(root, text="Całka", width=5, height=2, font=("Arial", 14), command=calkowanie)

# Ustawienie przycisków w siatce
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_mnoz.grid(row=3, column=3)
button_dziel.grid(row=4, column=3)

button_clear.grid(row=5, column=0)
button_eq.grid(row=5, column=1, columnspan=2)

button_pierwiastek.grid(row=1, column=4)
button_logarytm.grid(row=2, column=4)
button_rozwiaz.grid(row=3, column=4)
button_rozniczkowanie.grid(row=4, column=4)
button_calkowanie.grid(row=5, column=4)

# Label do wyświetlania wyniku
label_wynik = tk.Label(root, text="Wynik: ", font=("Arial", 14))
label_wynik.grid(row=6, column=0, columnspan=5)

# Uruchomienie aplikacji
root.mainloop()
