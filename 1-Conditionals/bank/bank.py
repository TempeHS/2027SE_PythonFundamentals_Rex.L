def main():
      userGreeting = input("Input a greeting: ").lower()
      parseUserGreeting(userGreeting)

def parseUserGreeting(greeting):
      if greeting.startswith("hello"):
            print("$0")
      elif greeting.startswith("h") and greeting != "hello":
            print("$20")
      else:
            print("$100")
            
main()