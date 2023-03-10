# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------
# LIBRARIES AND MODULES
import kuntoilija
import questions
# Ask a question and convert the answer to float
# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him
question = questions.Question('Kuinka paljon painat (kg): ')
weight = question.ask_user_float(True)[0]
question = questions.Question('Kuinka pitkä olet (cm): ')
height = question.ask_user_float(True)[0]
question = questions.Question('Kuinka vanha olet: ')
age = question.ask_user_integer(True)[0]
question = questions.Question('Sukupuoli 1 mies, 0 nainen: ')
gender = question.ask_user_integer(True)[0]
question = questions.Question('Mikä on kaulanympäryksesi (cm): ')
neck = question.ask_user_float(True)[0]
question = questions.Question('Mikä on vyötärönympäryksesi: ')
waist = question.ask_user_float(True)[0]
if gender == 0:
    question = questions.Question('Mikä on lantionympäryksesi: ')
    hips = question.ask_user_float(True)[0]

# Create an athelete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)
# Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(
        height, waist, hips, neck)
text_to_show = f'suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}'
print(text_to_show)