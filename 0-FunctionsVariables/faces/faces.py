def main():
      userInput = input("Enter a string with emoticons: ")
      print(convert(userInput))
      
      
def convert(userInput):
      parsedString = userInput.replace(":)", "🙂") 
      parsedString = parsedString.replace(":(", "🙁")

      return parsedString


main()
      