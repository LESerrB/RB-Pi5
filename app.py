import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import *

from GUI.pesaje_UI import Ui_MainWindow # Código generado por QtDesigner

class MainWindow(QMainWindow, Ui_MainWindow):
    num = 18

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lcdNumber.display(self.num)

        self.btnTarar.clicked.connect(self.tarar)
        self.btnPesar.clicked.connect(self.pesar)

    def tarar(self):
        self.num = 0
        self.lcdNumber.display(self.num)

    def pesar(self):
        self.num += 1
        self.lcdNumber.display(self.num)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())