from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from theme import Theme

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.show()

        theme = Theme()

        # Layout
        self.setLayout(QVBoxLayout())

        # Title
        self.setWindowTitle("Prime Number Generator")

        # font
        font = QFont('Helvetica', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # Label
        self.instructions = theme.instructions('Enter a number')

        self.setFixedWidth(350)
        self.setFixedHeight(350)

        self.layout().addWidget(self.instructions)

        self.setStyleSheet(f'''
            background: {theme.theme_lighter};
        ''')

        # Entry Box
        self.entry_box  = theme.entry_box()
        self.button     = theme.button('')

        self.entry_row = QHBoxLayout()
        self.entry_row.addWidget(self.entry_box)
        self.entry_row.addWidget(self.button)

        self.layout().addLayout(self.entry_row)

        self.entry_box.setFixedWidth(130)
        self.button   .setFixedWidth(170)

        self.listWidget = QListWidget()
        self.listWidget.setStyleSheet(f'''
            background: {theme.theme};
            color: {theme.accent};
            font: 24px;
        ''')
        self.layout().addWidget(self.listWidget)

        self.entry_box.returnPressed.connect(self.enter)
        self.button.clicked.connect(self.enter)

        self.reset()

    def enter(self):
        entry = self.entry_box.displayText()

        self.button.setText('RESET')

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.reset)

        if entry != "" and entry.isdigit():
            for x in range(2, int(entry) + 1):
                is_prime = True
                for y in range(2, x):
                    if x % y == 0:
                        is_prime = False
                if is_prime:
                    self.listWidget.addItem(str(x))

    def reset(self):
        self.instructions.setText('Enter a number to find\nall primes below it.')
        self.listWidget.clear()
        self.entry_box.clear()

        self.button.setText('ENTER')
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.enter)


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
