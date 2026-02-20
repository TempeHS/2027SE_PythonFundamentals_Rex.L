def main():
      user_plate = input("Plate: ")
      if is_valid(user_plate):
            print("Valid")
      else:
            print("Invalid")
      
      
def is_valid(plate):
      if length_check(plate) and no_punctuation(plate) and starting_letters(plate) and numbers_in_middle(plate):
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
            if plate[i].isnumeric():
                  
                  _, middle, right = plate.partition(plate[i])
                  
                  if middle == "0":
                        print("First number cannot be 0")
                        return False
                  elif right.isnumeric() == False and right != "":
                        print("Number plate has a number before a letter")
                  else:
                        return True
                  
            else: 
                  print("No Numbers in Middle: True")
                  return True
            
            
def starting_letters(plate):
      letter_count = 0
      
      for i in range(2):
            if plate[i].isalpha():
                  letter_count += 1
            else:
                  print("Plate must start with two letters")
                  return False
            
            if letter_count >= 2:
                  return True
                        


      
      
main()