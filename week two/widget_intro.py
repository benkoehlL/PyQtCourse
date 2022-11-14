from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.logo = QIcon('logo')
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("SaxonQ GUI Development")
        self.setWindowIcon(self.logo)

        '''
        label = QLabel('SaxonQ GUI development', self)
        #label.setText('Hallo')
        label.move(100,100)
        label.setFont(QFont("Sansserif",24))
        label.setStyleSheet("color:blue")
        #label.setText(str(12))
        label.setNum(12)
        '''

        label = QLabel(self)
        ## insert an image
        #pixmap = QPixmap('logo.png')
        #label.setPixmap(pixmap)
        
        ## insert a short movie (without sound)
        movie = QMovie('images/sky.gif')
        movie.setSpeed(100)
        label.setMovie(movie)
        movie.start()

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))
        line_edit.setStyleSheet('color:red')
        line_edit.setGeometry(500,0,200,25)
        line_edit.setPlaceholderText("Here you can write yourself")
        self.create_widget()


    def create_widget(self):
        hbox = QHBoxLayout()
        self.label = QLabel()
        self.label = QLabel('SaxonQ GUI development', self)
        #label.setText('Hallo')
        self.label.move(100,100)
        self.label.setFont(QFont("Sansserif",24))
        self.label.setStyleSheet("color:red")
        btn = self.create_button() 
        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def create_button(self):
        self.button_clck_counter = 0
        btn = QPushButton("Click", self)
        btn.setGeometry(0, 285, 500, 100)
        btn.setText('You can click me (but nothing will happen)')
        btn.setIcon(self.logo)
        btn.setIconSize(QSize(50,100))
        btn.setStyleSheet('color:red')
        btn.clicked.connect(self.clicked_button)
        
        # popup menu
        #menu = QMenu()
        #menu.setFont(QFont("Times", 12, QFont.Weight.ExtraBold))
        #menu.setStyleSheet('color:red')
        #menu.addAction("Okay")
        #menu.addAction("A")
        #menu.addAction('Menu')
        #menu.addAction('poped')
        #menu.addAction('up')

        #btn.setMenu(menu)

        return btn

    def clicked_button(self): 
        if(self.button_clck_counter%2==0):
            self.label.setText('Okay, this text changed')
            self.label.setFont(QFont("Times", 15))
            print(self.button_clck_counter)
            self.label.setStyleSheet('color:green')
            self.button_clck_counter += 1

        elif(self.button_clck_counter%2==1):
            self.label.setText('Okay, this text changed')
            self.label.setFont(QFont("Times", 15))
            self.label.setStyleSheet('color:red')
            print(self.button_clck_counter)
            self.button_clck_counter += 1
        



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())