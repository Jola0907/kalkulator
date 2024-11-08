import sys #importowanie modułu sys, który pozwala na dostęp do niektórych zmiennych używanych lub utworzonych przez interpreter Python
from PyQt5.QtWidgets import * #importowanie wszystkich klas z modułu QtWidgets, które są niezbędne do tworzenia interfejsu użytkownika


class Calculator(QMainWindow): #Klasa Calculator dziedziczy po QMainWindow, co oznacza, że będzie to główne okno aplikacji.
    def __init__(self): #konstruktor klasy Calculator, który inicjalizuje główne okno aplikacji oraz wywołuje metodę initUI().
        super().__init__()
        self.initUI() #konstruktor który uruchamia konstruktor, inicjalizacja wyglądu

    def initUI(self): #metoda inicjalizująca interfejs użytkownika kalkulatora.

        self.setWindowTitle("Calculator") #Ustawia tytuł okna
        #tworzy pole tekstowe do wyświetlania wyników oraz tworzy layouty do organizacji przycisków. Na końcu ustawia główny widget jako centralny

        self.wynik_line_edit = QLineEdit() #utworzenie pola
        self.wynik_line_edit.setReadOnly(True)  #pole do odczytu
        self.wynik_line_edit.setFixedHeight(70) #wysokość

        self.grid_layout = QGridLayout() #siatka
        self.make_buttons() #tworzy przyciski kalkulatora, umieszcza je na siatce (grid layout) i łączy je z odpowiednią funkcją (metodą on_click), która zostanie wywołana po kliknięciu.
        self.pionowy_layout = QVBoxLayout()


        self.pionowy_layout.addWidget(self.wynik_line_edit)## potrzebny do okna w którym wprowadzana jest wartość kalkulatora
        self.pionowy_layout.addLayout(self.grid_layout)## potrzebny do wprowadzenia przycisków
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.pionowy_layout)#
        self.setCentralWidget(self.main_widget)#



    def make_buttons(self): #tworzymy siateke, lokalizacja przycisków
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('Bksp', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('=', 4, 1, 1, 2)
        ]

        for button in buttons: # połączenie tych przycisków z funkcją
            btn = QPushButton(button[0])
            if len(button) == 3:
                self.grid_layout.addWidget(btn, button[1], button[2])
            else:
                self.grid_layout.addWidget(btn, button[1], button[2], button[3], button[4]) # utworzenie przycisku =
            btn.clicked.connect(self.on_click)

    def on_click(self): #metoda wywoływana po kliknięciu przycisku kalkulatora. W zależności od wartości tekstowej przycisku podejmuje odpowiednie działania
        value = self.sender().text() #wyciągamy wartość tekstową z przycisku
        if value == "C":
            self.wynik_line_edit.clear() #czyszczenie, czyszczenie pola tekstowego
        elif value == "Bksp": #usuwanie ostatniego znaku
            aktualny_text = self.wynik_line_edit.text()
            self.wynik_line_edit.setText(aktualny_text[:-1])
        elif value == "=": #obliczanie wartości wyrażenia lub dodawanie wartości przycisku do pola tekstowego
            try:
                wynik = eval(self.wynik_line_edit.text())
                self.wynik_line_edit.setText(str(wynik))
            except Exception as e: #wyjątek
                self.wynik_line_edit.setText('Error')
        else:
            self.wynik_line_edit.setText(self.wynik_line_edit.text() + value)


if __name__=="__main__": #Główny blok kodu:
    app = QApplication(sys.argv)##Tworzenie aplikacji Qt: app = QApplication(sys.argv)
    calc = Calculator() #Tworzenie instancji klasy Calculator: calc = Calculator()
    calc.show() #Wyświetlanie okna aplikacji: calc.show()
    sys.exit(app.exec_()) #Uruchamianie głównej pętli aplikacji: sys.exit(app.exec_())













