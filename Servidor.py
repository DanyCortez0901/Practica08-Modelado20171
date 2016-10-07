import sys
from PyQt4 import QtGui,QtCore, uic

class interfaz_cliente(QtGui.QMainWindow):
    def __init__(self):
        super(interfaz_cliente, self).__init__()
        uic.loadUi('Servidor.ui', self)
    	self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.show()

snake = QtGui.QApplication(sys.argv)
window = interfaz_cliente()
sys.exit(snake.exec_())
