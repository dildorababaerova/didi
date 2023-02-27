#Sovellus Painoindeksin ja kehon rasvaprosentin laskemiseen
#==========================================================

# Kirjastot ja moduulit
import math

'''
pituus_metreina = pituus / 100

#lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)

'''
#Määritteilaan funktio painoindeksin laskentaan

def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus(m)

        Return:
        float: painoindeksin desimillien tarkkudella
    """
   
    pituus = pituus / 100 #muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi


#Määritellään funktio aikuisen kehonrasvaprosentin laskimiseen
def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laske lapsen kehon rasvaprosentti

    Args:
        bmi (float): paino indeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 - > mies, 0 -> nainen

        Return:
        float: kehon rasvaprosentti (aikuinen)


    """
    rasvaprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti,1)
    return rasvaprosentti

def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laske lapsen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä
        sukupuoli (float): poika -> 1, tyttö-> 0
        
        Return:
        float: rasvaprosentti (lapsi)

    """
    rasvaprosentti = 1.51 * bmi + 0.7 * ika - 3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti, 1)

    return rasvaprosentti

# Usa:n rasvaprosentti kaava

def usarasvaprosenttimies(pituus, vyotaron_ymparys, kaulan_ymparys):
    """Laske miehen rasvaprosentti usa:n kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyötärön_ympärysmitta (cm)
        kaulan_ymparys (float): kaulan_ympärysmitta (cm)
        
    Returns:
        float: rasvaprosentti
        """
    #Muutetaan mitat tuumiksi
    tuuma_pituus = pituus / 2.54
    tuuma_vyotaro_ymparys = vyotaron_ymparys / 2.54
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.54


    #Lasketaan rasvaprosentti

    usarprosentti = 86.01*math.log10(tuuma_vyotaro_ymparys-tuuma_kaulan_ymparys)-70.041*math.log10(tuuma_pituus)+36.76
    
    
    return usarprosentti

def usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
    """Laske nasten rasvaprosentti usa:n kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyötärön_ympärysmitta (cm)
        kaulan_ymparys (float): kaulan_ympärysmitta (cm)
        lantion_ymparys (float): lantion_ympärysmitta (cm)
        
    Returns:
        float: rasvaprosentti
        """
    
    #Muutetaan mitat tuumiksi
    tuuma_pituus = pituus / 2.5
    tuuma_vyotaro_ymparys = vyotaron_ymparys / 2.54
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.54
    tuuma_lantion_ymparys = lantion_ymparys / 2.54


    #Laskentaan rasvaprosentti

    usa_rasvaprosentti = 163.205*math.log10(tuuma_vyotaro_ymparys+tuuma_lantion_ymparys-tuuma_kaulan_ymparys)-97.684*math.log10(
        tuuma_pituus)-78.387
    
    
    return usa_rasvaprosentti




#Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
#Mahdollistaa funktioiden lataamisen toisiin ohjelmiin
#Kunn koodi ladataan toiseen tiedostoon, if__name == "__main__" :n alapuolella olevaakodia ei suoritetaan

if __name__ == "__main__":

    #Muuttujat

    #Kysytään käyttäjalta tiedot
    pituus_teksti = input('Kuika pitkä olet (cm): ')
    paino_teksti = input('Kuinka paljon painat(kg): ')
    ikä_teksti = input('Kuinka vanha olet: ')
    sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen, vastaa 0: ')    
    vyotaron_ymparys_teksti = input('Mikä on vyötaron ympärykseksi (cm): ')
    kaulan_ymparys_teksti = input('Mikä on kaulasi ympärysmitta? (cm) : ')

    #Jos vastaus Sukupuolikysymyksen on nainen kysy lantion ympärysmittauksen
    if sukupuoli_teksti == "0" :
        lantion_ymparys_teksti = input("Mika on sinun lantion ympärysmitta? (cm):")
    
    #Muuttujan vastauksen liukuluvuksi
    pituus = float(pituus_teksti)  #Muutetaan liukuluvuksi
    paino = float(paino_teksti)  
    ika = float (ikä_teksti)
    sukupuoli = float(sukupuoli_teksti)
    vyotaron_ymparys = float(vyotaron_ymparys_teksti)
    kaulan_ymparys = float(kaulan_ymparys_teksti)
    lantion_ymparys = float(lantion_ymparys_teksti)



    #Lasketaaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi(paino, pituus)

    #Yli 18 vuotiailla käytetään aikuisen kaavaa

    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

        #Muussa tapauksessa kaytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    print ('Painoindeksisi on', oma_bmi,
    'ja kehon rasvaprosenttti on',oma_rasvaprosentti)

    
    #Jos mies laske miehen kaavalla, muussatapauksessa naisten kaavalla

    if sukupuoli == "1":
        
        usa_rasvaprosentti = usarasvaprosenttimies(pituus, vyotaron_ymparys, kaulan_ymparys)
    
    else:

        usa_rasvaprosentti = usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys)
    print("Usa:n armeijan kaavan mukaan rasvaprosenttisi ", usa_rasvaprosentti)  