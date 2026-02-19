def main():
      coke_cost = 50
      amount_payed = 0
      amount_due = coke_cost
      change_owed = 0
      
      
      while amount_payed < coke_cost:
            coin_input = int(input("Enter a coin: "))
            
            if coin_input == 25 or coin_input == 10 or coin_input == 5:
                  amount_payed += coin_input
                  amount_due = coke_cost - amount_payed
                  if amount_due > 0:
                        print("Amount due: " + str(amount_due))
            else:
                  print("Coin not accepted, please try again. ")
                  print("Amount due: " + str(amount_due)) 
                  coin_input = int(input("Enter a coin: "))


      change_owed = amount_payed - coke_cost
      print("Change dispensed: " + str(change_owed))
            
main()