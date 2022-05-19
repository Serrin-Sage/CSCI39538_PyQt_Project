from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from functools import partial

from theme import Theme

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.show()
        theme = Theme()

        self.setLayout(QVBoxLayout())

        self.setWindowTitle("Automorphic Numbers")

        self.instructions = theme.instructions('Enter a number to see if\nits square ends with itself.')

        self.entry_box = theme.entry_box()

        self.buttons = {}

        self.display = QLabel()
        self.display.setAlignment(Qt.AlignCenter)

        keypad = QGridLayout()

        buttons = {"1": (2, 0),
                   "2": (2, 1),
                   "3": (2, 2),
                   "4": (1, 0),
                   "5": (1, 1),
                   "6": (1, 2),
                   "7": (0, 0),
                   "8": (0, 1),
                   "9": (0, 2),
                   "0": (3, 1),
                   "Square": (3, 2),
                   "Clear": (3, 0),
                   }

        self.layout().addWidget(self.instructions)
        self.layout().addWidget(self.entry_box)
        self.layout().addWidget(self.display)
        self.layout().addLayout(keypad)

        def build_num(text):
            self.entry_box.setText(self.entry_box.displayText() + text)

        for text, pos in buttons.items():
            self.buttons[text] = theme.button(text)
            if text not in {"Square", "Clear"}:
                self.buttons[text].clicked.connect(partial(build_num, text))
            keypad.addWidget(self.buttons[text], pos[0], pos[1])

        self.entry_box.returnPressed.connect(self.square)
        self.buttons["Square"].clicked.connect(self.square)
        self.buttons["Clear"].clicked.connect(self.clear)

        self.setStyleSheet(f'''
            background: {theme.theme_lighter};
        ''')
        self.display.setStyleSheet(f'''
            background: {theme.theme_dark};
            color: white;
            font: 24px;
        ''')

    def clear(self):
        self.entry_box.clear()
        self.display.clear()

    def square(self):
        if self.entry_box.displayText().isdigit():
            entry = int(self.entry_box.displayText())
            square = entry * entry
            end = int(str(square)[-len(str(entry)):])
            isAutomorphic = end == entry
            self.display.setText('Automorphic!' if isAutomorphic else 'Not automorphic')
            self.entry_box.setText(f'{square}')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
