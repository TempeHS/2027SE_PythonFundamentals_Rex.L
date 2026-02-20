def main():
      user_plate = input("Plate: ")
      if is_valid(user_plate):
            print("Valid")
      else:
            print("Invalid")
      
      
def is_valid(plate):
      if length_check(plate) and no_punctuation(plate):
            return True
      else:
            return False
     
     
def length_check(plate):
      if len(plate) > 6:
            print("Too long, please try again. ") 
            print("Length Within Limits: False")
            return False
      elif len(plate) < 2:
            print("Too short, please try again. ")
            print("Length Within Limits: False")
            return False
      else:
            print("Length Within Limits: True")
            return True
      

def no_punctuation(plate):
      if plate.isalnum():
            print("No Punctuation: True")
            return True
      else:
            print("No Punctuation: False")
            return False
      

def numbers_in_middle(plate):
      for i in range(len(plate)):
            


      
      
main()