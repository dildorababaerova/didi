#"qiestion.py test can be found here"
#------------------------------------

import questions

# Test if confersion to integer work as expected



# def test_ask_user_integer(monkeypatch):
#     user_input = "100"
#     monkeypatch.setattr("builtins.input", lambda _: user_input)
#     question = questions.Question("Anna kokonaisluku")
#     assert question.ask_user_integer(False) == ( 100, 'OK', 0, 'Conversion successful')

# # Test an error condition when user adds a unit to a number
# def test_ask_user_integer2(monkeypatch):
#     user_input = "100v"
#     monkeypatch.setattr("builtins.input", lambda _: user_input)
#     question = questions.Question("Anna kokonaisluku")
#     assert question.ask_user_integer(False) == ( 0, 'Error', 1, "invalid literal for int() with base 10: '100v'")
    
 #Test static convertion method to integer
 def Test_static_ask_user_integer(monkeypatch):
     user_input = '100'
     monkeypatch.setattr('builtins.input', lambda _:user_input)
     questions.Question.ask_user_integer( 'Anna kokonaisluku', False) == (100, 'OK', 0, 'Conversion successful')

# Test if conversation to float work to espected
def test_ask_user_float(monkeypatch):
    user_input = "1.5"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Anna kokonaisluku")
    assert question.ask_user_float(False) == ( 1.5, 'OK', 0, 'Conversion successful')

def test_ask_user_float2(monkeypatch):
    user_input = "1.5v"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Anna kokonaisluku")
    assert question.ask_user_float(False) == ( 0, 'Error', 1, "could not convert string to float: '1.5v'")


# Test an error condition when user uses comma instead of dot as desimai separator 
def test_ask_user_float3(monkeypatch): # Simulate user input using Monkeypatch library
    user_input = "74,6"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Anna kokonaisluku")
    assert question.ask_user_float(False) == ( 1.5, 'OK', 0, "Conversion successful")


# Test conversion to boolian: case Y
def test_ask_user_boolean2(monkeypatch):
    user_input = "v"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Haluatko jatkaa? ")
    assert question.ask_user_boolean('Y', 'N', False) == ('N/A', 'Error', 1, 'unable to convert to boolean')

# Test conversion to boolian: case N
def test_ask_user_boolean3(monkeypatch):
    user_input = "n"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Haluatko jatkaa? ")
    assert question.ask_user_boolean('Y', 'N', False) == ('N/A', 'Error', 1, 'unable to convert to boolean')





"""



# Test conversion to boolian



# Test an error condition

# Change methods to static or class methods and test again
"""

