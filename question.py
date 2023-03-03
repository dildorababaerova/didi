# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING TO VARIOUS DATA TYPES
#------------------------------------------------------------------------------

#LIBRARIES AND MODULES

# CLASS DEFINITIONS

class Question():
    """A class containing methods to ask quistions on console
     and converting answers to various datetypes
     """
    
    
    def __init__(self, question):
        self.question = question
        

    def ask_user_integer(self, loop):
        """Ask a question and converts the answer to an integer

        Args:
            loop (bool): If True asks tht question until able to convert it 

        Returns:
            tuple: answer as integer, error message, erroor code, detailed error
        """

        # If loop argument is true use while loop until user inputs correct value
        if loop == True:
            
            while True:
                answer_txt = input(self.question)
                
                # Let try convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, "OK", 0, "Conversion successful")
                    break

                # If en error occurs tell the user to check   
                except Exception as e:
                    print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)        
                    result = (0, "Error", 0, str(e))

        # Else ask once and return zero value and error information    
        else:
                
            # Let try convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, "OK", 0, "Conversion successful")
                    
                # If en error occurs tell the user to check   
                except Exception as e:
                    print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)        
                    result = (0, "Error", 0, str(e))
        return result
    
    def ask_user_integer(self, true_value, false_value, loop):
        """_summary_

        Args:
            true_value (str): value to use as True
            false_value (str): value to use as False
            loop (bool): If True asks the question until able to convert it
        Returns:
        tuple: answer as integer, error message, erroor code, detailed error    
        """
    # If loop argument is true use while loop until user inputs correct value
        if loop == True:
            
            while True:
                answer_txt = input(self.question)
                
                # Let try convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, "OK", 0, "Conversion successful")
                    break

                # If en error occurs tell the user to check   
                except Exception as e:
                    print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)        
                    result = (0, "Error", 0, str(e))

        # Else ask once and return zero value and error information    
        else:
                
            # Let try convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, "OK", 0, "Conversion successful")
                    
                # If en error occurs tell the user to check   
                except Exception as e:
                    print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)        
                    result = (0, "Error", 0, str(e))
        return result
        
    
    
    
    
if __name__ == "__main__":

    question = Question("Kuinka vanha olet? ")
    answer_and_error = question.ask_user_integer(False)
    print(answer_and_error)
        

        

        

    