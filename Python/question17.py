import random
numbers = []
for i in range(8):
  numbers.append(random.randint(1,100))
max = numbers[0]
for j in numbers:
  if j > max:
    max = j
min = numbers[0]
for k in numbers:
  if k < min:
    min = k
print(" the biggest number is:",max)
print(" the smallest number is: " , min)

  
