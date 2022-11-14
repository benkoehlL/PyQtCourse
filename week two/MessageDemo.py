# Form implementation generated from reading ui file 'MessageDemo.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_warn = QtWidgets.QPushButton(Dialog)

        #connect signal
        self.pushButton_warn.clicked.connect(self.warn_msg)
        self.pushButton_warn.setObjectName("pushButton_warn")
        self.horizontalLayout.addWidget(self.pushButton_warn)
        self.pushButton_info = QtWidgets.QPushButton(Dialog)

        # connect signal
        self.pushButton_info.clicked.connect(self.info_msg)
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout.addWidget(self.pushButton_info)
        self.pushButton_about = QtWidgets.QPushButton(Dialog)

        # connect signal
        self.pushButton_about.clicked.connect(self.about_msg)
        self.pushButton_about.setObjectName("pushButton_about")
        self.horizontalLayout.addWidget(self.pushButton_about)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def warn_msg(self):
        QMessageBox.warning(self, "Warning", "This is a warning message")

    def info_msg(self):
        QMessageBox.information(self, "Information", "This is information message")

    def about_msg(self):
        QMessageBox.about(self, "About", "This is about message")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_warn.setText(_translate("Dialog", "Warning"))
        self.pushButton_info.setText(_translate("Dialog", "Information"))
        self.pushButton_about.setText(_translate("Dialog", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
