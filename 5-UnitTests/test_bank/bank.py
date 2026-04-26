def main():
      userGreeting = input("Input a greeting: ").lower()
      return_amount = parse_user_greeting(userGreeting)
      print(f"${return_amount}")


def parse_user_greeting(greeting):
      if greeting.startswith("hello"):
            return 0
      elif greeting.startswith("h") and greeting != "hello":
            return 20
      else:
            return 100
          
if __name__ == "__main__" :
      main()