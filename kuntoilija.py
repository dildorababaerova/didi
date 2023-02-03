#KUNTOJLIJAN TIEDOT OLIO OHJELMOINTINA
#====================================

#KIRJASTOT JA MODULIT (LIBRARIES AND MODULES)
#--------------------------------------------

import fitnes

#LUOKKAMÄÄRÄYKSET (CLASS DEFINITION)

# Kuntoilija - luokka Yliluokka Juniorikuntoilijalle (super class)
class Kuntoilija:
    """Luokka kuntoilijan tietoa varten"""

    #Olimuodostin eli konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        #MÄÄRITELLÄÄN TULEVAN OLION OMINAISUUDET (PROPERTY), LUOKAN KENTÄÄT (FIELD)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitnes.laske_bmi(self.paino, self.pituus)
        

    # Metodi rasvaprosentin laskimeseen (aikuinen / yleinen)
    def rasvaprosentti (self):
        self.rasvaprosentti = fitnes.aikuisen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti 


# JunioriKuntoilija_luokka Kuntoilija-luokan aliluokka(subclass)
class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille"""

    #Konstruktori

    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään periytyminen, mitä ominaisuuksia perii kun luokan sisälle aliluokka
        super().__init__(nimi, pituus, paino, ika, sukupuoli)
        
    # Metodi rasvaprosentin laskimeseen (ylikirjoitettu lapsen metodilla)
    def rasvaprosentti (self):
        self.rasvaprosentti = fitnes.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti 

   
   
if __name__ == "__main__":
            
    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija("Kalle Kuntoilija", 171, 65, 40, 1)
    print(kuntoilija.nimi, "painaa",  kuntoilija.paino, "kg")
    # print('painoindeksi on', kuntoilija.painoindeksi())
    print('painoindeksi on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija('Aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, "painaa",  juniorikuntoilija.paino, "kg")
    # print('painoindeksi on', juniorikuntoilija.painoindeksi())
    print('painoindeksi on', juniorikuntoilija.rasvaprosentti())         