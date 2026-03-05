import sys 

def main():
      try:
            file_name = sys.argv[1]
            
            if file_name.endswith(".py"):
                  pass
            else:
                  raise FileNotFoundError
      except FileNotFoundError, IndexError:
            sys.exit("Error: File not found")
            
      with open(file_name, "r") as file:
            lines = file.readlines()
      
      print(len(lines))
      
main()