num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
   case "+":
      result = num1 + num2 
      print("Result: ", result)
   case "-":
      result = num1 - num2
      print("Result", result)
   case "*":
      result = num1 * num2 
      print("Result", result)
   case "/":
      if num2 != 0:
        result = num1 / num2 
        print("Result", result)
      