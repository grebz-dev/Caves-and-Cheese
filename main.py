import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from PlayerWidget import PlayerWidget
from open_new import SplashWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
	
class MainWindow(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('Caves & Cheese')
		self.splash=SplashWidget()
		self.setCentralWidget(self.splash)
		self.setWindowIcon(QtGui.QIcon('logo.png'))
		self.move(300,500)
		self.resize(0,self.height())
		self.splash.fileOpened.connect(self.initGame)
	
	@pyqtSlot(str)
	def initGame(self, filename):
		player = PlayerWidget(filename)
		self.setCentralWidget(player)
		self.resize(0,self.height())
		
if __name__ == '__main__':

	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())