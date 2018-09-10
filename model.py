import random
import copy

class Matrix:
    def __init__(self, vrstica=4, stolpec=4):
        self.vrstica = vrstica
        self.stolpec = stolpec

        self.matrika = []
        self.stara_matrika = []

        #naredimo matriko velikosti vrstica * stolpec in jo zapolnimo z 0:
        for i in range(self.vrstica):
            vr = []
            for j in range(self.stolpec):
                vr.append(0)
            self.matrika.append(vr)
        self.dodaj_stevilo()
        
    def __str__(self):
        return '{}'.format(self.matrika)

    def __repr__(self):
        lepa_matrika = ''
        for i in range(len(self.matrika)):
            lepa_matrika += '{}'.format(self.matrika[i])
            if i != len(self.matrika) - 1:
                lepa_matrika += '\n'
        return '{}'.format(lepa_matrika)

    def dodaj_stevilo(self):
        polje = []
        for st in range(self.vrstica):
            polje.append(st)
        i = 0
        while i == 0:
            izbrana_vrstica = random.choice(polje)
            izbran_stolpec = random.choice(polje)

            polozeno_stevilo = [2, 2, 2, 2, 4]
            izbrano_stevilo = random.choice(polozeno_stevilo)
            if self.matrika[izbrana_vrstica][izbran_stolpec] == 0:
                self.matrika[izbrana_vrstica][izbran_stolpec] = izbrano_stevilo
                i += 1
        #lahko se postavi sam če je 0

    def premik_levo(self):
        self.shrani_zgodovino()
        
        # funkcija vse postavi na levo in sešteje
        for i in range(self.vrstica):
            elementi = []
            # neničelne elemente postavimo v seznam elementi
            for j in range(self.stolpec):
                a_ij = self.matrika[i][j]
                if a_ij != 0:
                    elementi.append(a_ij)

            # seštejemo enake
            for x in range(len(elementi) - 1):
                if elementi[x] == elementi[x + 1]:
                    elementi[x] = elementi[x] * 2
                    elementi[x + 1] = 0

            # odstranimo 0 iz seštevanja zgoraj
            urejeni_elementi = []
            for e in elementi:
                if e != 0:
                    urejeni_elementi.append(e)
                
            while len(urejeni_elementi) < self.stolpec:
                urejeni_elementi.append(0)
            self.matrika[i] = urejeni_elementi

    def premik_desno(self):
        self.shrani_zgodovino()
        
        for i in range(self.vrstica):
            elementi = []
            for j in range(self.stolpec):
                a_ij = self.matrika[i][j]
                if a_ij != 0:
                    elementi.append(a_ij)

            elementi2 = elementi[::-1]
            for x in range(len(elementi2) - 1):
                if elementi2[x] == elementi2[x + 1]:
                    elementi2[x] = elementi2[x] * 2
                    elementi2[x + 1] = 0

            urejeni_elementi = []
            for e in elementi2[::-1]:
                if e != 0:
                    urejeni_elementi.append(e)
                    
            while len(urejeni_elementi) < self.stolpec:
                urejeni_elementi.insert(0, 0)
            self.matrika[i] = urejeni_elementi

    def premik_gor(self):
        self.shrani_zgodovino()
        
        #vse postavimo gor in seštejemo
        n = 0
        while n < self.stolpec:
            elementi = []
            #zberemo neničelne elemente
            for i in range(self.vrstica):
                a_in = self.matrika[i][n]
                if a_in != 0:
                    elementi.append(a_in)

            # seštejemo enake
            for x in range(len(elementi) - 1):
                if elementi[x] == elementi[x + 1]:
                    elementi[x] = elementi[x] * 2
                    elementi[x + 1] = 0

            # odstranimo 0 iz seštevanja zgoraj
            urejeni_elementi = []
            for e in elementi:
                if e != 0:
                    urejeni_elementi.append(e)
            
            #dodamo ničle
            while len(urejeni_elementi) < self.stolpec:
                urejeni_elementi.append(0)
            #postavimo jih v stolpec
            for i in range(self.vrstica):
                self.matrika[i][n] = urejeni_elementi[i]
            n += 1

    def premik_dol(self):
        self.shrani_zgodovino()
        
        n = 0
        while n < self.stolpec:
            elementi = []
            for i in range(self.vrstica):
                a_in = self.matrika[i][n]
                if a_in != 0:
                    elementi.append(a_in)

            elementi2 = elementi[::-1]
            for x in range(len(elementi2) - 1):
                if elementi2[x] == elementi2[x + 1]:
                    elementi2[x] = elementi2[x] * 2
                    elementi2[x + 1] = 0

            urejeni_elementi = []
            for e in elementi2[::-1]:
                if e != 0:
                    urejeni_elementi.append(e)
            
            while len(urejeni_elementi) < self.vrstica:
                urejeni_elementi.insert(0, 0)

            for i in range(self.vrstica):
                self.matrika[i][n] = urejeni_elementi[i]
            n += 1

    def doloceni_element(self, i, j):
        return self.matrika[i][j]

    def shrani_zgodovino(self):
        self.stara_matrika = copy.deepcopy(self.matrika)

    def prejsnja_matrika(self):
        self.matrika = self.stara_matrika

    def ali_je_matrika_ok(self):
        for i in range(self.vrstica):
            for j in range(self.stolpec):
                if self.matrika[i][j] == 0:
                    return True
        return False
