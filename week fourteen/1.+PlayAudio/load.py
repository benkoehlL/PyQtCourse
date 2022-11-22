import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.load('Media.qml')
#basicscene.qml

sys.exit(app.exec())