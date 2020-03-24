import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication,QHBoxLayout)
import random

class Example(QWidget):
    """description of class"""

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.btn = QPushButton('Dialog', self)
        self.btn.clicked.connect(self.showDialog)

        self.btn1 = QPushButton('Dialog1', self)
        self.btn1.clicked.connect(self.printMessage)
        
        self.le = QLineEdit(self)
        #self.le.move(130, 22)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn)
        hbox.addWidget(self.le)
        hbox.addWidget(self.btn1)
        
        #self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.setLayout(hbox)
        self.show()
        
        
    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))

    def get_val_at_pos_1(x):
        
        return x[1]

    heros = [
        ('Superman', 99),
        ('Batman', 100),
        ('Joker', 85)
    ]

    def printMessage(self):
        
        sorted_pairs0 = sorted(self.heros, key=self.get_val_at_pos_1)
        print(sorted_pairs0)

