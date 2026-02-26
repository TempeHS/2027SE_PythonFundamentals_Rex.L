months = [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December"
	]

def main():
      while True:
            try:
                  user_input = input("Enter a date: ")
                  month, day, year = user_input.split("/")
                  print(f"{int(year)}-{int(month):02}-{int(day):02}")
                  break
            except ValueError:
                  try:
                        day_month, year = user_input.split(",")
                        day, _, month = day_month.partition(" ")

                        try:
                              month in months
                        
                  except ValueError:
                        print("Invalid input, try again.")
                        continue
            
main()