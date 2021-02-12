from src.main_window import GameWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("images/logo.png"))
    window = GameWindow(app)
    app.exec()
