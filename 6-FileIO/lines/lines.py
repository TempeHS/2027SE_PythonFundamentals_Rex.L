import sys 

def main():
      line_count = 0
      
      try:
            file_name = sys.argv[1]
            
            if len(sys.argv) > 2:
                  print(len(sys.argv))
                  raise IndexError
            elif file_name.endswith(".py"): 
                  pass
            else:
                  raise ValueError
            
      except IndexError:
            sys.exit("Too few/many command-line arguments")
      
      except ValueError:
            sys.exit("Not a python file")
      
      try:   
            with open(file_name, "r") as file:
                  for line in file:
                        if line.startswith("#") or not line.strip():
                              continue
                        else:
                              line_count += 1
      except FileNotFoundError:
            sys.exit("File does not exist")
                  
      print(f"Number of lines: {line_count}")
      
main()