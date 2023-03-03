# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------

# LIBRARIES AND MODULES
import kuntoilija



# Ask a question and convert the answer to float
def ask_user(question):
    """Ask a question from the user and converts answer to a floading point number

    Args:
        question (str): The question to ask

    Returns:
        tuple: answer as float, Error message, Error code and a detailed error message
    """
    # Loop until user gives a correctly formatted value  
    while True:
        answer_txt = input(question)


    # Let try convert input to numeric
        try:
            answer = float(answer_txt)
            result = (answer, "OK", 0, "Conversion successful")
            break

        # If en error occurs tell the user to check   
        except Exception as e:
            print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)        
            result = (0, "Error", 0, str(e))
    return result


# Enter information about an athlete
nimi = input("Nimi: ")

# Use ask user function to get heigt and convert it in float
answer = ask_user("Pituus (cm) ")

# Read the list element of the tuple conteining height value
pituus = answer[0]


answer = ask_user("Paino (kg) ")
paino = answer[0]

answer = ask_user("Ikä  ")
ika = answer[0]

answer = ask_user("sukupuoli, jos mies 1, jos nainen 0  ")
sukupuoli = answer[0]


"""
# Loop until correct weight value
while True:
    paino_txt = input("Paino (kg): ")


# Let try convert input to numeric
    try:
        paino = float(paino_txt)
        break

# If en error occurs tell the user to check   
    except Exception as e:
        print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)

# Loop until correct age value
while True:
    ika_txt = input("Ika: ")


# Let try convert input to numeric
    try:
        ika = float(ika_txt)
        break

# If en error occurs tell the user to check   
    except Exception as e:
        print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)  


# Loop until correct gender value
while True:
    sukupuoli_txt = input("Sukupuoli, 1 mies, 0 nainen: ")


# Let try convert input to numeric
    try:
        sukupuoli = float(sukupuoli_txt)
        break

# If en error occurs tell the user to check   
    except Exception as e:
        print("Virhe syötetyssä arvossa, vain 1 ja 0 sallittu", e)
        """

kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
print(kuntoilija1.nimi, "painoindeksisi on", kuntoilija1.bmi)
print("Viimeisen kysymyksen virheilmoitus", answer[1], "koodi", answer[2], "engl.ilmoitus", answer[3])

