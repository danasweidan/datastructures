cars=[]

def push(car):
    cars.append(car)

def pop():
    cars.pop()
    return

def isEmpty():
    if len(cars)==0:
        print("stack is empty")
        return True
    else:
        ("stack is not empty")
        return False

def isFull():
    if len(cars)==6:
        print("stack is full")
        return True
    else: 
        print("stack is not full")
        return False

push("Mondeo")
print(cars)

push("Golf")
print(cars)

isEmpty()
print(cars)

push("Fiesta")
print(cars)

push("Punto")
print(cars)

pop()
print(cars)

push("Civic")
print(cars)

push("Porche")
print(cars)

isFull()
print(cars)

pop()
print(cars)

pop()
print(cars)