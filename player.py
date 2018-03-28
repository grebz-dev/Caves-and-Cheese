import random
import sys, os

class Player(QGroupBox):	

	def __init__(self, statFile):
		self.inventory = []
		self.stats = {}
		self.notes = {}
		self.skills = {}
		self.health = 20
		self.parseStats(statFile)
		self.initUI()
		
	def updateStat(self, key, value):
		self.stats[key]=value
		print(self.stats)
		
	def updateInventory(self, item, index):
		self.inventory[index]=item
		print(self.inventory)
	
	def parseStats(self, filename):
		file = open(filename)
		for line in file:
			if line and not line.startswith('#') and not line.startswith("\n"):
				if line.startswith('@'):
					self.inventory.append(line[1:].strip())
				if line.startswith('^'):
					self.skills.append(line[1:].strip())
				if line.startswith('?'):
					self.notes.append(line[1:].strip())
				else:
					split = line.split('=')
					self.stats[split[0]]=split[1].strip()
	
	def export(self, filename):
		file = open(filename,'w+')
		
		for key, value in self.stats.items():
			file.write(key+"="+str(value)+"\n")
		
		for item in self.inventory:
			if not item == "":
				file.write('@'+item+"\n")