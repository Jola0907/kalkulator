def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    if b == 0:
        return "Błąd! Nie można dzielić przez zero."
    return a / b


def potega(a, b):
    return a ** b


# Funkcja obsługująca wybór operacji
def kalkulator():
    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")

    wybor = input("Wybierz numer operacji (1/2/3/4/5): ")

    if wybor not in ['1', '2', '3', '4', '5']:
        print("Błędny wybór!")
        return

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


# Uruchomienie kalkulatora
kalkulator()
