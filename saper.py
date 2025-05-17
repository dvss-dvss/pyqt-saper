import random
import time

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Сапер")
        self.setGeometry(300, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()


