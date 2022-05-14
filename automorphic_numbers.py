
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from functools import partial

ERROR_MSG = "ERROR"

class PyQtUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automorphic Numbers")
        self.setFixedSize(350, 350)
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

def main():

    app1 = QApplication(sys.argv)
    view = PyQtUI()
    view.show()
    model = automorphic_number_calculate
    PyQtUICtrl(model=model, view=view)
    sys.exit(app1.exec())

if __name__ == "__main__":
    main()
