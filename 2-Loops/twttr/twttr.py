def main():
      user_input = input("Enter a string of text: ")
      parseUserText(user_input)
      
      
def parseUserText(text):
      omitted_letters = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
      for i in text:
            if i in omitted_letters:
                  print("", end="")
            else:
                  print(i, end="")
      
      
    
main()