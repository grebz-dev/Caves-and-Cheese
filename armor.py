import sys, os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QMainWindow, QLineEdit

class ArmorWidget(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		hbox = QHBoxLayout()
		vbox = QVBoxLayout()
		
		self.head = QLineEdit()
		self.torso = QLineEdit()
		self.arms = QLineEdit()
		self.legs = QLineEdit()
		self.feet = QLineEdit()
		
		vbox.addWidget(self.head)
		vbox.addWidget(self.torso)
		vbox.addWidget(self.arms)
		vbox.addWidget(self.legs)
		vbox.addWidget(self.feet)
		
		armor_guy = QLabel(self)
		armor_guy.setPixmap(QPixmap(resource_path("armor_guy.png")))
		hbox.addWidget(armor_guy)
		hbox.addLayout(vbox)
		self.setLayout(hbox)

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)
	
if __name__ == '__main__':

	app = QApplication(sys.argv)
	w = ArmorWidget();
	w.show()
	sys.exit(app.exec_())