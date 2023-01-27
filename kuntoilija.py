#KUNTOJLIJAN TIEDOT OLIO OHJELMOITINA
#====================================

#kIRJASTOT JA MODULIT (LIBRARIES AND MODULES)
#--------------------------------------------

import fitnes

#LUKKAMÄÄRÄYKSET (CLASS DEFINITION)


class Kuntoilija:
    """Luokka kuntojlijen tietoa varten"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        #MÄÄRITELLÄÄN TULEVAN OLION OMINAISUUDET (PROPERTY), LUOKAN KENTÄÄT (FIELD)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

        if __name__ == "__main__":
            
            #Luodaan olio luokasta Kuntoilija
            kuntoilija = Kuntoilija("Kalle Kuntoilija", 171, 65, 40, 1)
            print(kuntoilija.nimi, "painaa",  kuntoilija.paino, "kg")

        