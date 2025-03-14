import sys

from PyQt5.QtWidgets import (QDesktopWidget, QApplication, QMainWindow, QWidget, QPushButton,
                             QScrollArea, QHBoxLayout, QGroupBox, QVBoxLayout, QCheckBox, QAction, qApp)
from PyQt5.QtGui import QIcon
class AutomaticExcel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    
    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('ExitApplication')
        exitAction.triggered.connect(qApp.quit)

        mainLayout = QVBoxLayout()
        mainLayout.addStretch(1)

        cw = QWidget()
        cw.setLayout(mainLayout)
        self.setCentralWidget(cw)

        test = QVBoxLayout(self)

        selGBox = QGroupBox()
        

        resGBox = QGroupBox()

        

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Automatic-excel')
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.show()
    
    def fileSelecClicked(self):
        print("a")
    
    def fileTransClicked(self):
        print("a")
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AutomaticExcel()
    sys.exit(app.exec_())