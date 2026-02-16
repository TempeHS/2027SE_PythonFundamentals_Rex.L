def main():
      user_input = int(input("Insert a coin: "))
      coke_cost = 50
      amount_payed = 0
      
      while amount_payed < coke_cost:
            amount_payed += user_input
            
            if amount_payed >= coke_cost:
                  break
            elif user_input != 25 or 10 or 5:
                  print("Not accepted, try again")
                  user_input = int(input("Insert a coin: "))
            else:
                  amount_payed += user_input
            
            
            
            
main()