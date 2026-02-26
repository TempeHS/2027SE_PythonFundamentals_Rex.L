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
                  if int(month) > 12 or int(month) < 1:
                        continue
                  print(f"{int(year)}-{int(month):02}-{int(day):02}")
                  break
            except ValueError:
                  try:
                        day_month, year = user_input.split(",")
                        month, _, day = day_month.partition(" ")
                        month = month.title()
                        try:
                              if month in months:
                                    month_num = months.index(month) + 1
                                    
                                    print(f"{int(year)}-{int(month_num):02}-{int(day):02}")
                                    break
                              else:
                                    continue
                        except ValueError:
                              continue
                        
                  except ValueError:
                        print("Invalid input, try again.")
                        continue
            
main()