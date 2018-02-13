import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PlayerWidget import PlayerWidget

if __name__ == '__main__':

	app = QApplication(sys.argv)

	w = QWidget()
	w.resize(600, 800)
	w.setWindowTitle('Caves & Cheese')
	statfile = open("Paul.cnc")
	player = PlayerWidget(statfile)
	w.addWidget(player)
	w.show()
	sys.exit(app.exec_())