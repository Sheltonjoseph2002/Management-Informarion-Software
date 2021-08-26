import sys
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *    
from PyQt5.QtGui import *
import sqlite3

def main():
    class add_details(QWidget):
        def __init__(self):
                    super().__init__()
                    self.title = "Enter Students detail"
                    self.top = 0
                    self.left = 0
                    self.width = 1000
                    self.height = 1000
                    self.setWindowIcon(QIcon("kings.ico"))
                    self.setWindowTitle(self.title)
                    self.setGeometry(self.left, self.top, self.width, self.height)
                    oImage = QImage("BG4.png")                  
                    palette = QPalette()
                    palette.setBrush(QPalette.Window, QBrush(oImage))                        
                    self.setPalette(palette)
                    formLayout =QFormLayout()
                    formLayout.setVerticalSpacing(20)
                    groupBox = QGroupBox()
                    groupBox.setGeometry(0,0,1000,1000)

                    reg_no = QLineEdit()
                    reg_no.setMaximumWidth(500)
                    reg_no.setFont(QFont("Times New Roman",16))
                    my_regex1 = QRegExp("[0-9 ,'-;:]{12}")
                    my_validator = QRegExpValidator(my_regex1, reg_no)
                    reg_no.setValidator(my_validator)
                    r = QLabel("Register Number")
                    r.setStyleSheet("color : white")
                    r.setFont(QFont("Times New Roman",16))
                    formLayout.addRow(r,reg_no)
                    
                    
                    name = QLineEdit()
                    name.setMaximumWidth(500)
                    name.setFont(QFont("Times New Roman",16))
                    my_regex = QRegExp("[a-zA-Z. ,';:]{50}")
                    my_validator = QRegExpValidator(my_regex, name)
                    name.setValidator(my_validator)
                    n = QLabel("Student Name")
                    n.setStyleSheet("color : white")
                    n.setFont(QFont("Times New Roman",16))
                    formLayout.addRow(n,name)

                    dob = QDateEdit()
                    dob.setDisplayFormat("d-MMM-yyyy")
                    dob.setMaximumWidth(500)
                    dob.setFont(QFont("Times New Roman",16))
                    db = QLabel("Date Of Birth")
                    db.setStyleSheet("color : white")
                    db.setFont(QFont("Times New Roman",16))
                    formLayout.addRow(db,dob)

                    b = QLineEdit()
                    b.setMaximumWidth(500)
                    b.setFont(QFont("Times New Roman",16))
                    my_regex1 = QRegExp("[0-9 ,'-;:]{9}")
                    my_validator = QRegExpValidator(my_regex1, b)
                    b.setValidator(my_validator)
                    b.setPlaceholderText("Example: 2019-2023")
                    batch = QLabel("Batch")
                    batch.setStyleSheet("color : white")
                    batch.setFont(QFont("Times New Roman",16))
                    formLayout.addRow(batch,b)

                    rb2 = QVBoxLayout()
                    self.d1 = QRadioButton("B.E(Computer Science and Engineering)")
                    self.d2 = QRadioButton("B.E(Mechanical Engineering)")
                    self.d3 = QRadioButton("B.Tech(Information Technology)")
                    self.d4 = QRadioButton("B.E(Electronics and Communication Engineering)")
                    self.d5 = QRadioButton("B.E(Bio-medical Engineering)")
                    self.d6 = QRadioButton("B.E(Robotics and Automation)")
                    self.d7 = QRadioButton("B.Tech(Artificial Intelligence and Data Science Engineering)")
                    self.d1.setStyleSheet("color : white")
                    self.d1.setFont(QFont("Times New Roman",16))
                    self.d2.setStyleSheet("color : white")
                    self.d2.setFont(QFont("Times New Roman",16))
                    self.d3.setStyleSheet("color : white")
                    self.d3.setFont(QFont("Times New Roman",16))
                    self.d4.setStyleSheet("color : white")
                    self.d4.setFont(QFont("Times New Roman",16))
                    self.d5.setStyleSheet("color : white")
                    self.d5.setFont(QFont("Times New Roman",16))
                    self.d6.setStyleSheet("color : white")
                    self.d6.setFont(QFont("Times New Roman",16))
                    self.d7.setStyleSheet("color : white")
                    self.d7.setFont(QFont("Times New Roman",16))
                    self.btngroup2 = QButtonGroup()
                    self.btngroup2.addButton(self.d1)
                    self.btngroup2.addButton(self.d2)
                    self.btngroup2.addButton(self.d3)
                    self.btngroup2.addButton(self.d4)
                    self.btngroup2.addButton(self.d5)
                    self.btngroup2.addButton(self.d6)
                    self.btngroup2.addButton(self.d7)
                    rb2.addWidget(self.d1)
                    rb2.addWidget(self.d2)
                    rb2.addWidget(self.d3)
                    rb2.addWidget(self.d4)
                    rb2.addWidget(self.d5)
                    rb2.addWidget(self.d6)
                    rb2.addWidget(self.d7)
                    rb2.addStretch()

                    d = QLabel("Department")
                    d.setStyleSheet("color : white")
                    d .setFont(QFont("Times New Roman",16))
                    formLayout.addRow(d,rb2)

                    

                    fee = QLineEdit()
                    fee.setMaximumWidth(500)
                    fee.setFont(QFont("Times New Roman",16))
                    my_regex1 = QRegExp("[0-9 ,'-;:]{12}")
                    my_validator = QRegExpValidator(my_regex1, fee)
                    fee.setValidator(my_validator)
                    f = QLabel("Fees Due")
                    f.setStyleSheet("color : white")
                    f .setFont(QFont("Times New Roman",16))
                    formLayout.addRow(f,fee)

                    
                    lst = []
                    lst.clear()
                    def certificate():
                        
                        if c1.isChecked() == True:
                            lst.append(c1.text())
                        if c2.isChecked() == True:
                            lst.append(c2.text())
                        if c3.isChecked() == True:
                            lst.append(c3.text())
                        if c4.isChecked() == True:
                            lst.append(c4.text())
                        if c5.isChecked() == True:
                            lst.append(c5.text())
                        if c6.isChecked() == True:
                            lst.append(c6.text())
                        if c7.isChecked() == True:
                            lst.append(c7.text())
                        if c8.isChecked() == True:
                            lst.append(c8.text())
                        if c9.isChecked() == True:
                            lst.append(c9.text())
                        if c10.isChecked() == True:
                            lst.append(c10.text())
                        if c11.isChecked() == True:
                            lst.append(c11.text())
                        if c12.isChecked() == True:
                            lst.append(c12.text())
                        if c13.isChecked() == True:
                            lst.append(c13.text())
                        if c14.isChecked() == True:
                            lst.append(c14.text())
                        if c15.isChecked() == True:
                            lst.append(c15.text())
                        if c16.isChecked() == True:
                            lst.append(c16.text())
                        if c17.isChecked() == True:
                            lst.append(c17.text())

                    def statechanged1(cbr):
                        for cb2 in (i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17):
                            
                            if cb2.text() == cbr.text():
                                if cbr.isChecked() == True:
                                    cb2.setChecked(False)
                    rb3 = QHBoxLayout()
                    c1 = QCheckBox("10th Marksheet")
                    c1.stateChanged.connect(lambda: statechanged1(c1))
                    c1.setStyleSheet("color : white")
                    c1.setFont(QFont("Times New Roman",16))

                    
                    rb3.addWidget(c1)

                    c2 = QCheckBox("11th Marksheet")
                    c2.stateChanged.connect(lambda: statechanged1(c2))
                    c2.setStyleSheet("color : white")
                    c2.setFont(QFont("Times New Roman",16))
                    
                    rb3.addWidget(c2)
                    rb3.addStretch()
                    ssc = QLabel("Select Submitted Certificate      ")
                    ssc.setStyleSheet("color : white")
                    ssc.setFont(QFont("Times New Roman",16))
                    formLayout.addRow(ssc,rb3)

                    rb4 = QHBoxLayout()
                    c3 = QCheckBox("12th Marksheet")
                    c3.stateChanged.connect(lambda: statechanged1(c3))
                    c3.setStyleSheet("color : white")
                    c3.setFont(QFont("Times New Roman",16))
                    
                    rb4.addWidget(c3)

                    c4 = QCheckBox("Community Certificate")
                    c4.stateChanged.connect(lambda: statechanged1(c4))
                    c4.setStyleSheet("color : white")
                    c4.setFont(QFont("Times New Roman",16))
                    
                    rb4.addWidget(c4)
                    rb4.addStretch()
                    formLayout.addRow("",rb4)    

                    rb5 = QHBoxLayout()
                    c5 = QCheckBox("1st Semester Marksheet")
                    c5.stateChanged.connect(lambda: statechanged1(c5))
                    c5.setStyleSheet("color : white")
                    c5.setFont(QFont("Times New Roman",16))
                    
                    rb5.addWidget(c5)

                    c6 = QCheckBox("2nd Semester Marksheet")
                    c6.stateChanged.connect(lambda: statechanged1(c6))
                    c6.setStyleSheet("color : white")
                    c6.setFont(QFont("Times New Roman",16))
                    
                    rb5.addWidget(c6)
                    rb5.addStretch()
                    formLayout.addRow("",rb5)

                    rb6 = QHBoxLayout()
                    c7 = QCheckBox("3rd Semester Marksheet")
                    c7.stateChanged.connect(lambda: statechanged1(c7))
                    c7.setStyleSheet("color : white")
                    c7.setFont(QFont("Times New Roman",16))
                    
                    rb6.addWidget(c7)

                    c8 = QCheckBox("4th Semester Marksheet")
                    c8.stateChanged.connect(lambda: statechanged1(c8))
                    c8.setStyleSheet("color : white")
                    c8.setFont(QFont("Times New Roman",16))
                    
                    rb6.addWidget(c8)
                    rb6.addStretch()
                    formLayout.addRow("",rb6)
                    
                    rb7 = QHBoxLayout()
                    c9 = QCheckBox("5th Semester Marksheet")
                    c9.stateChanged.connect(lambda: statechanged1(c9))
                    c9.setStyleSheet("color : white")
                    c9.setFont(QFont("Times New Roman",16))
                    
                    rb7.addWidget(c9)

                    c10 = QCheckBox("6th Semester Marksheet")
                    c10.stateChanged.connect(lambda: statechanged1(c10))
                    c10.setStyleSheet("color : white")
                    c10.setFont(QFont("Times New Roman",16))
                    
                    rb7.addWidget(c10)
                    rb7.addStretch()
                    formLayout.addRow("",rb7)

                    rb8 = QHBoxLayout()
                    c11 = QCheckBox("7th Semester Marksheet")
                    c11.stateChanged.connect(lambda: statechanged1(c11))
                    c11.setStyleSheet("color : white")
                    c11.setFont(QFont("Times New Roman",16))
                    
                    rb8.addWidget(c11)

                    c12 = QCheckBox("8th Semester Marksheet")
                    c12.stateChanged.connect(lambda: statechanged1(c12))
                    c12.setStyleSheet("color : white")
                    c12.setFont(QFont("Times New Roman",16))
                    
                    rb8.addWidget(c12)
                    rb8.addStretch()
                    formLayout.addRow("",rb8)

                    rb9 = QHBoxLayout()
                    c13 = QCheckBox("Consolidated statement")
                    c13.stateChanged.connect(lambda: statechanged1(c13))
                    c13.setStyleSheet("color : white")
                    c13.setFont(QFont("Times New Roman",16))
                    
                    rb9.addWidget(c13)

                    c14 = QCheckBox("Degree Certificate")
                    c14.stateChanged.connect(lambda: statechanged1(c14))
                    c14.setStyleSheet("color : white")
                    c14.setFont(QFont("Times New Roman",16))
                
                    rb9.addWidget(c14)
                    rb9.addStretch()
                    formLayout.addRow("",rb9)

                    rb10 = QHBoxLayout()
                    c15 = QCheckBox("Conduct Certificate")
                    c15.stateChanged.connect(lambda: statechanged1(c15))
                    c15.setStyleSheet("color : white")
                    c15.setFont(QFont("Times New Roman",16))
                    
                    rb10.addWidget(c15)

                    c16 = QCheckBox("Course completion Certificate")
                    c16.stateChanged.connect(lambda: statechanged1(c16))
                    c16.setStyleSheet("color : white")
                    c16.setFont(QFont("Times New Roman",16))
                    
                    rb10.addWidget(c16)
                    rb10.addStretch()
                    formLayout.addRow("",rb10)

                    rb11 = QHBoxLayout()
                    c17 = QCheckBox("College TC")
                    c17.stateChanged.connect(lambda: statechanged1(c17))
                    c17.setStyleSheet("color : white")
                    c17.setFont(QFont("Times New Roman",16))
                    
                    rb11.addWidget(c17)
                    rb11.addStretch()
                    formLayout.addRow("",rb11)

        ###############################################################################
                    def statechanged(cbc):
                        i18.setChecked(False)
                        for cb in (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17):
                            if cbc.text() == cb.text():
                                if cbc.isChecked() == True:
                                    cb.setChecked(False)
                    ilist = []
                    def cissued():
                        if i1.isChecked() == True:
                            ilist.append(i1.text())
                        if i2.isChecked() == True:
                            ilist.append(i2.text())
                        if i3.isChecked() == True:
                            ilist.append(i3.text())
                        if i4.isChecked() == True:
                            ilist.append(i4.text())
                        if i5.isChecked() == True:
                            ilist.append(i5.text())
                        if i6.isChecked() == True:
                            ilist.append(i6.text())
                        if i7.isChecked() == True:
                            ilist.append(i7.text())
                        if i8.isChecked() == True:
                            ilist.append(i8.text())
                        if i9.isChecked() == True:
                            ilist.append(i9.text())
                        if i10.isChecked() == True:
                            ilist.append(i10.text())
                        if i11.isChecked() == True:
                            ilist.append(i11.text())
                        if i12.isChecked() == True:
                            ilist.append(i12.text())
                        if i13.isChecked() == True:
                            ilist.append(i13.text())
                        if i14.isChecked() == True:
                            ilist.append(i14.text())
                        if i15.isChecked() == True:
                            ilist.append(i15.text())
                        if i16.isChecked() == True:
                            lst.append(i16.text())
                        if i17.isChecked() == True:
                            ilist.append(i17.text())
                        if i18.isChecked() == True:
                            ilist.append(i18.text())

                    ci1 = QHBoxLayout()
                    i1 = QCheckBox("10th Marksheet")
                    i1.stateChanged.connect(lambda: statechanged(i1))
                    i1.setStyleSheet("color : white")
                    i1.setFont(QFont("Times New Roman",16))
                    
                    ci1.addWidget(i1)

                    i2 = QCheckBox("11th Marksheet")
                    i2.stateChanged.connect(lambda: statechanged(i2))
                    i2.setStyleSheet("color : white")
                    i2.setFont(QFont("Times New Roman",16))
                    
                    ci1.addWidget(i2)
                    ci1.addStretch()
                    ssc = QLabel("Certificates issued")
                    ssc.setStyleSheet("color : white")
                    ssc.setFont(QFont("Times New Roman",16))
                    formLayout.addRow(ssc,ci1)

                    ci2 = QHBoxLayout()
                    i3 = QCheckBox("12th Marksheet")
                    i3.stateChanged.connect(lambda: statechanged(i3))
                    i3.setStyleSheet("color : white")
                    i3.setFont(QFont("Times New Roman",16))
                    
                    ci2.addWidget(i3)

                    i4 = QCheckBox("Community Certificate")
                    i4.stateChanged.connect(lambda: statechanged(i4))
                    i4.setStyleSheet("color : white")
                    i4.setFont(QFont("Times New Roman",16))
                    
                    ci2.addWidget(i4)
                    ci2.addStretch()
                    formLayout.addRow("",ci2)    

                    ci3 = QHBoxLayout()
                    i5 = QCheckBox("1st Semester Marksheet")
                    i5.stateChanged.connect(lambda: statechanged(i5))
                    i5.setStyleSheet("color : white")
                    i5.setFont(QFont("Times New Roman",16))
                    
                    ci3.addWidget(i5)

                    i6 = QCheckBox("2nd Semester Marksheet")
                    i6.stateChanged.connect(lambda: statechanged(i6))
                    i6.setStyleSheet("color : white")
                    i6.setFont(QFont("Times New Roman",16))
                    
                    ci3.addWidget(i6)
                    ci3.addStretch()
                    formLayout.addRow("",ci3)

                    ci4 = QHBoxLayout()
                    i7 = QCheckBox("3rd Semester Marksheet")
                    i7.stateChanged.connect(lambda: statechanged(i7))
                    i7.setStyleSheet("color : white")
                    i7.setFont(QFont("Times New Roman",16))
                    
                    ci4.addWidget(i7)

                    i8 = QCheckBox("4th Semester Marksheet")
                    i8.stateChanged.connect(lambda: statechanged(i8))
                    i8.setStyleSheet("color : white")
                    i8.setFont(QFont("Times New Roman",16))
                    
                    ci4.addWidget(i8)
                    ci4.addStretch()
                    formLayout.addRow("",ci4)
                    
                    ci5 = QHBoxLayout()
                    i9 = QCheckBox("5th Semester Marksheet")
                    i9.stateChanged.connect(lambda: statechanged(i9))
                    i9.setStyleSheet("color : white")
                    i9.setFont(QFont("Times New Roman",16))
                    
                    ci5.addWidget(i9)

                    i10 = QCheckBox("6th Semester Marksheet")
                    i10.stateChanged.connect(lambda: statechanged(i10))
                    i10.setStyleSheet("color : white")
                    i10.setFont(QFont("Times New Roman",16))
                    
                    ci5.addWidget(i10)
                    ci5.addStretch()
                    formLayout.addRow("",ci5)

                    ci6 = QHBoxLayout()
                    i11 = QCheckBox("7th Semester Marksheet")
                    i11.stateChanged.connect(lambda: statechanged(i11))
                    i11.setStyleSheet("color : white")
                    i11.setFont(QFont("Times New Roman",16))
                    
                    ci6.addWidget(i11)

                    i12 = QCheckBox("8th Semester Marksheet")
                    i12.stateChanged.connect(lambda: statechanged(i12))
                    i12.setStyleSheet("color : white")
                    i12.setFont(QFont("Times New Roman",16))
                    
                    ci6.addWidget(i12)
                    ci6.addStretch()
                    formLayout.addRow("",ci6)

                    ci7 = QHBoxLayout()
                    i13 = QCheckBox("Consolidated statement")
                    i13.stateChanged.connect(lambda: statechanged(i13))
                    i13.setStyleSheet("color : white")
                    i13.setFont(QFont("Times New Roman",16))
                    
                    ci7.addWidget(i13)

                    i14 = QCheckBox("Degree Certificate")
                    i14.stateChanged.connect(lambda: statechanged(i14))
                    i14.setStyleSheet("color : white")
                    i14.setFont(QFont("Times New Roman",16))
                
                    ci7.addWidget(i14)
                    ci7.addStretch()
                    formLayout.addRow("",ci7)

                    ci8 = QHBoxLayout()
                    i15 = QCheckBox("Conduct Certificate")
                    i15.stateChanged.connect(lambda: statechanged(i15))
                    i15.setStyleSheet("color : white")
                    i15.setFont(QFont("Times New Roman",16))
                    
                    ci8.addWidget(i15)

                    i16 = QCheckBox("Course completion Certificate")
                    i16.stateChanged.connect(lambda: statechanged(i16))
                    i16.setStyleSheet("color : white")
                    i16.setFont(QFont("Times New Roman",16))
                    
                    ci8.addWidget(i16)
                    ci8.addStretch()
                    formLayout.addRow("",ci8)

                    ci9 = QHBoxLayout()
                    i17 = QCheckBox("College TC")
                    i17.stateChanged.connect(lambda: statechanged(i17))
                    i17.setStyleSheet("color : white")
                    i17.setFont(QFont("Times New Roman",16))
                    
                    ci9.addWidget(i17)

                    i18 = QCheckBox("None")
                    i18.setChecked(True)
                    i18.setStyleSheet("color : white")
                    i18.setFont(QFont("Times New Roman",16))

                    

                    ci9.addWidget(i18)
                    ci9.addStretch()
                    formLayout.addRow("",ci9)
                    


                    def upload():
                        certificate()
                        if reg_no.text() == "":
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Warning)

                                if reg_no.text() == "":
                                    msgBox.setText("Please fill the Register Number")
                                
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()
                        elif name.text() == "":
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Warning) 
                                
                                if name.text() == "":
                                    msgBox.setText("Please fill the Student Name")
                                
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()
                        elif b.text() == "":
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Warning) 
                                
                                if b.text() == "":
                                    msgBox.setText("Please fill the Batch")
                                
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()
                        elif fee.text() == "":
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Warning) 
                                
                                if fee.text() == "":
                                    msgBox.setText("Please fill the Fees Due")

                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()
                        elif lst == []:
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Warning) 
                                msgBox.setText("Please select Certificates")
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()

                        else:   
                            
                                for none in (i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17):
                                    if none.isChecked() == False:
                                        i18.setChecked(True)
                                A = reg_no.text()
                                B = name.text()
                                C = dob.date().toPyDate()
                                        
                                D = b.text()
                                for j in (self.d1,self.d2,self.d3,self.d4,self.d5,self.d6,self.d7):
                                    if j.isChecked():
                                        dept = j.text()
                                E = dept
                                F = fee.text()
                                G = str(lst)
                                cissued()
                                H = str(ilist)
                                
                                """DBname = "Student student_Database"
                                DBuser = "postgres"
                                DBPass = "12345678"
                                DBhost = "server.IT.com"
                                DBport = "5432" """

                                db = sqlite3.connect('student_Database.db')

                                cur = db.cursor()
                                #cur.execute("CREATE TABLE student_Database (Regno TEXT,Name TEXT,Dateofbirth TEXT,Batch TEXT,Department TEXT,fee TEXT,Certificates_submitted TEXT,certificates_issued TEXT)")
                                cur.execute("INSERT INTO student_Database VALUES(?,?,?,?,?,?,?,?)",(A,B,C,D,E,F,G,H))
                                cur.execute("SELECT Name FROM student_Database WHERE Regno = ?",(A,))    
                                data = cur.fetchone() 
                                db.commit()           
                                db.close
                                
                                self.close()
                            
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Information) 
                                msgBox.setText("The details of " + data[0] + " has been uploaded")
                                msgBox.setWindowTitle("Information")
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                returnValue = msgBox.exec()
                                if returnValue == QMessageBox.Ok:
                                    msgBox.close()   
                        
                        
                    a = QPushButton("   Upload   ")
                    a.setFont(QFont("Times New Roman Bold",16))
                    a.clicked.connect(upload)

                    def cancel():
                        self.close()
                        
                    c = QPushButton("Cancel")
                    c.setFont(QFont("Times New Roman Bold",16))
                    c.clicked.connect(cancel)
                    formLayout.addRow(a,c)
                    groupBox.setLayout(formLayout)
                    scroll = QScrollArea()
                    scroll.setWidget(groupBox)
                    scroll.setWidgetResizable(True)
                    layout = QVBoxLayout(self)
                    layout.addWidget(scroll)
                    self.showMaximized()
                    
    add_details()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
    app.exec()