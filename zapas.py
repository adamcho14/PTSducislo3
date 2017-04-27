from random import randint

class Zapas():

    def __init__(self, a, b):
        self.druzstvoA = a
        self.druzstvoB = b
        self.dictA = dict()
        self.dictB = dict()


    def hraj(self):
        vysledokA = randint(0,9)
        vysledokB = randint(0,9)

        if vysledokA == 0 and vysledokB == 0:
            print("Stav zapasu je 0:0")
            return (0,0)
        print("Vysledok: " + str(vysledokA) + " : " + str(vysledokB))
        pred = randint(0,20)
        for i in range(1,vysledokA+1):
            self.dictA[i] = pred
            pred = randint(pred,90)

        pred = randint(0,20)
        for i in range(1,vysledokB+1):
            self.dictB[i] = pred
            pred = randint(pred,90)

        print(self.druzstvoA + " stretilo tieto goly: ")
        for k in self.dictA:
            print(str(k) + "   " + str(self.dictA[k]))

        print(self.druzstvoB +" stretilo tieto goly: ")
        for k in self.dictB:
            print(str(k) + "   " + str(self.dictB[k]))

        return (vysledokA, vysledokB)


