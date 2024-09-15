from cProfile import label

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)  # 创建应用
# print(sys.argv)
# print(app.arguments())

window = QWidget()
window.setWindowTitle("ExeTest")
window.resize(500, 450)
window.move(0, 0)
window.show()

label1 = QLabel()
label1.setText("Hallo World")
label1.resize(150, 50)
label1.setStyleSheet("background-color:yellow;padding:10px")
label1.move(100, 100)

label1.setParent(window)
label1.show()

sys.exit(app.exec())  # 开始执行，并进行消息等待
