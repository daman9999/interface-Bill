from PyQt5 import QtCore, QtGui, QtWidgets
import sys,random
from FirebaseFunction import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget ,QLabel,QMessageBox
import urllib.request
from PrintFunctionality import createAndLoadPdf

global storingList
storingList=list()
storingList=getImgUrlAfterCheckingTrue(convictDict)



class Ui_MainWindow(object):
    
            
            
    def msgbtn(i):
       print("Button clicked is:",i)
       
    def mesg(self,txt):          
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(txt)
            msg.setWindowTitle("MessageBox demo")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(self.msgbtn)
            retval = msg.exec_()
    global count
    count=0
    
    def labelCode(self,count):
            self.textEdit_3.setText("rs. 2000")
            global val
            val=self.textEdit_3.toPlainText
            self.textEdit_2.setText("True")
            url = storingList[count]  
            global printUrl
            printUrl=url                  
            print(f"PREV count ={count}")
            data = urllib.request.urlopen(url).read()
            image = QtGui.QImage()
            image.loadFromData(data)
            self.label.setPixmap(QtGui.QPixmap(image))
            
    def search_Key(printUrl,dictionary):
            
            search_age = printUrl
            for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                 if age == search_age:
                     print(name)
                     return name
 
    def method3_Prev(self):
            try:      
                    global count
                    print(f"current count ={count}")        
                    if count <0:
                            raise Exception("Sorry, no numbers below zero")
                    count=count-1
                    self.labelCode(count)
            except Exception as e :
                    self.label.clear()
                    self.label.setText("Error Loading image........" )
                    self.mesg("There is no images previous to this pressing NEXT")
        
    
    def method2_Next(self):
            try:
                    global count
                    print(f"current count ={count}")
                    count+=1                    
                    self.labelCode(count) 
            except Exception as e :
                    print(e)
                    self.label.setText("Error Loading image........")
                    self.mesg("You reached to the END \"NO DATA\" pressing prev")
    

    
    def method1_Print(self):
        try:
            docno=random.randint(0,10)*random.randint(0,5)+random.randint(0,12)
            createAndLoadPdf(f"Mydoc{docno}.pdf",printUrl,val)
        except Exception as e:
                print(e)
                self.mesg("First load the image using NEXT AND PREV")
        
            
        

    

    def setupUi(self, MainWindow):  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(0,0,0);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 471, 501))
        self.label.setStyleSheet("color:white;\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(580, 310, 191, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"font: 75  20pt \"MS Reference Sans Serif\";\n"
"    color:rgb(255, 255, 255);\n"
"background-color: rgb(85,5,123);    \n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(137, 44, 220);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 75  20pt \"MS Reference Sans Serif\";\n"
"    color:rgb(255, 255, 255);\n"
"background-color: rgb(85,5,123);    \n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(137, 44, 220);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75  20pt \"MS Reference Sans Serif\";\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: rgb(129, 0, 0);\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(32, 106, 93);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(580, 220, 191, 31))
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 100, 61, 21))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 190, 61, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(580, 130, 191, 31))
        self.textEdit_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        


        self.pushButton_3.clicked.connect(lambda:self.method3_Prev())
        self.pushButton_2.clicked.connect(lambda:self.method2_Next())
        self.pushButton.clicked.connect(lambda:self.method1_Print())
    




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Loading your Image here........."))
        self.pushButton_3.setText(_translate("MainWindow", "Prev"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Left"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Right"))
        self.pushButton.setText(_translate("MainWindow", "Print Bill"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "Fined"))
        self.label_3.setText(_translate("MainWindow", "Checked?"))
    

 




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
