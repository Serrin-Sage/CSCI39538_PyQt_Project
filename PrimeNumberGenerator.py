from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.setLayout(qtw.QVBoxLayout())

        # Title
        self.setWindowTitle("Prime Number Generator")

        # setting geometry
        self.setGeometry(100, 100, 340, 350)

        # showing all the widgets
        self.show()

        # font
        font = qtg.QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # Label
        self.label = qtw.QLabel("Enter a number ", self)
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
        self.label.setFont(qtg.QFont('Times', 13))
        self.label.setAlignment(Qt.AlignCenter)

        # setting style sheet
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 2px solid black;"
                                 "background : lightgrey;"
                                 "}")

        self.layout().addWidget(self.label)
        # Entry Box
        entry_box = qtw.QLineEdit()
        entry_box.setObjectName("EntryBox")
        self.layout().addWidget(entry_box)

        # Buttons

        generate_btn = qtw.QPushButton(
            "Generate!", clicked=lambda: primeNumberGenerator())
        self.layout().addWidget(generate_btn)

        # reset button to reset the game, adding action to reset button
        reset_game = qtw.QPushButton(
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
        warning_label = qtw.QLabel("")
        warning_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(warning_label)

        self.listWidget = qtw.QListWidget()

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
                for x in range(2, int(entry)+1):
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


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
