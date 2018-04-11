import sys, os
import pickle

class Player():	

	def __init__(self):
		self.inventory = []
		self.stats = {"Range":'0', "Magic":'0' , "Melee":'0' , "Defense":'0' , "Charisma":'0' , "Healing":'0' , "Dexterity":'0' , "Intelligence":'0'}
		self.skills = []
		self.skill_num = 20
		self.health = 20
		self.notes = ""
		self.armor = {"Head":["",""],"Torso":["",""],"Arms":["",""],"Legs":["",""],"Feet":["",""]}
		self.traits = {"CHARACTER_NAME":'',"PLAYER_NAME":'',"Strength":'',"CAPACITY":'10',"Health":'',"Level":'',"SIZE":''}
		while len(self.inventory) < int(self.traits["CAPACITY"]):
			self.inventory.append("")
			
	def init_new(self,character_name, player_name,size):
		self.traits["CHARACTER_NAME"]=character_name
		self.traits["SIZE"]=size
		self.traits["PLAYER_NAME"]=player_name

	def updateStat(self, key, value):
		self.stats[key]=value
		
	def updateTrait(self, key, value):
		self.traits[key]=value
		
	def updateInventory(self, item, index):
		self.inventory[index]=item
		
	def updateInventory(self, item, index):
		self.inventory[index]=item
		
	def updateSkill(self, skill, index):
		self.skills[index]=skill
		
	def updateNotes(self, text):
		self.notes=text
		
	def updateArmor(self, location, item, buff):
		self.armor[location]=[item,buff]
	
	def export(self, filename):
		pickle.dump(self, open(filename,'wb'))
		