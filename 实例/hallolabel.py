# Form implementation generated from reading ui file 'hallolabel.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 475)
        Form.setBaseSize(QtCore.QSize(400, 300))
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(210, 240, 111, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test1"))
        self.label_2.setText(_translate("Form", "Halloe Label"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    Ui_Form().setupUi(window)
    window.show()

    sys.exit(app.exec())
