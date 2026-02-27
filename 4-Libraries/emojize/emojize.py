import emoji

def main():
      user_input = input("Enter a string: ")
      print(f"Output: {emoji.emojize(user_input, language="alias")}")
      
main()