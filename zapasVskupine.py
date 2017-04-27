import itertools
from zapas import Zapas

class zapasVskupine():

	def __init__(self, pole):
		self.pole = pole
		self.comb = self.spravAllKombinacies()
		self.spravTabulku()

	def spravAllKombinacies(self):
		pole = list(itertools.product(self.pole, self.pole))
		for i in pole:
			if i[0] == i[1]:
				pole.remove(i)
		return pole

	def spravTabulku(self):
		self.dictTab = {}
		for i in self.pole:
			self.dictTab[i] = 0

	def posun(self):
		if len(self.comb) == 0:
			self.printujTabulku()
			dictN = dict()
			for i in range (2):
				najv = 0
				pos = None
				for i in self.dictTab:
					if self.dictTab[i] > najv:
						najv = self.dictTab[i]
						pos = i
				dictN[pos] = najv
				del self.dictTab[pos]
			print("Vsetky zapasy v skupine uz boli odohrane")
			print (dictN)
			return dictN
		else:
			print("Zapas sa odohral medzi: " + self.comb[0][0] + " a " + self.comb[0][1])
			zapas = (self.comb[0][0], self.comb[0][1])
			p = Zapas(zapas[0], zapas[1]).hraj()
			self.comb.remove(zapas)
			if p[0] == p[1]:
				self.dictTab[zapas[0]] += 1
				self.dictTab[zapas[1]] += 1
			elif p[0] < p[1]:
				self.dictTab[zapas[1]] += 1
			elif p[0] > p[1]:
				self.dictTab[zapas[0]] += 1

	def printujTabulku(self):
		dict2 = self.dictTab.copy()
		print(dict2)

	def allZapasy(self):
		for i in range(13):
			self.posun()
	def finalAllZapasy(self):
		for i in range(240):
			self.posun()
		return self.posun()











