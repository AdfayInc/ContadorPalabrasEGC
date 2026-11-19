import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #Carga de nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
    def ContarPalabras(self):
        #Recuperar texto✅
        texto = self.edtCaracteres.toPlainText()
        #Separar las palabras✅
        textoSeparado = texto.split()
        print(textoSeparado)
        #Contar las palabras 
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras:{cantidadPalabras}")
        #Contar los caracteres
        totalCaracteres = 0 
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        
        #Logica
        if cantidadPalabras >=20:
            self.tvPalabras.setStyleSheet("color: red;")
        else: 
            self.tvPalabras.setStyleSheet("color: black;")
        if totalCaracteres >=120:
            self.tvCaracteres.setStyleSheet("color: red;")
        else: 
            self.tvCaracteres.setStyleSheet("color: black;")
            
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())

