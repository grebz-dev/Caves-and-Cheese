import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from tabs import MultiTabWidget
from open_new import SplashWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
from player import Player

	
class MainWindow(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('Caves & Cheese')
		self.splash=SplashWidget()
		self.setCentralWidget(self.splash)
		self.setWindowIcon(QtGui.QIcon(resource_path('logo.png')))
		self.splash.start.connect(self.initGame)
	
	@pyqtSlot(Player)
	def initGame(self, player):
		tabs = MultiTabWidget(player)
		self.setCentralWidget(tabs)
		self.adjustSize()
		
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)		

if __name__ == '__main__':

	app = QApplication(sys.argv)
	#app.setStyleSheet()
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())