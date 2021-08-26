from PIL import Image,ImageFont,ImageDraw
import win32ui
from PIL import ImageWin
import win32print
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *    
from PyQt5.QtGui import *
import sys
from datetime import datetime
import ast   
import sqlite3

def main(win):    
    def get_details():
                window = QWidget()
                window.setWindowTitle('Get Student Details')
                window.setGeometry(500,500,500,100)
                window.setWindowIcon(QIcon("kings.ico"))
                

                layout = QFormLayout()
                regno = QLineEdit()
                my_regex1 = QRegExp("[0-9 ,'-;:]{12}")
                my_validator = QRegExpValidator(my_regex1, regno)
                regno.setValidator(my_validator)
                regno.setFont(QFont("Times New Roman",12))
                layout.addRow("Enter Register Number",regno)
                
                class get(QWidget):
                    def __init__(self):
                        super().__init__()
                        if regno.text() == "":
                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Warning) 
                            msgBox.setText("Enter Register Number")
                            msgBox.setWindowTitle("Warning")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            returnValue = msgBox.exec()
                            if returnValue == QMessageBox.Ok:
                                msgBox.close()
                                        

                        else:    
                            try: 
                                self.title = "Student Details"
                                self.top = 100
                                self.left = 100
                                self.width = 1000
                                self.height = 1000
                                self.setWindowIcon(QIcon("kings.ico"))
                                self.setWindowTitle(self.title)
                                self.setGeometry(self.left, self.top, self.width, self.height)
                                            
                                formLayout =QFormLayout()
                                groupBox = QGroupBox()
                                groupBox.setGeometry(0,0,1200,1200)
                                formLayout.setVerticalSpacing(15)

                                """DBname = "ampkmxpj"
                                DBuser = "ampkmxpj"
                                DBPass = "4iQSOieaHWL45EXhf0UfWCNHqmAv2yqh"
                                DBhost = "batyr.db.elephantsql.com"
                                DBport = "5432" """
                                db = sqlite3.connect('student_Database.db')

                                cur = db.cursor()
                                get_regno = regno.text()
                                cur.execute("SELECT * FROM student_Database WHERE Regno = ?",(get_regno,))
                                a,b,c,d,e,f,g,h = cur.fetchone()
                                db.commit()
                                            
                                registerno = QLineEdit()
                                registerno.setFont(QFont("Times New Roman",16))
                                registerno.setText(str(a))
                                registerno.setReadOnly(True)

                                studentname = QLineEdit()
                                studentname.setFont(QFont("Times New Roman",16))
                                studentname.setText(str(b))
                                studentname.setReadOnly(True)

                                dateofbirth = QDateEdit()
                                dateofbirth.setFont(QFont("Times New Roman",16))
                                dateofbirth.setDisplayFormat("d-MMM-yyyy")
                                dateob = datetime.strptime(str(c), '%Y-%m-%d')
                                dateofbirth.setDate(dateob)
                                str_date = str(dateofbirth.text())
                                dateofbirth.setReadOnly(True)

                                Batch = QLineEdit()
                                Batch.setFont(QFont("Times New Roman",16))
                                Batch.setText(str(d))
                                Batch.setReadOnly(True)

                                Department = QLineEdit()
                                Department.setFont(QFont("Times New Roman",16))
                                Department.setText(str(e))
                                Department.setReadOnly(True)

                                feedue = QLineEdit()
                                feedue.setFont(QFont("Times New Roman",16))
                                feedue.setText(str(f))
                                feedue.setReadOnly(True)

                                certificate_s = QTextEdit()
                                certificate_s.setFont(QFont("Times New Roman",14))
                                l1 = ast.literal_eval(g)
                                cert_s = ""
                                for li1 in l1:
                                    if l1.index(li1) >= 1:
                                        cert_s = cert_s + "," + li1
                                    elif li1 == l1[-1]:
                                        cert_s = cert_s + li1 + "."
                                    else:
                                        cert_s = cert_s + li1
                                certificate_s.setText(cert_s)
                                certificate_s.setWordWrapMode(True)
                                certificate_s.setReadOnly(True)

                                certificate_i = QTextEdit()
                                certificate_i.setFont(QFont("Times New Roman",14))
                                l2 = ast.literal_eval(h)
                                cert_i = ""
                                for li2 in l2:
                                    if l2.index(li2) >= 1:
                                        cert_i = cert_i + "," + li2
                                    elif li2 == l2[-1]:
                                        cert_i = cert_i + li2 + "."
                                    else:
                                        cert_i = cert_i + li2
                                certificate_i.setText(cert_i)
                                certificate_i.setWordWrapMode(True)
                                certificate_i.setReadOnly(True)

                                i_on = QDateEdit()
                                i_on.setFont(QFont("Times New Roman",16))
                                i_on.setDisplayFormat("d-MMM-yyyy")
                                i_on.setDate(QDate.currentDate())

                                remarks = QLineEdit()
                                remarks.setFont(QFont("Times New Roman",16))

                                g1 = QLabel("Register Number")
                                g2 = QLabel("Student Name")
                                g3 = QLabel("Date of Birth")
                                g4 = QLabel("Batch")
                                g5 = QLabel("Department")
                                g6 = QLabel("Certificates Submitted")
                                g7 = QLabel("Certificates Issued")
                                g8 = QLabel("certificates Issued on")
                                g9 = QLabel("Remarks")
                                g1.setFont(QFont("Times New Roman",16))
                                g2.setFont(QFont("Times New Roman",16))
                                g3.setFont(QFont("Times New Roman",16))
                                g4.setFont(QFont("Times New Roman",16))
                                g5.setFont(QFont("Times New Roman",16))
                                g6.setFont(QFont("Times New Roman",16))
                                g7.setFont(QFont("Times New Roman",16))
                                g8.setFont(QFont("Times New Roman",16))
                                g9.setFont(QFont("Times New Roman",16))

                                formLayout.addRow(g1,registerno)
                                formLayout.addRow(g2,studentname)
                                formLayout.addRow(g3,dateofbirth)
                                formLayout.addRow(g4,Batch)
                                formLayout.addRow(g5,Department)
                                formLayout.addRow(g6,certificate_s)
                                formLayout.addRow(g7,certificate_i)
                                formLayout.addRow(g8,i_on)
                                formLayout.addRow(g9,remarks)

                                def print_img():
                                    self.show()
                                    my_image = Image.open("print.png")

                                    title_font = ImageFont.truetype(font='times-new-roman.ttf', size = 100)

                                    image_editable = ImageDraw.Draw(my_image)

                                    image_editable.text((1550,1040),str(a),(0,0,0),font=title_font)
                                    image_editable.text((1550,1300),str(b),(0,0,0),font=title_font)
                                    image_editable.text((1550,1550),str_date,(0,0,0),font=title_font)
                                    image_editable.text((1550,1800),str(d),(0,0,0),font=title_font)
                                    image_editable.text((1550,2050),str(e),(0,0,0),font=title_font)
                                    image_editable.text((1550,2300),str(f),(0,0,0),font=title_font)
                                    lr = 1550
                                    ttb = 2550
                                    op1 = ast.literal_eval(g)
                                    op2 = ast.literal_eval(h)
                                    for y in op1:
                                        image_editable.text((lr,ttb),y,(0,0,0),font=title_font)
                                                                    
                                        if y == op1[-1]:
                                            image_editable.text((lr+10+len(y)*45,ttb),".",(0,0,0),font=title_font)
                                        else:
                                            image_editable.text((lr+len(y)*45,ttb),",",(0,0,0),font=title_font)
                                        lr = lr + len(y)*50
                                        if op1.index(y)%2 == 0:
                                            lr = 1550
                                            ttb = ttb + 110
                                    lr2=1550
                                    ttb2=3600
                                    for z in op2:
                                        image_editable.text((lr2,ttb2),z,(0,0,0),font=title_font)
                                                                    
                                        if z == op2[-1]:
                                            image_editable.text((lr2+10+len(z)*45,ttb2),".",(0,0,0),font=title_font)
                                        else:
                                            image_editable.text((lr2+len(z)*45,ttb2),",",(0,0,0),font=title_font)
                                        lr2 = lr2 + len(z)*50
                                        if op2.index(z)%2 == 0:
                                            lr2 = 1550
                                            ttb2 = ttb2 + 110
                                        image_editable.text((1550,4580),str(i_on.date().toPyDate()),(0,0,0),font=title_font)
                                        image_editable.text((800,4850),remarks.text(),(0,0,0),font=title_font)
                                        my_image.save("report.png")
                                        my_image.show()
                                        win.showMaximized()

            
                                        msgBox = QMessageBox()
                                        msgBox.setIcon(QMessageBox.Question)
                                        msgBox.setText("Are you sure you want to print?")
                                        msgBox.setWindowTitle("Question")
                                        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                                        returnValue = msgBox.exec()
                                        if returnValue == QMessageBox.Yes:
                                            HORZRES = 8
                                            VERTRES = 10

                                            LOGPIXELSX = 88
                                            LOGPIXELSY = 90

                                            PHYSICALWIDTH = 110
                                            PHYSICALHEIGHT = 111

                                            PHYSICALOFFSETX = 112
                                            PHYSICALOFFSETY = 113

                                            printer_name = win32print.GetDefaultPrinter ()
                                            file_name = "report.png"


                                            hDC = win32ui.CreateDC ()
                                            hDC.CreatePrinterDC (printer_name)
                                            printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
                                            printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
                                            printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)


                                            bmp = Image.open (file_name)
                                            if bmp.size[0] > bmp.size[1]:
                                                bmp = bmp.rotate (90)

                                            ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
                                            scale = min (ratios)


                                            hDC.StartDoc (file_name)
                                            hDC.StartPage ()

                                            dib = ImageWin.Dib (bmp)
                                            scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
                                            x1 = int ((printer_size[0] - scaled_width) / 2)
                                            y1 = int ((printer_size[1] - scaled_height) / 2)
                                            x2 = x1 + scaled_width
                                            y2 = y1 + scaled_height
                                            dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

                                            hDC.EndPage ()
                                            hDC.EndDoc ()
                                            hDC.DeleteDC ()
                                        if returnValue == QMessageBox.No:
                                            msgBox.close()
                                            
                                                        
                                pnt = QPushButton("Print")
                                pnt.setFont(QFont("Times New Roman",16))
                                pnt.clicked.connect(print_img)

                                def cancel():
                                    self.close()
                                cncl = QPushButton("Close")
                                cncl.setFont(QFont("Times New Roman",16))
                                cncl.clicked.connect(cancel)
                                formLayout.addRow(pnt,cncl)

                                groupBox.setLayout(formLayout)
                                scroll = QScrollArea()
                                scroll.setWidget(groupBox)
                                scroll.setWidgetResizable(True)
                                scroll.setFixedHeight(1000)
                                layout = QVBoxLayout(self)
                                layout.addWidget(scroll)
                                self.show()
                            except TypeError:
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Warning) 
                                msgBox.setText("Enter correct Register Number")
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()
                            
                        
                a = QPushButton("GET")
                a.clicked.connect(lambda: get())

                def cancel():
                    window.close()
                c = QPushButton("Cancel")
                c.clicked.connect(cancel)
                layout.addRow(a,c)
                
                window.setLayout(layout)
                window.show()
    get_details()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
    app.exec()