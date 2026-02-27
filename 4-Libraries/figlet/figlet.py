from pyfiglet import Figlet
import sys
import random

def main():
      
      
      if len(sys.argv) > 3:
            sys.exit("Too many arguments")
      elif len(sys.argv) == 2:
            sys.exit("Argument not accepted")
      else:
            print("Argument Test Passed")
            print(sys.argv[2])
            user_input = input("Enter a string: ")
            try:
                  if sys.argv[2] not in Figlet().getFonts():
                        sys.exit("Failed font check")
                  elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
                        print(sys.argv[1])
                        sys.exit("Failed font input check")
                  else:
                        f = Figlet().setFont(font=sys.argv[2])
                        print(f.renderText(user_input))
            except IndexError:
                  sys.exit("Too many/few arguments")

      
main()