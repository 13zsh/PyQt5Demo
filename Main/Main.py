from MainForm import Ui_Dialog

import sys
import cv2
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolTip,QMessageBox,QDesktopWidget,QLabel, QHBoxLayout, QVBoxLayout,QPushButton,QWidget, 
                             QGridLayout,QLineEdit,QTextEdit,QAction,QLCDNumber,QSlider)
from PyQt5.QtGui import (QImage, QPixmap, QIcon, QFont)
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from Example import Example
from Color import Color
from Font import Font
from EFile import EFile
from Drag import Drag
from Burning import Burn

class MyWindow(QWidget, Ui_Dialog):
 def __init__(self, *args, **kwargs):

     super().__init__(*args, **kwargs)
     self.setupUi(self)
     self.initUILCD()
     #self.iniUI()

     '''
     类的内部变量定义
     '''
 num = 0

         
 def initUILCD(self):
        
    lcd = QLCDNumber(self)
    sld = QSlider(Qt.Horizontal, self)
    btnLCD = QPushButton('demo')

    self.c = Communicate()
    self.c.closeApp.connect(self.close) 

    btnLCD.clicked.connect(self.btnDemo)
 
    vbox = QVBoxLayout()
    vbox.addWidget(lcd)
    vbox.addWidget(sld)
    vbox.addWidget(btnLCD)
 
    self.setLayout(vbox)
    sld.valueChanged.connect(lcd.display)
        
    self.setGeometry(300, 300, 250, 150)
    self.setWindowTitle('Signal & slot')
    self.show()

 def btnDemo(self):
     
     self.c.closeApp.emit()

 def init(self):
        
    grid = QGridLayout()
    self.setLayout(grid)
 
    names = ['Cls', 'Bck', '', 'Close',
                '7', '8', '9', '/',
            '4', '5', '6', '*',
                '1', '2', '3', '-',
            '0', '.', '=', '+']
        
    positions = [(i,j) for i in range(5) for j in range(4)]
        
    for position, name in zip(positions, names):
            
        if name == '':
            continue
        button = QPushButton(name)
        grid.addWidget(button, *position)
            
    self.move(300, 150)
    self.setWindowTitle('Calculator')
    self.show()

 def test(self):

    textEdit = QTextEdit()
    self.setCentralWidget(textEdit)

    exitAction = QAction(QIcon('python.ico'), 'Exit', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(self.close)

    self.statusBar()

    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)

    toolbar = self.addToolBar('Exit')
    toolbar.addAction(exitAction)
        
    self.setGeometry(300, 300, 350, 250)
    self.setWindowTitle('Main window')    
    self.show()

 def initUIEx(self):
        
    title = QLabel('Title')
    author = QLabel('Author')
    review = QLabel('Review')
 
    titleEdit = QLineEdit()
    authorEdit = QLineEdit()
    reviewEdit = QTextEdit()
 
    grid = QGridLayout()
    #grid.setSpacing(10)
 
    grid.addWidget(title, 0, 0)
    grid.addWidget(titleEdit, 0, 1)
 
    grid.addWidget(author, 1, 0)
    grid.addWidget(authorEdit, 1, 1)
 
    grid.addWidget(review, 2, 0)
    grid.addWidget(reviewEdit, 2, 1, 5, 1)
        
    self.setLayout(grid) 
        
    self.setGeometry(300, 300, 350, 300)
    self.setWindowTitle('Review')    
    self.show()

 def iniUI(self):

     self.btnDefault.clicked.connect(self.OnPushButton1)
     self.btnOne.clicked.connect(self.OnPushBtnOne)
     self.setWindowTitle('主界面')
     self.setWindowIcon(QIcon('python.ico'))
     self.lblDefault = QLabel('lblDefault', self)

     lbl1 = QLabel('Zetcode', self)
     #lbl1.move(15, 10)

     #创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
     QToolTip.setFont(QFont('SansSerif',10))
     self.setToolTip('This is a <b>QWidget</b> widget')
     self.btnDefault.setToolTip('This is a <b> QPushButton</b> widget')
     #显示窗口
     #self.setGeometry(300,300,250,150)
     #self.center()

     #self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

     hbox = QHBoxLayout()
     hbox.addStretch(1)
     hbox.addWidget(self.btnDefault)
     hbox.addWidget(self.btnOne)
     hbox.addWidget(lbl1)
     hbox.addWidget(self.lblDefault)
 
     vbox = QVBoxLayout()
     vbox.addStretch(1)
     vbox.addLayout(hbox)
        
     self.setLayout(vbox)

     self.statusBar().showMessage('Ready')
     self.showMaximized()
     #self.setGeometry(300, 300, 300, 150)
     self.show()

 def OnPushButton1(self):

     self.num += 1
     self.setWindowTitle("pushbutton has been clicked {0} times".format(self.num))
     
     return None
 
 def OnPushBtnOne(self):

     self.num -= 1
     self.setWindowTitle("pushbutton has been clicked {0} times".format(self.num))
     return None

 def closeEvent(self, event):

     reply = QMessageBox.question(self, 'Message','Are you sure to quit?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)

     if reply == QMessageBox.Yes:
         event.accept()
     else:
         event.ignore()

 #控制窗口显示在屏幕中心的方法    
 def center(self):

    #获得窗口
    qr = self.frameGeometry()
    #获得屏幕中心点
    cp = QDesktopWidget().availableGeometry().center()
    #显示到屏幕中心
    qr.moveCenter(cp)
    self.move(qr.topLeft())

class Communicate(QObject):
    
    closeApp = pyqtSignal() 
    

if __name__ == "__main__":
 app = QApplication(sys.argv)
 mainWindow = Burn()
 #mainWindow.show()
 sys.exit(app.exec_())