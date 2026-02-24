menu = {
	"Baja Taco": 4.25,
	"Burrito": 7.50,
	"Bowl": 8.50,
	"Nachos": 11.00,
	"Quesadilla": 8.50,
	"Super Burrito": 8.50,
	"Super Quesadilla": 9.50,
	"Taco": 3.00,
	"Tortilla Salad": 8.00
}



def main():
      total_cost = 0
      
      while True:
            try: 
                  user_input = input("Place an order: ").title()
            except KeyboardInterrupt:
                  print("")
                  return

            try:
                  total_cost += menu[user_input]
                  print(f"{user_input} - Total Cost: ${total_cost:.2f}")
                  continue
            except KeyError:
                  print("Item not found, please try again.")
                  continue
            


main()