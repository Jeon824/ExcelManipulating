import sys
import os
from PyQt5.QtWidgets import QGroupBox, QCheckBox, QLabel, QDesktopWidget, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import process

class AutomaticExcel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.file_list = []
        self.select_check_box_list = []
        self.result_check_box_list = []

        #self.setupt_main_window()
        #self.set_window_layout()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Automatic-excel')
        self.center()
        self.controlBox = QGroupBox('Control Panel')

        #'파일선택' 버튼
        fileSelecBtn = QPushButton('파일선택', self)
        fileSelecBtn.setCheckable(False)
        fileSelecBtn.clicked.connect(self.openFileNamesDialog)

        #'파일변환' 버튼
        fileTransBtn = QPushButton('파일변환', self)
        fileTransBtn.setCheckable(False)
        fileTransBtn.clicked.connect(self.transformFile)
        
        #'파일삭제' 버튼
        fileDelBtn = QPushButton('파일 삭제', self)
        fileDelBtn.setCheckable(False)
        fileDelBtn.clicked.connect(self.delSelectedFile)

        #Main vertical layout
        self.main_layout = QVBoxLayout(self)
    
        #control button panel
        self.controlLayout = QHBoxLayout()
        self.controlLayout.addWidget(fileSelecBtn)
        self.controlLayout.addWidget(fileTransBtn)
        self.controlLayout.addWidget(fileDelBtn)
        self.controlBox.setLayout(self.controlLayout)

        #Box which indicate selected files
        self.selectLayout = QVBoxLayout()
        self.selectBox = QGroupBox('선택된 파일 목록')
        self.selectBox.setLayout(self.selectLayout)

        #Box which indicate transformed result files 
        self.resultLayout = QVBoxLayout()
        self.resultBox = QGroupBox('변환된 파일 목록')
        self.resultBox.setLayout(self.resultLayout)
    
        self.main_layout.addWidget(self.controlBox,alignment=QtCore.Qt.AlignTop)
        self.main_layout.addWidget(self.selectBox)
        self.main_layout.addWidget(self.resultBox)
        
        centralWidget = QWidget()
        centralWidget.setLayout(self.main_layout)
        self.setCentralWidget(centralWidget)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())   

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            for file in files:
                self.file_list.append(file)
                self.select_check_box_list.append(QCheckBox(file))
                self.selectLayout.addWidget(self.select_check_box_list[len(self.select_check_box_list) - 1])
    
    def delSelectedFile(self, button):
        for cb in self.select_check_box_list:
            if cb.isChecked():
                i = self.file_list.index(cb.text())
                self.selectLayout.removeWidget(cb)
                self.select_check_box_list.pop(i)
                self.file_list.pop(i)
            
        
    def transformFile(self):
        process.compare(self.file_list)
    
    def getCheckFileList(self):
        print('getCheckFileList')
        
        
def main():
    app = QApplication(sys.argv)
    ae = AutomaticExcel()
    ae.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
