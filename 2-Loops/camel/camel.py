def main():
      user_variable = input("Enter a variable name: ")
      parseUserVariable(user_variable)
      
      
def parseUserVariable(variable):
      for _ in variable:
            print(_)
                 
main()