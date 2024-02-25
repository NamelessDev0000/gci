from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
