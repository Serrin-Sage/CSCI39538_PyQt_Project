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

        if self.count < 4:
            self.instructions.setText('Repeat these steps until\nyou notice a pattern.')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    sys.exit(app.exec_())
