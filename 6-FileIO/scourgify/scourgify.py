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
            else:
                  raise ValueError
      except IndexError:
            sys.exit("Too few/many command-line arguments")
      except ValueError:
            sys.exit("Invalid file type")

            
      read_file(old_user_file, new_user_file)


def read_file(old, new):
      try:
            with open(old, "r", newline="") as csvfile:
                  reader = csv.DictReader(csvfile)
                  
                  with open(new, "w", newline="") as final_file:
                        layout = ["first_name", "last_name", "house"]
                        writer = csv.DictWriter(final_file, fieldnames=layout)  
                        writer.writeheader()
                  
                        for row in reader:
                              last_name, first_name = row["name"].split(",")
                              writer.writerow(
                                    {"first_name": first_name.strip(), 
                                    "last_name": last_name.strip(), 
                                    "house": row["house"].strip()
                                    })
      except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
            
      
main()