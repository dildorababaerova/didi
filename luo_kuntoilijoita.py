# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------

# LIBRARIES AND MODULES
import kuntoilija
import question



# Ask a question and convert the answer to float


# Enter information about an athlete
name = input("Nimi: ")

#Ask details about her/him
question1 = question.Question("Kuinka paljon painat(kg): ")
weight =question1.ask_user_float(True)[0]
question2 = question.Question("Kuinka pitkä olet(cm): ")
height = question2.ask_user_float(True)[0]
question3 = question.Question("Kuinka vanha olet: ")
age = question3.ask_user_integer(True)[0]
question4 = question.Question("Sukupuoli 1 mies, 0 nainen: ")
gender = question4.ask_user_integer(True)[0]
question5 =question.Question("Mikä on kaulanympäryksesi (cm): ")
neck = question5.ask_user_float(True)[0]
question6 = question.Question("Mikä on vyötärönympäryksesi (cm): ")
waist = question6.ask_user_float(True)[0]
if gender == 0:
    question7 = question.Question("Mikä on lantionnympäryksesi (cm): ")
    hips = question7.ask_user_float(True)[0]

# Create an athlete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija (name, height, weight, age, gender)

# Print some information about the athlete
text_to_show = f"Terve {athlete.nimi}, paioindeksi tänään on {athlete.bmi}"
print(text_to_show)

fat_persentage = athlete.rasvaprosentti()
if gender == 1:
    usa_fat_persentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_persentage = athlete.usa_rasvaprosentti_nainen(height, waist, hips, neck)

text_to_show = f"suomalainen rasva-% on {fat_persentage} ja amerikkalainen on {usa_fat_persentage}"
print(text_to_show)

 
