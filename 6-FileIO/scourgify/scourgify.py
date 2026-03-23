import sys
import csv

def main():
      try:
            old_user_file = sys.argv[1]
            new_user_file = sys.argv[2]
            
            if len(sys.argv) != 3:
                  raise IndexError
            elif old_user_file.endswith(".csv") and new_user_file.endswith(".csv"):
                  pass
                  print(len(sys.argv))
            else:
                  raise ValueError
      except IndexError:
            sys.exit("Too few/many command-line arguments")
      except ValueError:
            sys.exit("Invalid file type")
            
      read_file(old_user_file, new_user_file)

def read_file(old, new):
      with open(old, "w", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                  print(row)            

                  
main()