import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("contadorPalabras.ui", self)

        self.btnContar.clicked.connect(self.contarPalabras)

    def contarPalabras(self):
        texto = str(self.edtCaracteres.toPlainText())

        textoSeparado = len(texto.split())

        textoLongitud = len(texto)

        self.tvPalabras.setText(f"Palabras: {textoSeparado}")
        self.tvCaracteres.setText(f"Caracteres: {textoLongitud}")


app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())