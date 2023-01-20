#Sovellus Painoindeksin ja kehon rasvaprosentin laskemiseen
#==========================================================

#Muuttujat

#Kysytään käyttäjalta tiedot
pituus_teksti = input('Kuika pitkä olet (cm): ')
paino_teksti = input('Kuinka paljon painat(kg): ')
ikä_teksti = input('Kuinka vanha olet: ')
sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen, vastaa 0: ')

#Muuttujan vastauksen liukuluvuksi
pituus = float(pituus_teksti)  #Muutetaan liukuluvuksi
paino = float(paino_teksti)  
ika = float (ikä_teksti)
sukupuoli = float(sukupuoli_teksti)

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



def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laske lapsen kehon rasvaprosentti

    Args:
        bmi (float): paino indeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 - > mies, 0 -> nainen

        Return:
        float: kehon rasvaprosentti (aikuinen)


    """
    rasvaprosentti = 1.2 + bmi + 0.23 * ika - 10.8 + sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti)
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
    return rasvaprosentti
        
oma_bmi = laske_bmi(paino, pituus,)
oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

print ('Painoindeksisi on', oma_bmi, 'ja kehon rasvaprosenttti on',oma_rasvaprosentti)