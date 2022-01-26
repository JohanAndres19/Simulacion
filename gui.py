import sys
from PyQt5.QtGui import QTextOption 
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from qt_for_python.uic.ventanaS import *
import random
import numpy as np
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
        self.ui.text_ingresar.setAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setVisible(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.setColumnCount(5)
    def Get_modelo(self):
        return self.modelo

#--------------------------------------
#--------------------------------------

class Controlador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.boton_encriptar.clicked.connect(lambda:self.ventana.Get_modelo().Simular())

#---------------------------------------
#---------------------------------------
class Modelo ():
    def __init__(self) :
        self.ventana = Ventana_principal(self)

    def Simular (self):
        self.matriz=[]
        ingresado= int(self.ventana.ui.text_ingresar.text())
        for i in range(ingresado):
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
                self.matriz.append([i+1,lista.count('Ca'),lista.count('Cr'),len(lista),8-len(lista)])
        self.Mostrar_tabla()

    def Mostrar_tabla(self):  
        labels_en_y=[]
        if self.ventana.ui.tableWidget.rowCount()!=0:
            self.ventana.ui.tableWidget.clearContents()
            self.ventana.ui.tableWidget.setRowCount(0)
        self.ventana.ui.tableWidget.setHorizontalHeaderLabels([" NUMERO DE JUEGO "," # CARAS "," # CRUCES ","# LANZAMIENTOS"," GANADOS "])
        fila=0
        for i in self.matriz:
            columna=0
            self.ventana.ui.tableWidget.insertRow(fila)
            for j in i :
                celda= QTableWidgetItem(str(j))
                celda.setTextAlignment(Qt.AlignHCenter)
                self.ventana.ui.tableWidget.setItem(fila,columna,celda)
                columna+=1
            fila+=1 
        self.ventana.ui.tableWidget.setVerticalHeaderLabels([])  
        self.ventana.ui.tableWidget.setVisible(True) 
        arreglo= np.array(self.matriz)
        self.ventana.ui.textEdit.setText('Cantidad de Juegos: '+str(len(self.matriz))+'\n'+'Promedio lanzamientos: '+"{:.3f}".format(np.average(arreglo[:,3]))+'\n'+'Promedio ganado: '+"{:.3f}".format(np.average(arreglo[:,4])))

    def Get_ventana(self):
        return self.ventana    

#--------------------------------------
#---------------Main------------------- 
if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())
