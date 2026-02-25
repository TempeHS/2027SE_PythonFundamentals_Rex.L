grocery_list = {}

def main():
      
      
      while True:
            try:
                  user_input = input("Enter an item: \n").upper()
                  if user_input not in grocery_list:
                        grocery_list[user_input] = 1
                  else:
                        grocery_list[user_input] += 1
            except KeyboardInterrupt:
                  sorted_list = dict(sorted(grocery_list.items()))
                  
                  for item, amount in sorted_list.items():
                        if amount > 1:
                              print(f"{amount}x{item}", end="\n")
                        else:
                              print(item, end="\n")
                              
                  return
      
main()