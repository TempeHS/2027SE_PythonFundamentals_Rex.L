from bank import parse_user_greeting

def test_greeting_hello():
      assert parse_user_greeting("hello, random text") == 0


def test_greeting_hnothello():
      assert parse_user_greeting("hi, random text") == 20
      
      
def test_greeting_other():
      assert parse_user_greeting("good morning, random text") == 100