import math  # Importowanie biblioteki math do obliczeń matematycznych
import numpy as np  # Importowanie biblioteki numpy do operacji na macierzach


# Funkcja dodająca dwie liczby
def dodaj(a, b):
    return a + b


# Funkcja odejmująca dwie liczby
def odejmij(a, b):
    return a - b


# Funkcja mnożąca dwie liczby
def pomnoz(a, b):
    return a * b


# Funkcja dzieląca dwie liczby z kontrolą dzielenia przez zero
def podziel(a, b):
    if b == 0:
        return "Błąd! Nie można dzielić przez zero."
    return a / b


# Funkcja obliczająca potęgę
def potega(a, b):
    return a ** b


# Funkcja obliczająca pierwiastek kwadratowy z liczby
def pierwiastek(a):
    if a < 0:
        return "Błąd! Nie można obliczyć pierwiastka z liczby ujemnej."
    return math.sqrt(a)


# Funkcja obliczająca logarytm naturalny (logaritm o podstawie e)
def logarytm(a):
    if a <= 0:
        return "Błąd! Logarytm z liczby <= 0 nie jest możliwy."
    return math.log(a)


# Funkcje trygonometryczne
def sinus(a):
    return math.sin(math.radians(a))  # Przekształcenie kąta z stopni na radiany przed obliczeniem sinusa


def cosinus(a):
    return math.cos(math.radians(a))  # Przekształcenie kąta z stopni na radiany przed obliczeniem cosinusa


def tangens(a):
    return math.tan(math.radians(a))  # Przekształcenie kąta z stopni na radiany przed obliczeniem tangensa


# Funkcje z użyciem numpy
def dodaj_macierze():
    # Tworzymy dwie macierze 2x2
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    return np.add(A, B)  # Dodanie dwóch macierzy


def mnoz_macierze():
    # Tworzymy dwie macierze 2x2
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    return np.dot(A, B)  # Mnożenie dwóch macierzy


def odwrotność_macierzy():
    # Tworzymy macierz 2x2
    A = np.array([[1, 2], [3, 4]])
    return np.linalg.inv(A)  # Obliczenie odwrotności macierzy


# Funkcja obsługująca wybór operacji
def kalkulator():
    print("Zaawansowany kalkulator matematyczny")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Pierwiastek kwadratowy")
    print("7. Logarytm")
    print("8. Sinus (w stopniach)")
    print("9. Cosinus (w stopniach)")
    print("10. Tangens (w stopniach)")
    print("11. Dodawanie macierzy (2x2)")
    print("12. Mnożenie macierzy (2x2)")
    print("13. Obliczanie odwrotności macierzy (2x2)")

    wybor = input("Wybierz numer operacji (1-13): ")

    if wybor not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
        print("Błędny wybór!")
        return

    if wybor in ['1', '2', '3', '4', '5']:
        num1 = float(input("Podaj pierwszy numer: "))
        num2 = float(input("Podaj drugi numer: "))

    if wybor == '1':
        print(f"{num1} + {num2} = {dodaj(num1, num2)}")
    elif wybor == '2':
        print(f"{num1} - {num2} = {odejmij(num1, num2)}")
    elif wybor == '3':
        print(f"{num1} * {num2} = {pomnoz(num1, num2)}")
    elif wybor == '4':
        print(f"{num1} / {num2} = {podziel(num1, num2)}")
    elif wybor == '5':
        print(f"{num1} ^ {num2} = {potega(num1, num2)}")

    if wybor == '6':
        num = float(input("Podaj liczbę do obliczenia pierwiastka kwadratowego: "))
        print(f"Pierwiastek kwadratowy z {num} = {pierwiastek(num)}")
    elif wybor == '7':
        num = float(input("Podaj liczbę do obliczenia logarytmu: "))
        print(f"Logarytm naturalny z {num} = {logarytm(num)}")
    elif wybor == '8':
        kat = float(input("Podaj kąt w stopniach do obliczenia sinusa: "))
        print(f"Sinus z {kat}° = {sinus(kat)}")
    elif wybor == '9':
        kat = float(input("Podaj kąt w stopniach do obliczenia cosinusa: "))
        print(f"Cosinus z {kat}° = {cosinus(kat)}")
    elif wybor == '10':
        kat = float(input("Podaj kąt w stopniach do obliczenia tangensa: "))
        print(f"Tangens z {kat}° = {tangens(kat)}")

    if wybor == '11':
        print("Dodawanie macierzy:")
        print(dodaj_macierze())
    elif wybor == '12':
        print("Mnożenie macierzy:")
        print(mnoz_macierze())
    elif wybor == '13':
        print("Odwrotność macierzy:")
        print(odwrotność_macierzy())


# Uruchomienie kalkulatora
kalkulator()
