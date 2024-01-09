#array numbers [6]
numbers=["","","","","",""]
length=len(numbers)

#input numbers
for i in range(0,length):
    numbers[i]=int(input("Enter a number:"))

for i in range(0,length):
  print(numbers[length-1-i])

for i in range(0,length):
   total=0
   total=total + numbers[i]
print("total=" + str(total))

average= total/6
print("average=" + str(average))
 

