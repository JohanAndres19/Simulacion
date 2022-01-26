import sys
from PyQt5.QtGui import QTextOption 
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from qt_for_python.uic.ventanaS import *

import random
#-------------------------------------
#------------- Interfaz---------------

class Ventana_principal(QMainWindow):
    def __init__(self,modelo):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo=modelo
        self.controlador=Controlador(self)
        #----------------------------
        self.setWindowTitle("SIMULADOR")
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setWordWrapMode(QTextOption.NoWrap)
        #--------------------------------
        self.ui.text_ingresar.setClearButtonEnabled(True)
        self.ui.tableWidget.setVisible(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def Get_modelo(self):
        return self.modelo

#--------------------------------------
#--------------------------------------

class Controlador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.boton_encriptar.clicked.connect(lambda:print("hola"))

#---------------------------------------
#---------------------------------------
class Modelo ():
    def __init__(self) :
        self.ventana = Ventana_principal(self)

    def Simular (self):
        lista=[]
        diferencia=0
        
        while diferencia !=3:
            cara_moneda = random.randint(0,99)
            if cara_moneda <50:
                lista.append('Ca')
            elif cara_moneda >=50:
                lista.append('Cr')
            if abs(lista.count('Ca')-lista.count('Cr'))==3:
                diferencia= abs(lista.count('Ca')-lista.count('Cr'))        
        else:
            print('psadk',len(lista))
            for i in lista:
                print(i,' ',end='')    

    def Mostrar_tabla(self):  
        labels_en_y=[]
        if self.ventana.ui.tableWidget.rowCount()!=0:
            self.ventana.ui.tableWidget.clearContents()
            self.ventana.ui.tableWidget.setRowCount(0)
        self.ventana.ui.tableWidget.setHorizontalHeaderLabels(["NUMERO DE JUEGO","# CARAS","# CRUCES","# LANZAMIENTOS",])
        fila=0
        for i in self.cursor.Get_Cursor():
            columna=0
            self.ventana.ui.tableWidget.insertRow(fila)
            for j in i :
                celda= QTableWidgetItem(str(j))
                celda.setTextAlignment(Qt.AlignHCenter)
                self.ventana.ui.tableWidget.setItem(fila,columna,celda)
                columna+=1
            fila+=1 
        self.ventana.ui.tableWidget.insertRow(len(self.cursor.Get_Cursor()))
        valores =[' ','0',str(len(self.cursor.Get_Cursor())+1),'0']
        columna=0
        for i in valores:
            celda= QTableWidgetItem(str(i))
            celda.setTextAlignment(Qt.AlignHCenter)
            print(i)
            self.ventana.ui.tableWidget.setItem(len(self.cursor.Get_Cursor()),columna,celda)
            columna+=1 

        for i in range(len(self.cursor.Get_Cursor())+1):
            labels_en_y.append(str(i))
        self.ventana.ui.tableWidget.setVerticalHeaderLabels(labels_en_y)  
        self.ventana.ui.tableWidget.setVisible(True) 
        

    def Get_ventana(self):
        return self.ventana    

#--------------------------------------
#---------------Main------------------- 
if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())
