#"qiestion.py test can be found here"
#------------------------------------

import questions

# Test if confersion to integer work as expected

user_input = "100"

def test_ask_user_intger(monkeypatch):
    user_input = "100"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Anna kokonaisluku")
    assert question.ask_user_integer(False) == ( 100, "OK", 0, "Conversion successful")

# Test an error cindition when user adds aunit to a number
def test_ask_user_intger2(monkeypatch):
    user_input = "100"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Anna kokonaisluku")
    assert question.ask_user_integer(False) == ( 0, "OK", "Error", 1, "invalid literal for base 10: 100v")
    
# Test if conversation to float work to espected

# Test  en error condition when user adds a unit to a floating poin number


# Test conversion to boolian



# Test an error condition

# Change methods to static or class methods and test again

