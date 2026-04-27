def main():
    while True:
        user_input = input("How much fuel is left? ")
        try:
            percentage = convert(user_input)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input, try again.")

    print(gauge(percentage))


def convert(fraction):
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError("Invalid format")

    numerator = int(parts[0])  
    denominator = int(parts[1])

    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if numerator > denominator:
        raise ValueError("Numerator cannot exceed denominator")

    return round(numerator / denominator * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()