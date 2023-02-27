#KUNTOJLIJAN TIEDOT OLIO OHJELMOINTINA
#====================================

#KIRJASTOT JA MODULIT (LIBRARIES AND MODULES)
#--------------------------------------------

import fitnes

#LUOKKAMÄÄRÄYKSET (CLASS DEFINITION)

# Kuntoilija - luokka Yliluokka Juniorikuntoilijalle (super class)
class Kuntoilija:
    """Luokka kuntoilijan tietoa varten"""

    #Olimuodostin eli konstruktori, self -> tuleva olio
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
    

    #Metodi rasvaprosenttien laskemiseen USA:n metodeilla
    def usa_rasvaprosentti_mies(self, pituus, vyotaron_ymparys, kaulan_ymparys):
        """Laskee miehen rasvaprosentin USA:n kaavalla

        Args:
            pituus (float): pituus (cm)
            kaulan_ymparys (float): kaulanympärys (cm)
            kaulan_ymparys(float): kaulan ympärys (cm)
            Returns:
            float: rasvaprosentti
        """
        usa_rasvaprosentti = fitnes.usarasvaprosenttimies(pituus, vyotaron_ymparys, kaulan_ymparys)
        return usa_rasvaprosentti
    
    def usa_rasvaprosentti_nainen(self, pituus, vyotaron_ymparys, kaulan_ymparys, lantion_ymparys):
        """_summary_

        Args:
            vyotaron_ymparys(float): vyötärön ympärysmitta (cm)
            kaulan_ymparys (float): kaulan ympärysmitta (cm)
            lantion_ymparys (float): lantion ympärysmitta (cm)
        
        Returns:
            float: rasvaprosentti

        """
        usa_rasvaprosentti = fitnes.usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys)
        return usa_rasvaprosentti
      


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