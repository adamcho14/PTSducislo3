import random
import itertools
from zapasVskupine import zapasVskupine
from zapas import Zapas

class FIFAWorldRanking():

	def __init__(self, pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8):
		self.counter = 0
		self.pole = []
		self.skupina1 = zapasVskupine(pole1)
		self.skupina2 = zapasVskupine(pole2)
		self.skupina3 = zapasVskupine(pole3)
		self.skupina4 = zapasVskupine(pole4)
		self.skupina5 = zapasVskupine(pole5)
		self.skupina6 = zapasVskupine(pole6)
		self.skupina7 = zapasVskupine(pole7)
		self.skupina8 = zapasVskupine(pole8)

	def posunOden(self):
		self.counter += 1

		if self.counter < 12:
			self.skupina1.posun()
			self.skupina2.posun()
			self.skupina3.posun()
			self.skupina4.posun()
			self.skupina5.posun()
			self.skupina6.posun()
			self.skupina7.posun()
			self.skupina8.posun()
		else:
			a = self.skupina1.posun()
			b = self.skupina2.posun()
			c = self.skupina3.posun()
			d = self.skupina4.posun()
			e = self.skupina5.posun()
			f = self.skupina6.posun()
			g = self.skupina7.posun()
			h = self.skupina8.posun()
			try:
				for i in a: self.pole.append(i)
				for i in b: self.pole.append(i)
				for i in c: self.pole.append(i)
				for i in d: self.pole.append(i)
				for i in e: self.pole.append(i)
				for i in f: self.pole.append(i)
				for i in g: self.pole.append(i)
				for i in h: self.pole.append(i)
				print("ahoooooj")
				self.finalZapasy()
			except:
				pass



	def finalZapasy(self):
		self.skupina = zapasVskupine(self.pole).finalAllZapasy()
		pocet = 1
		array = []
		for i in self.skupina:
			array.append(i)
		print("Prvy skoncil: " + array[0])
		print("Druhy skoncil: " + array[1])

	def allZapasy(self):
		for i in range(13):
			self.posunOden()



pole1 = ["Slovensko", "Madarsko", "Ukrajina", "Polsko"]
pole2 = ["Cesko", "Nemecko", "Rakusko", "Francuzsko"]
pole3 = ["Svajciarsko", "Norsko", "Svedsko", "Taliansko"]
pole4 = ["Spanielsko", "Kazachstan", "Srbsko", "Chorvatsko"]
pole5 = ["Anglisko", "Island", "Dansko", "Ukrajina"]
pole6 = ["Belgisko", "Luxembursko", "Irsko", "Skotsko"]
pole7 = ["Kosovo", "Severne_Irsko", "Litva", "Albnasko"]
pole8 = ["Rumunsko", "Wales", "Rusko", "Turecko"]

g = FIFAWorldRanking(pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8)
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()
##g.posunOden()

##g.allZapasy()

