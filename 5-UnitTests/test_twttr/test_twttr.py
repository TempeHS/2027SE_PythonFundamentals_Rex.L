from twttr import shorten

def test_remove_vowel():
      assert shorten("hello") == "hll"


def test_uppercase_vowel():
      assert shorten("HELLO") == "HLL"
      
      
def test_no_vowels():
      assert shorten("MHLTvrK") == "MHLTvrK"
      
      
def test_all_vowels():
      assert shorten("AeIoU") == ""      


