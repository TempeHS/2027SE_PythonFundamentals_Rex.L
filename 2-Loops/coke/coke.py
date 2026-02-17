coke_cost = 50
amount_due = 0
user_input = ""

def main():
      getUserInput()
      
      while amount_payed < coke_cost:
            if amount_payed >= coke_cost:
                  break
            elif user_input != 25 and user_input != 10 and user_input != 5:
                  print("Coin not supported, please try again: ")
                  getUserInput()
            else:
                  amount_payed = amount_payed + user_input
                  amount_due = coke_cost - amount_payed
                  print(amount_due)
      
      
def getUserInput():
      user_input = input("Insert a coin: ")
      amount_payed = amount_payed + user_input
      return amount_payed
      
      
main()