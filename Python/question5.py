num1_string = input("Enter first number:")
num2_string = input("Enter second number:")
# CONVERT ABOVE NUMBERS TO INTEGERS:
num1 = int(num1_string)
num2 = int(num2_string)

#PERFORM OPERATIONS
print("sum:" , num1 + num2 )
print("difference :" , num1 - num2)
print(" product:" , num1 * num2)
if num1 > num2:
  print(" The first number is greater than the  second")
elif num2 > num1 :
  print(" The second number is greater than the first ")
else :
  print("Both the numbers are equal")
