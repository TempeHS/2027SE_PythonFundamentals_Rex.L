def main():
      user_variable = input("Enter a variable name: ")
      parseUserVariable(user_variable)
      
      
def parseUserVariable(variable):
      for i in variable:
            if i.isupper():
                  print("_" + i.lower(), end="")
            else:
                  print(i, end="")
                  
                  
main()