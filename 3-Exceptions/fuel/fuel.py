def main():
      empty = "E"
      full = "F"
      
      
      while True:
            user_input = input("How much fuel is left? ")
            
            try:
                  parsed_fuel = user_input.split("/")
                  numer = float(parsed_fuel[0])
                  denom = float(parsed_fuel[1])
                  percent_fuel = numer / denom * 100
                  
                  if numer > denom:
                        raise ValueError("Invalid input, try again.")
                  break
            except (ValueError, ZeroDivisionError):
                  print("Invalid input, try again.")
            
                  
      if percent_fuel <= 1:
            print(empty)
      elif percent_fuel >= 99:
            print(full)
      else:
            print(f"{percent_fuel}%") 
      
      
main()