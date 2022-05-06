import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Recreational Math Selector")
        self.setGeometry(200, 200, 400, 400)
        self.label = QLabel("NEW WINDOW TEST")
        layout.addWidget(self.label)
        self.setLayout(layout)

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