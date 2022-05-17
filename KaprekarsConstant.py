from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())

        self.setWindowTitle("Kaprekar's Constant")

        self.show()

        self.intro_label = QLabel("\n 6174 is a very special number!\n\nDo you want to see why?\n", self)
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

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
