from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import sys

from theme import Theme
#********** KAPREKAR'S CONSTANT ********#
class Kaprekar(QWidget):
    def __init__(self):
        super().__init__()

        theme = Theme()

        self.count = 0

        self.setLayout(QVBoxLayout())

        self.setWindowTitle("Kaprekar's Constant")

        self.step_label   = QLabel('STEP ONE')
        self.instructions = QLabel('Enter a 4-digit number\nwith 2 unique digits.')
        self.entry_box    = QLineEdit()
        self.number_box   = QLabel()
        self.button       = QPushButton('Enter')

        self.calculation    = QVBoxLayout()
        self.entry_row      = QHBoxLayout()
        self.decreasing_row = QHBoxLayout()
        self.increasing_row = QHBoxLayout()

        self.decreasing_box   = QLabel()
        self.increasing_box   = QLabel()
        self.decreasing_label = QLabel('decreasing')
        self.increasing_label = QLabel('increasing')

        self.number_box      .hide()
        self.decreasing_label.hide()
        self.increasing_label.hide()

        self.layout().addWidget(self.step_label)
        self.layout().addWidget(self.instructions)
        self.layout().addLayout(self.calculation)
        self.layout().addLayout(self.entry_row)

        self.entry_row.addWidget(self.entry_box)
        self.entry_row.addWidget(self.number_box)
        self.entry_row.addWidget(self.button)

        self.decreasing_row.addWidget(self.decreasing_box)
        self.increasing_row.addWidget(self.increasing_box)
        self.decreasing_row.addWidget(self.decreasing_label)
        self.increasing_row.addWidget(self.increasing_label)

        self.calculation.addLayout(self.decreasing_row)
        self.calculation.addLayout(self.increasing_row)

        self               .setFixedHeight(350)
        self.instructions  .setFixedHeight(80)

        self               .setFixedWidth(350)
        self.entry_box     .setFixedWidth(130)
        self.number_box    .setFixedWidth(130)
        self.button        .setFixedWidth(170)
        self.decreasing_box.setFixedWidth(118)
        self.increasing_box.setFixedWidth(118)

        self.step_label    .setAlignment(Qt.AlignLeft)
        self.instructions  .setAlignment(Qt.AlignCenter)
        self.entry_box     .setAlignment(Qt.AlignRight)
        self.number_box    .setAlignment(Qt.AlignRight)
        self.decreasing_box.setAlignment(Qt.AlignRight)
        self.increasing_box.setAlignment(Qt.AlignRight)

        self.button.clicked.connect(self.enter)

        self.setStyleSheet(f'''
            background: {theme.theme};
            font: 24px;
        ''')
        self.step_label.setStyleSheet(f'''
            background: {theme.theme};
            font: bold 36px;
            color: white;
        '''
        )
        self.instructions.setStyleSheet(f'''
            {theme.border}
            background: {theme.accent};
            color: {theme.theme_dark};
        ''')
        self.decreasing_box.setStyleSheet(f'''
            color: white;
            font: 36px;
        ''')
        self.increasing_box.setStyleSheet(f'''
            color: white;
            font: 36px;
        ''')
        self.decreasing_label.setStyleSheet(f'''
            color: {theme.accent};
            font: 20px;
        ''')
        self.increasing_label.setStyleSheet(f'''
            color: {theme.accent};
            font: 20px;
        ''')
        self.entry_box.setStyleSheet(f'''
            {theme.border}
            background: {theme.accent};
            color: {theme.theme};
            font: 36px;
        ''')
        self.number_box.setStyleSheet(f'''
            {theme.border}
            background: {theme.accent};
            color: {theme.theme};
            font: 36px;
        ''')
        self.button.setStyleSheet(
            'QPushButton {' f'''
                {theme.border}
                padding: 5px 10px;
                background: {theme.theme};
                color: white;
                text-transform: uppercase;
            ''''}'
            'QPushButton::hover {' f'''
                {theme.border_inverse}
                background: {theme.theme};
            ''''}'
            'QPushButton::pressed {' f'''
                {theme.border_inverse}
                background: {theme.theme_dark};
            ''''}'
        )


    def enter(self):
        entry = self.entry_box.displayText()

        def twoUnique():
            count = {}
            for digit in entry:
              if digit in count:
                count[digit] += 1
                if count[digit] > 2:
                  return False
              else:
                count[digit] = 1
            return True

        if len(entry) == 4 and entry.isdigit() and twoUnique():
            self.number = int(self.entry_box.displayText())
            self.entry_box.hide()
            self.number_box.show()
            self.cycle()

    def cycle(self):
        instructions = 'Arrange digits in\ndecreasing order.'

        self.notice = 'Have you noticed yet?'

        if self.count > 3:
            self.notice = "Kaprekar's Constant:\n6174"

        self.step_label  .setText('STEP TWO')
        self.instructions.setText(instructions if self.count < 2 else self.notice)
        self.number_box  .setText(f'{self.number}')
        self.button      .setText('Sort')

        self.decreasing_label.hide()
        self.increasing_label.hide()

        self.decreasing_box.clear()
        self.increasing_box.clear()

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.sortDecreasing)

    def sortDecreasing(self):
        instructions = 'Arrange digits in\nincreasing order.'

        self.decreasing = int(''.join([str(digit) for digit in sorted([int(digit) for digit in str(self.number)], reverse=True)]))

        self.step_label    .setText('STEP THREE')
        self.instructions  .setText(instructions if self.count < 2 else self.notice)
        self.decreasing_box.setText(f'{self.decreasing}')

        self.decreasing_label.show()

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.sortIncreasing)

    def sortIncreasing(self):
        instructions = 'Subtract this number\nfrom the previous one.'

        self.increasing = int(str(self.decreasing)[::-1])

        self.number_box.clear()

        self.step_label    .setText('STEP FOUR')
        self.instructions  .setText(instructions if self.count < 2 else self.notice)
        self.increasing_box.setText(f'- {self.increasing}')
        self.button        .setText('Subtract')

        self.increasing_label.show()

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.subtract)

    def subtract(self):
        self.number = self.decreasing - self.increasing

        self.step_label.setText('STEP ONE (again)')
        self.number_box.setText(f'{self.number}')
        self.button    .setText('Repeat')

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.cycle)

        if self.number == 6174:
            self.count += 1
            self.number_box.setStyleSheet(f'''
                {theme.border}
                background: white;
                color: {theme.theme};
                font: 36px;
            ''')

        if self.count < 4:
            self.instructions.setText('Repeat these steps until\nyou notice a pattern.')

