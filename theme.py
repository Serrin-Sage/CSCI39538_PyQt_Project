from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Theme():
    theme         = '#FF7FB0'
    theme_light   = '#FFA0C0'
    theme_lighter = '#FFB0D0'
    theme_dark    = '#F270A0'
    accent        = '#DDFFFF'

    border = f'''
        border-top: 4px solid {theme_light};
        border-left: 4px solid {theme_light};
        border-right: 4px solid {theme_dark};
        border-bottom: 4px solid {theme_dark};
    '''

    border_inverse = f'''
        border-top: 4px solid {theme_dark};
        border-left: 4px solid {theme_dark};
        border-right: 4px solid {theme_light};
        border-bottom: 4px solid {theme_light};
    '''

    def instructions(self, text):
        instructions = QLabel(text)
        instructions.setAlignment(Qt.AlignCenter)
        instructions.setFixedHeight(80)
        instructions.setStyleSheet(f'''
            {self.border}
            background: white;
            color: {self.theme_dark};
            font: 24px;
        ''')
        return instructions

    def entry_box(self):
        entry_box = QLineEdit()
        entry_box.setAlignment(Qt.AlignRight)
        entry_box.setStyleSheet(f'''
            {self.border}
            background: {self.accent};
            color: {self.theme};
            font: 36px;
        ''')
        return entry_box

    def button(self, text):
        button = QPushButton(text)
        button.setStyleSheet(
            'QPushButton {' f'''
                {self.border}
                padding: 5px 10px;
                background: {self.theme};
                color: white;
                font: 24px;
            ''''}'
            'QPushButton::hover {' f'''
                {self.border_inverse}
                background: {self.theme};
            ''''}'
            'QPushButton::pressed {' f'''
                {self.border_inverse}
                background: {self.theme_dark};
            ''''}'
        )
        return button
