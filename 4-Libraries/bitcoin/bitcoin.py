import requests as req
import sys

r = req.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r.json()

def main():
      try:
            bitcoin = float(sys.argv[1])
            print(bitcoin)
      except ValueError, IndexError:
            sys.exit("Error, invalid input")
            
      print(r)
            
main()
            