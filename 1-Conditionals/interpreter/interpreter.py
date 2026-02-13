userExpression = input("Enter an arithmetic expression: ")

x, y, z = userExpression.split(" ")



if y == "+":
      answer = float(x) + float(z)
elif y == "-":
      answer = float(x) - float(z)
elif y == "*":
      answer = float(x) * float(z)
elif y == "/":
      answer = float(x) / float(z)
      
print(answer)
      