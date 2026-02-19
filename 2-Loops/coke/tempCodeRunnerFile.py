      while amount_payed < coke_cost:
            if amount_payed >= coke_cost:
                  break
            elif coin_input == 25 or coin_input == 10 or coin_input == 5:
                  amount_payed += coin_input
                  amount_due = coke_cost - amount_payed
                  print("Amount due: " + amount_due)
                  coin_input = int(input("Enter another coin: "))
            else:
                  print("Coin not accepted, please try again. ")
                  coin_input = int(input("Enter a coin: "))


      change_owed = amount_payed - coke_cost
      print("Change dispensed: " + change_owed)