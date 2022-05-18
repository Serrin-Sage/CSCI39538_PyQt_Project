from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import sys


#********** KAPREKAR CONSTANT GENERATOR ********#
class Kaprekar(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())

        self.setWindowTitle("Kaprekar's Constant")
        # self.setGeometry(200, 200, 400, 400)
        self.intro_label = QLabel("\nFind out why 6174\nis a special number.\n", self)
        self.intro_label.setAlignment(Qt.AlignCenter)
        self.intro_label.setStyleSheet("QLabel"
            "{"
                "border: 2px solid black;"
                "background: white;"
            "}"
        )
        self.layout().addWidget(self.intro_label)

        self.intro_button = QPushButton('Start')
        self.intro_button.clicked.connect(self.start)
        self.layout().addWidget(self.intro_button)

    def start(self):
        self.intro_button.hide()

        self.entry_label = QLabel('Think of a four-digit number:', self)
        self.layout().addWidget(self.entry_label)

        self.entry_box = QLineEdit()
        self.layout().addWidget(self.entry_box)

        self.entry_button = QPushButton('Enter')
        self.entry_button.clicked.connect(self.enter)
        self.layout().addWidget(self.entry_button)

    def enter(self):
        entry = self.entry_box.displayText()

        def threeRepeating():
            count = {}

            for digit in entry:
              if digit in count:
                count[digit] += 1
                if count[digit] > 2:
                  return True
              else:
                count[digit] = 1
            return False

        if len(entry) == 4 and entry.isdigit():
            color_black = QGraphicsColorizeEffect()
            color_black.setColor(Qt.black)
            self.entry_label.setGraphicsEffect(color_black)
            if threeRepeating():
                self.entry_label.setText(f'Three digits cannot repeat.')
                color_red = QGraphicsColorizeEffect()
                color_red.setColor(Qt.red)
                self.entry_label.setGraphicsEffect(color_red)
            else:
                self.entry_box.hide()
                self.entry_button.hide()
                self.number = int(self.entry_box.displayText())
                self.entry_label.setAlignment(Qt.AlignRight)
                self.entry_label.setText(f'Starting number = {self.number}')

                self.cycle()

    def cycle(self):
        self.decreasing_button = QPushButton(f'Sort {self.number} in decreasing order')
        self.decreasing_button.clicked.connect(self.sortDecreasing)
        self.layout().addWidget(self.decreasing_button)

    def sortDecreasing(self):
        self.decreasing_button.hide()

        self.decreasing = int(''.join([str(digit) for digit in sorted([int(digit) for digit in str(self.number)], reverse=True)]))

        text = f'   {self.decreasing}'
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignRight)
        self.layout().addWidget(label)

        self.increasing_button = QPushButton(f'Sort {self.number} in increasing order')
        self.increasing_button.clicked.connect(self.sortIncreasing)
        self.layout().addWidget(self.increasing_button)

    def sortIncreasing(self):
        self.increasing_button.hide()

        self.increasing = int(str(self.decreasing)[::-1])

        text = '-  ' + str(self.increasing).rjust(4, ' ')
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignRight)
        self.layout().addWidget(label)

        self.subtract_button = QPushButton(f'Subtract: {self.decreasing} - {self.increasing}')
        self.subtract_button.clicked.connect(self.subtract)
        self.layout().addWidget(self.subtract_button)

    def subtract(self):
        self.subtract_button.hide()

        self.number = self.decreasing - self.increasing

        text = f'Resulting number = {self.number}'
        label = QLabel(text)
        label.setAlignment(Qt.AlignRight)

        if self.number == 6174:
            label.setStyleSheet("QLabel"
                "{"
                    "border: 2px solid black;"
                    "background: white;"
                "}"
            )
            self.layout().addWidget(label)
        else:
            self.layout().addWidget(label)
            self.cycle()

