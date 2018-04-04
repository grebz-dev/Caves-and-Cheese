from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit
from PyQt5.QtCore import pyqtSignal

class NotesWidget(QWidget):

	def __init__(self,player):
		super().__init__()
		self.initUI(player)
		
	def initUI(self, player):
		layout = QVBoxLayout()
		self.textedit = QPlainTextEdit()

		self.textedit.textChanged.connect(lambda text=self.textedit.toPlainText, player=player : self.valUpdate(text, player))
		layout.addWidget(self.textedit)
		self.setLayout(layout)
		
	def valUpdate(self, text, player):
		player.updateNotes(text)