import sys
import csv
from tabulate import tabulate as t

def main():
      try:
            user_input = sys.argv[1]
            
            if len(sys.argv) > 2:
                  raise IndexError
            elif user_input.endswith(".csv"):
                  pass
            else:
                  raise ValueError
      except IndexError:
            sys.exit("Too few/many command-line arguments")
      except ValueError:
            sys.exit("Not a CSV file")
      
      
      try:
            with open(user_input, "r") as csvfile:
                  print(csvfile)
                  menu = csv.DictReader(csvfile)
                  print(t(menu, headers="keys", tablefmt="grid"))
      except FileNotFoundError:
            sys.exit("File not found")
            
      
      
main()