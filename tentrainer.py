from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5 import Qt
import sys

# La clase Window hereda de QDialog
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Layout Management"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100

        self.InitWindow()
        


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.puntajeLayout()
        self.codeLayout()
        self.onGameLayout()

        self.show()

    def puntajeLayout(self):
        self.puntajeBox = QGroupBox("Puntajes")
        hboxlayout = QHBoxLayout()
        labelWpm = QLabel(self)
        labelWpm.setText("<small>I'm small</small><br>"
            "I'm average :(<br>"
            "<big>I'm big!</big><br>"
            "<font size=15>I'm 15!</font>")
        labelWpm.setAlignment(QtCore.Qt.AlignCenter)

        labelAcc = QLabel(self)
        labelAcc.setText("99%")
        labelAcc.setAlignment(QtCore.Qt.AlignCenter)

        hboxlayout.addWidget(labelWpm)
        hboxlayout.addWidget(labelAcc)

        self.puntajeBox.setLayout(hboxlayout)

    def codeLayout(self):
        self.codeBox = QGroupBox("Código")
        hboxlayout = QHBoxLayout()
        labelCode = QLabel(self)
        labelCode.setText("This should be some code")
        labelCode.setAlignment(QtCore.Qt.AlignLeft)

        hboxlayout.addWidget(labelCode)
        self.codeBox.setLayout(hboxlayout)

    def onGameLayout (self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.puntajeBox)
        vbox.addWidget(self.codeBox)
        self.setLayout(vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = Window()
    sys.exit(App.exec())