#********** PRIME NUMBER GENERATOR ********#
class PrimeNumGen(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.setLayout(QVBoxLayout())

        # Title
        self.setWindowTitle("Prime Number Generator")

        # setting geometry
        self.setGeometry(200, 200, 400, 400)

        # font
        font = QFont('Helvetica', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # Label
        self.label = QLabel("Enter a number ", self)
        # setting geometry to the label
        self.label.setGeometry(40, 85, 260, 60)
        # making the info label multi line
        self.label.setWordWrap(True)

        # setting font to the head
        self.label.setFont(font)
        # setting alignment of the head
        self.label.setAlignment(Qt.AlignCenter)
        # setting color effect to the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)

        # setting font and alignment
        self.label.setFont(QFont('Helvetica', 13))
        self.label.setAlignment(Qt.AlignCenter)

        # setting style sheet
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 2px solid black;"
                                 "background : lightgrey;"
                                 "}")

        self.layout().addWidget(self.label)
        # Entry Box
        entry_box = QLineEdit()
        entry_box.setObjectName("EntryBox")
        self.layout().addWidget(entry_box)

        # Buttons

        generate_btn = QPushButton(
            "Generate!", clicked=lambda: primeNumberGenerator())
        self.layout().addWidget(generate_btn)

        # reset button to reset the game, adding action to reset button
        reset_game = QPushButton(
            "Reset", clicked=lambda: reset_action(self))
        self.layout().addWidget(reset_game)

        # setting geometry to the push button
        reset_game.setGeometry(175, 280, 100, 40)

        # setting color effect
        color_red = QGraphicsColorizeEffect()
        color_red.setColor(Qt.red)
        reset_game.setGraphicsEffect(color_red)

        color_green = QGraphicsColorizeEffect()
        color_green.setColor(Qt.green)
        generate_btn.setGraphicsEffect(color_green)

        # Warning/Answer
        warning_label = QLabel("")
        warning_label.setFont(QFont('Helvetica', 24))
        self.layout().addWidget(warning_label)

        self.listWidget = QListWidget()

        def reset_action(self):

            self.label.setStyleSheet("QLabel"
                                     "{"
                                     "border : 2px solid black;"
                                     "background : lightgrey;"
                                     "}")

            # setting text to the info label
            self.label.setText("Reset...Enter a number")

            # empty output box
            self.listWidget.clear()

            # clear entry box
            entry_box.clear()

        def primeNumberGenerator():

            entry = entry_box.displayText()
            # making label green
            self.label.setStyleSheet("QLabel"
                                     "{"
                                     "border : 2px solid black;"
                                     "background : lightgrey;"
                                     "}")

            if entry != "":
                for x in range(2, int(entry) + 1):
                    is_prime = True
                    for y in range(2, x):
                        if x % y == 0:
                            is_prime = False
                    if is_prime:
                        # print(x)
                        self.listWidget.addItem(str(x))
                        self.layout().addWidget(self.listWidget)

            else:
                self.label.setText("The box cannot be empty. Enter a number ")


#******** AUTOMORPHIC NUMBER GENERATOR ********#
ERROR_MSG = "ERROR"

class AutoMorphGen(QMainWindow):

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.setWindowTitle("Automorphic Numbers")
        self.setGeometry(200, 200, 400, 400)
        self.general_layout = QVBoxLayout()
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        self._create_display_input()
        self._create_buttons()
        self._connect_signals()


    def _create_display_input(self):
        self.display_input1 = QLineEdit()
        self.display_input1.setGeometry(100, 100, 340, 350)
        self.display_input1.setAlignment(Qt.AlignLeft)
        self.general_layout.addWidget(self.display_input1)

    def _create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()

        buttons = {"1": (0, 0),
                   "2": (0, 1),
                   "3": (0, 2),
                   "4": (0, 3),
                   "5": (0, 4),
                   "6": (1, 0),
                   "7": (1, 1),
                   "8": (1, 2),
                   "9": (1, 3),
                   "0": (1, 4),
                   "Enter": (2, 0),
                   "Clear": (2, 1),
                   }

        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(45, 45)
            buttons_layout.addWidget(self.buttons[btn_text], pos[0], pos[1])

        self.general_layout.addLayout(buttons_layout)

    def set_display_input_text(self, text):
        self.display_input1.setText(text)
        self.display_input1.setFocus()

    def show_display_input_text(self):
        return self.display_input1.text()

    def clear_display_input(self):
        self.set_display_input_text("")

    def _calculate(self):
        result = self._model(n = self.show_display_input_text())
        self.set_display_input_text(result)

    def _build_num(self, n_more):
        if self.show_display_input_text() == ERROR_MSG:
            self.clear_display_input()

        n = self.show_display_input_text() + n_more
        self.set_display_input_text(n)

    def _connect_signals(self):
        for btn_text, btn in self.buttons.items():
            if btn_text not in {"Enter", "Clear"}:
                btn.clicked.connect(partial(self._build_num, btn_text))

        self.buttons["Enter"].clicked.connect(self._calculate)
        self.display_input1.returnPressed.connect(self._calculate)
        self.buttons["Clear"].clicked.connect(self.clear_display_input)

def automorphic_number_calculate(n):

    try:
        square_num = int(n) * int(n)
        num_length = len(str(n))
        last_digits = (str(square_num)[-num_length:])
        if last_digits == n:
            result = f"Automorphic number. {n} squared is {square_num}."
        else:
            result = f"Not an automorphic number. {n} squared is {square_num}."
    except Exception:
        result = ERROR_MSG
    return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget(self)

        self.setCentralWidget(widget)

        layout = QVBoxLayout()

        self.setWindowTitle("Cool Math Tricks")
        self.setGeometry(200, 200, 400, 400)
        self.title = QLabel('Select a math trick to start:', self)
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.window1 = PrimeNumGen()
        self.window2 = AutoMorphGen(automorphic_number_calculate)
        self.window3 = Kaprekar()

        button1 = QPushButton("Prime Number\nGenerator")
        button2 = QPushButton("AutoMorphic Number\nGenerator")
        button3 = QPushButton("Kaprekar's Constant")

        button1.clicked.connect(lambda checked: self.toggle_window(self.window1))
        button2.clicked.connect(lambda checked: self.toggle_window(self.window2))
        button3.clicked.connect(lambda checked: self.toggle_window(self.window3))

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        widget.setLayout(layout)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

def main():
    app = QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
