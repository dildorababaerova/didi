#"qiestion.py test can be found here"
#------------------------------------

import questions

# Test if confersion to integer work as expected

user_input = "100"

def test_ask_user_intger(monkeypatch):
    user_input = "100"
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    question = questions.Question("Answer")
    assert question.ask_user_integer(False) == ( 100, "OK", 0, "Conversion successful")
    