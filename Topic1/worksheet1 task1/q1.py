#array numbers [6]
numbers=["","","","","",""]

#input numbers
for i in range(0,6):
    numbers[i]=int(input("Enter a number:"))

for i in range(0,6):
  print(numbers[5-i])

for i in range(0,6):
   total=0
   total=total + numbers[i]
print("total=" + str(total))

average= total/6
print("average=" + str(average))
 