#********** PRIME NUMBER GENERATOR ********#
class PrimeNumGen(QWidget):
    def __init__(self):
        super().__init__()

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

#******** AUTOMORPHIC NUMBER GENERATOR ********#
class AutoMorphGen(QWidget):

    def __init__(self):
        super().__init__()
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        theme = Theme()

        widget = QWidget(self)

        self.setCentralWidget(widget)

        layout = QVBoxLayout()

        self.setWindowTitle("Cool Math Tricks")

        self.window1 = PrimeNumGen()
        self.window2 = AutoMorphGen()
        self.window3 = Kaprekar()

        self.instructions = theme.instructions('Select a math trick to start!')

        self.setFixedWidth(350)
        self.setFixedHeight(350)

        layout.addWidget(self.instructions)

        button1 = theme.button("Prime Number Generator")
        button2 = theme.button("AutoMorphic Numbers")
        button3 = theme.button("Kaprekar's Constant")

        button1.clicked.connect(lambda checked: self.toggle_window(self.window1))
        button2.clicked.connect(lambda checked: self.toggle_window(self.window2))
        button3.clicked.connect(lambda checked: self.toggle_window(self.window3))

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        widget.setLayout(layout)

        self.setStyleSheet(f'''
            background: {theme.theme_lighter};
            font: 24px;
        ''')

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
