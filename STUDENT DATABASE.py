#importing packages
from PIL import Image,ImageFont,ImageDraw
import win32ui
from PIL import ImageWin
import win32print
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *    
from PyQt5.QtGui import *
import random,sys
from datetime import datetime
import ast   
import sqlite3
import add_details,get_details,update_details

#Main window
class main():
    def __init__(self,width,height):
        super().__init__()
        self.window = QWidget()
        self.window.setWindowTitle('Student student_Database')
        self.window.setWindowIcon(QIcon("kings.ico"))

        bg = ["BG1.png","BG2.png","BG3.png"]

        background = Image.open(random.choice(bg))
        size = (width,height)
        BG = background.resize(size)
        BG.save("BG.png")

        '''oImage = QImage("BG.png")                  
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))                        
        self.window.setPalette(palette)'''
        
        self.window.setStyleSheet("background-image : url(BG.png)")
        
        def add_d():
            add_details.main()
            self.window.showMaximized() 

        self.add = QPushButton(self.window)
        self.add.setText("ADD STUDENTS DETAILS")
        self.add.clicked.connect(add_d)
        self.add.setFont(QFont("Times New Roman Bold",17))
        self.add.setStyleSheet("border-radius : 12;border : 2px solid black; background: white")
        self.add.setFixedSize(525,70)
        self.add.move(round(width/2)-250,round(height - (45/100)*height))
        
        def get_d():
            get_details.main(self.window)
            self.window.showMaximized()

        self.get = QPushButton(self.window)
        self.get.setText("GET STUDENTS DETAIL")
        self.get.clicked.connect(get_d)
        self.get.setFont(QFont("Times New Roman Bold",17))
        self.get.setStyleSheet("border-radius : 12;border : 2px solid black; background: white")
        self.get.setFixedSize(525,70)
        self.get.move(round(width/2)-250,round(height - (35/100)*height))
        
        def update_d():
            update_details.main()
            self.window.showMaximized()
        self.update = QPushButton(self.window)
        self.update.setText("UPDATE / DELETE DETAILS")
        self.update.clicked.connect(update_d)
        self.update.setFont(QFont("Times New Roman Bold",17))
        self.update.setStyleSheet("border-radius : 12;border : 2px solid black; background: white")
        self.update.setFixedSize(525,70)
        self.update.move(round(width/2)-250,round(height - (25/100)*height))
        
        def Exit():
            self.window.close()
        self.ex = QPushButton(self.window)
        self.ex.setText("EXIT")
        self.ex.clicked.connect(Exit)
        self.ex.setFont(QFont("Times New Roman",17))
        self.ex.setStyleSheet("border-radius : 12;border : 2px solid black; background: white")
        self.ex.setFixedSize(150,70)
        self.ex.move(round(width/2-80),round(height - (15/100)*height))
        
        self.window.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    resolution = app.desktop().screenGeometry()
    w , h = resolution.width() , resolution.height()
    main(w,h)
    app.exec()

