from datetime import date
import sys


class Date:

    def __init__(self, dob):
            self.dob = dob

    @classmethod
    def get(cls):
            user_input = input("Date of Birth: ")
            try:
                  dob = date.fromisoformat(user_input)
                  return cls(dob)
            except ValueError:
                  sys.exit("Invalid date")

    def minutes_since(self):
            delta = date.today() - self.dob
            return delta.days * 24 * 60


class MinutesToWords:

      ONES = ["", "one", "two", "three", "four", "five", "six", "seven",
                  "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                  "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
      TENS = ["", "", "twenty", "thirty", "forty", "fifty",
                  "sixty", "seventy", "eighty", "ninety"]

      def __init__(self, minutes):
            self.minutes = minutes

      def convert(self):
            if self.minutes == 0:
                  return "zero minutes"

            billions  = self.minutes // 1_000_000_000
            millions  = (self.minutes % 1_000_000_000) // 1_000_000
            thousands = (self.minutes % 1_000_000) // 1_000
            remainder = self.minutes % 1_000

            parts = []
            if billions:
                  parts.append(f"{self._group(billions)} billion")
            if millions:
                  parts.append(f"{self._group(millions)} million")
            if thousands:
                  parts.append(f"{self._group(thousands)} thousand")
            if remainder:
                  parts.append(self._group(remainder))

            return " ".join(parts) + " minutes"

      def _group(self, n):
            if n == 0:
                  return ""
            elif n < 20:
                  return self.ONES[n]
            elif n < 100:
                  rest = "" if n % 10 == 0 else " " + self.ONES[n % 10]
                  return self.TENS[n // 10] + rest
            else:
                  hundreds = self.ONES[n // 100] + " hundred"
                  rest = self._group(n % 100)
                  return hundreds + (" " + rest if rest else "")


def main():
      dob = Date.get()
      minutes = dob.minutes_since()
      print(MinutesToWords(minutes).convert())


if __name__ == "__main__":
      main()