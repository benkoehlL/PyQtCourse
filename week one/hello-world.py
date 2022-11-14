from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Hello Window")
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedWidth(700)
        self.setFixedHeight(400)
        self.setStyleSheet('background-color:black')
        self.setWindowOpacity(0.05)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())



'''
## creat a QMainWindow
app = QApplication(sys.argv)
window = QMainWindow()
window.statusBar().showMessage("Welcome to the main window")
window.menuBar().addMenu("File")
window.menuBar().addMenu("Option")
window.menuBar().addMenu("Cat")
window.setWindowTitle("Hello Window")
window.setGeometry(2000,2000,4000,4000)

window.show()
sys.exit(app.exec())
'''

'''
## creat a QWidget
app = QApplication(sys.argv)
window = QWidget()
window.show()
sys.exit(app.exec())
'''

'''
app = QApplication(sys.argv)
window = QDialog()
window.show()
sys.exit(app.exec())
'''