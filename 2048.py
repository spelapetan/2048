import tkinter as tk
import model

VELIKOST = 4

class IgralnaPlosca:
    def __init__(self, okno):
        self.m = model.Matrix(VELIKOST, VELIKOST)
        self.stevec = 0
        
        self.okno = okno
        zgornja_vrstica = tk.Frame(okno)
        zgoraj = tk.Frame(zgornja_vrstica)
        spodaj = tk.Frame(zgornja_vrstica)
        self.okvir_matrike = tk.Frame(okno)
        zgornja_vrstica.pack()
        zgoraj.pack()
        spodaj.pack()
        self.okvir_matrike.pack()

        self.pozdrav = tk.Label(zgoraj, text='Pozdravljeni v igrici 2048!', font=("Helvetica", 15, "bold"))
        self.stevilo_potez = tk.Label(spodaj, text='0', font=("Helvetica", 15, "bold"))
        self.nazaj = tk.Button(spodaj, text='NAZAJ', font=("Helvetica", 15, "bold"), command=self.razveljavi)
        
        
        self.pozdrav.grid(row=0, column=0)
        self.stevilo_potez.grid(row=0, column=1)
        self.nazaj.grid(row=0, column=2)

        self.okno.bind('<Key>', self.tipka)

        self.nastavi_stevilke()

    def tipka(self, event):
        if event.keysym == 'Left':
            self.m.premik_levo()
            self.osvezi()
        elif event.keysym == 'Right':
            self.m.premik_desno()
            self.osvezi()
        elif event.keysym == 'Up':
            self.m.premik_gor()
            self.osvezi()
        elif event.keysym == 'Down':
            self.m.premik_dol()
            self.osvezi()
        
    def nastavi_stevilke(self):
        for i in range(VELIKOST):
            for j in range(VELIKOST):
                a_ij = self.m.doloceni_element(i, j)
                besedilo = a_ij
                if a_ij == 0:
                    besedilo = ''
                elif a_ij == 2048:
                    self.zmaga()
                barve = {'': 'snow',
                         '2': 'navajo white',
                         '4': 'PeachPuff2',
                         '8': 'light salmon',
                         '16': 'coral',
                         '32': 'dark orange',
                         '64': 'yellow',
                         '128': 'green yellow',
                         '256': 'lime green',
                         '512': 'aquamarine',
                         '1024': 'DodgerBlue2',
                         '2048': 'gold'}
                tk.Label(self.okvir_matrike, text='{}'.format(besedilo), font=("Helvetica", 50, "bold"), 
                        borderwidth=2, relief='solid', height=2, width=4, 
                        bg=barve.get('{}'.format(str(besedilo)), 'grey')).grid(row=i, column=j)

    def razveljavi(self):
        self.m.prejsnja_matrika()
        self.pozdrav.config(text='Odlično vam gre.')
        self.nastavi_stevilke()
        self.pristej_potezo()
        self.nazaj.configure(state=tk.DISABLED)

    def osvezi(self):
        if self.m.ali_je_matrika_ok() is True:
            self.m.dodaj_stevilo()
            self.pozdrav.config(text='Odlično vam gre.')
            self.nastavi_stevilke()
            self.pristej_potezo()
            self.nazaj.configure(state=tk.NORMAL)
        else:
            self.koncaj_igro()

    def zmaga(self):
        self.pozdrav.config(text='Čestitamo, zmagali ste!')

    def koncaj_igro(self):
        self.pozdrav.config(text='Igre je konec, ker ni več možnih potez.')
        self.okno.unbind('<Key>')
        self.nazaj.configure(state=tk.DISABLED)

    def pristej_potezo(self):
        self.stevec += 1
        self.stevilo_potez.config(text='{}'.format(self.stevec))


okno = tk.Tk()
moj_program = IgralnaPlosca(okno)
okno.mainloop()
