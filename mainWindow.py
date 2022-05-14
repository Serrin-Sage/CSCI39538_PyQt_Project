import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from functools import partial
import automorphic_numbers
import sys

#********** PRIME NUMBER GENERATOR ********#
class PrimeNumGen(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # Title
        self.setWindowTitle("Prime Number Generator")

        # setting geometry
        self.setGeometry(200, 200, 400, 400)

        # font
        font = QFont('Times', 14)
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
        self.label.setFont(QFont('Times', 13))
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
        reset_game = QPushButton("Reset", clicked=lambda: reset_action())
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
            # making label green
            self.label.setStyleSheet("QLabel"
                                     "{"
                                     "border : 2px solid black;"
                                     "background : lightgrey;"
                                     "}")

            # setting text to the info label
            self.label.setText("Reset...Enter a number")

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

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automorphic Numbers")
        self.setGeometry(100, 100, 340, 350)
        self.general_layout = QVBoxLayout()
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        self._create_display_input()
        self._create_buttons()

    def _create_display_input(self):
        self.display_input1 = QLineEdit()
        self.display_input1.setFixedHeight(35)
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

class PyQtUICtrl:

    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connect_signals()

    def _calculate(self):
        result = self._model(n = self._view.show_display_input_text())
        self._view.set_display_input_text(result)

    def _build_num(self, n_more):
        if self._view.show_display_input_text() == ERROR_MSG:
            self._view.clear_display_input()

        n = self._view.show_display_input_text() + n_more
        self._view.set_display_input_text(n)

    def _connect_signals(self):
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {"Enter", "Clear"}:
                btn.clicked.connect(partial(self._build_num, btn_text))

        self._view.buttons["Enter"].clicked.connect(self._calculate)
        self._view.display_input1.returnPressed.connect(self._calculate)
        self._view.buttons["Clear"].clicked.connect(self._view.clear_display_input)

def automorphic_number_calculate(n):

    try:
        square_num = int(n) * int(n)
        num_length = len(str(n))
        last_digits = (str(square_num)[-num_length:])
        if last_digits == n:
            result = f"Automorphic number. {n} squared is {square_num}."
        else:
            result = f"Not a automorphic number. {n} squared is {square_num}."
    except Exception:
        result = ERROR_MSG
    return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = PrimeNumGen()
        self.window2 = AutoMorphGen()
        self.setWindowTitle("Recreational Math Selector")
        self.setGeometry(200, 200, 400, 400)
        l = QVBoxLayout()
        button1 = QPushButton("Prime Gen")
        button2 = QPushButton("AutoMorph Gen")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome to Recreational Math Selector")
        self.label.move(100, 100)
        self.update()


    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def update(self):
        self.label.adjustSize()


app = QApplication(sys.argv)
Main = MainWindow()
Main.show()

sys.exit(app.exec())