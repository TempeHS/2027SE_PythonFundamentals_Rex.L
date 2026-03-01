import inflect

p = inflect.engine()
inputs = []

def main():
      while True:
            try:
                  user_input = input("Enter a name: ")
                  inputs.append(user_input)
                  continue
            except KeyboardInterrupt:
                  break
      
      print(inputs)
      print_output()
      
      
def print_output():
      parsed_output = p.join(inputs)
      print(f"Adieu, adieu, to {parsed_output}")
      
main()