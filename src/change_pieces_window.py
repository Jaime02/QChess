from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QComboBox, QPushButton


class ChangePiecesWindow(QMainWindow):
    def __init__(self, w):
        QMainWindow.__init__(self)

        self.setWindowTitle("Change piece set")
        self.setWindowFlag(Qt.Tool)
        self.setWindowModality(Qt.ApplicationModal)

        self.w = w
        cw = QWidget(self)
        self.setCentralWidget(cw)

        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)

        self.piece_sets = ["Default", "Condal", "Kingdom", "Leipzig", "Magnetic",
                           "Marroquin", "Maya", "Medieval", "Motif"]

        label = QLabel("Choose a piece set:", cw)
        label.setGeometry(10, 10, 180, 25)

        self.combo_box = QComboBox(cw)
        self.combo_box.setGeometry(10, 40, 180, 30)

        for s in self.piece_sets:
            self.combo_box.addItem(s)

        self.accept_button = QPushButton("Accept", cw)
        self.accept_button.setGeometry(10, 80, 90, 30)
        self.accept_button.clicked.connect(self.change)

        self.cancel_button = QPushButton("Cancel", cw)
        self.cancel_button.setGeometry(100, 80, 90, 30)
        self.cancel_button.clicked.connect(self.close)

        self.setFixedSize(200, 120)

    def change(self):
        self.w.game_widget.piece_set = self.combo_box.currentText()
        self.w.game_widget.change_images()
        self.close()

    def show(self):
        QMainWindow.show(self)
        self.activateWindow()
