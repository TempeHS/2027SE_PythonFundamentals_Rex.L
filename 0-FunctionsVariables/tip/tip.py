def main():
		dollars = dollars_to_float(input("How much was the meal? "))
		percent = percent_to_float(input("What percentage would you like to tip? "))
		tip = dollars * percent
		print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
	parsedDollars = float(d.strip("$"))
	return parsedDollars

def percent_to_float(p):
	parsedPercent = float(p.strip("%")) / 100
	return parsedPercent


main()