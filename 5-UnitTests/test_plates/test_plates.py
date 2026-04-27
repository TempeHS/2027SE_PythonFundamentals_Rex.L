from plates import is_valid


def test_plate_length():
      assert is_valid("B2MLPPOAM") == False
      assert is_valid("WAMBF5") == True 
      assert is_valid("M") == False
      
      
def test_no_punctuation():
      assert is_valid("MWAVN") == True
      assert is_valid("M.Y3/J") == False
      assert is_valid("..T74") == False
      
      
def test_numbers_in_middle():
      assert is_valid("MWAVN") == True
      assert is_valid("0MYU") == False
      assert is_valid("451TU") == False
      
      
def test_start_letters():
      assert is_valid("AMZ") == True
      assert is_valid("A2MJL") == False
      
      