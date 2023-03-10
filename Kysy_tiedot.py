#OHJELMA, JOKA KYSYY BMI TIETOJA USEASTA KUNTOILIJASTA
#=====================================================

#KIRJASTOT JA MODUULIT
#---------------------

#Tuodaan fitnes.py:n sisältämät toiminnot tähän ohjelmaan
import fitness

#Kysytään tiediot ja tulostetaan painoindeksi kunnes halutaan lopettaa
bmi_lista = []
nimilista = []
while True: # Ikuinen silmukka jossa ollaan kunnes annetaan tyhjä pituus
        
        nimi = input("Nimi, tyhjä lopettaa: ")
        
        if nimi == " ":
            break
        
        nimilista.append(nimi)
        pituus_teksti = input("Pituus (cm):  ")
        paino_teksti = input("Paino (kg): ")

        #Yritetään muuttaa syötetyt tekstin luvuiksi
        try:
            pituus = float(pituus_teksti)
            paino = float(paino_teksti)

            #Lasketaan painoindeksi fitnes-modulin laske bmi-funktiolla
            bmi = fitness.laske_bmi(paino, pituus)

            #Luodaan monikko (tuple), jossa nimi ja bmi
            monikko = (nimi, bmi)

            #Lisätään monikko listaan
            bmi_lista.append(monikko)

            # Näytetään tulokset ruudulla
            print("Painoindeksi on", bmi )
            
        #Jos tapahtuu virhe, ilmoitetaan käyttäjälle    
        except Exception as e:
            print("Syötteessä oli virhe, yritä uudelleen", e)

#Tulosta ruudulle lopuksi lista painoindekseistä
print("Nimet ja painoindeksit olivat: ", bmi_lista)  

#Puretaan lista ja tulostetaa se rivi-riviltä -> monikko / rivi
for henkilo in bmi_lista:

    #Monikossa on kaksi tietoa, joiden indeksit ovat 0 (ensimmäinen) ja 1 toinen
    print(henkilo[0], "painoindeksi on", henkilo[1])


#Listassa olivien monikoiden määrä
print("Listassa oli", len(bmi_lista), "merkintää")

#Harjoitus: Tee bmi-listaan perusteella kuntoilijoiden aakostettu nimilista
nimilista.sort() # Aakostetaan nimilista
print(nimilista) # Tulostetaan se
