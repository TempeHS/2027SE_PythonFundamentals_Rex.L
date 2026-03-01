import random as r

def main():
      while True:
            try:
                  user_input = int(input("Enter a level: "))
                  if user_input < 0:
                        raise ValueError
                  break
            except ValueError:
                  continue
            
      random_number = r.randrange(1, user_input)
      
      while True:
            try:
                  user_guess = int(input("Guess the number: "))
                  if user_guess < 0:
                        raise ValueError
            except ValueError:
                  continue
            
            if user_guess > random_number:
                  print("Too large!")
                  continue
            elif user_guess < random_number:
                  print("Too small!")
                  continue
            else:
                  print("Just Right!")
                  break
            
main()