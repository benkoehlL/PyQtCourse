# Form implementation generated from reading ui file 'InsertData.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditUsername = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.horizontalLayout.addWidget(self.lineEditUsername)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditPassword = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_2.addWidget(self.lineEditPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #connect to singal
        self.pushButton.clicked.connect(self.insert_data)

        self.verticalLayout.addWidget(self.pushButton)
        self.labelResult = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def insert_data(self):
        try:
            db=mc.connect(
                host="pyqtexample.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
                user="admin",
                password="password",
                database="pyqt",
                port=3306
            )

            cur = db.cursor()
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()

            query = "INSERT INTO User (username, password) VALUES (%s, %s)"
            value = (username, password)

            cur.execute(query, value)

            db.commit()

            self.labelResult.setText("Data inserted")

        except mc.Error as e:
            self.labelResult.setText("Unable to insert data {} ".format(e))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Insert Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())