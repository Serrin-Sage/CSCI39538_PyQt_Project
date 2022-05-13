import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class NewWindow(QWidget):
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = NewWindow()
        self.setWindowTitle("Recreational Math Selector")
        self.setGeometry(200, 200, 400, 400)
        l = QVBoxLayout()
        button1 = QPushButton("ENTER")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)

        )
        l.addWidget(button1)

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