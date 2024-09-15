from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./hallolabel.ui")
    ui.show()

    sys.exit(app.exec())
