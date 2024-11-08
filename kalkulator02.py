import math  # Importowanie biblioteki math do obliczeń matematycznych

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

# Funkcja obsługująca wybór operacji
def kalkulator():
    print("Zaawansowany kalkulator matematyczny")
    print
