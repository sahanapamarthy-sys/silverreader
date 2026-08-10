import math

def say_goodbye(name): 
    print("Goodbye" , name)

def area(radius):
    area = math.pi * (radius**2)
    print(area)

def subtract(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def clothes(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    return (min_temp, max_temp)

def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False 

def field_trip(distance,fuel):
    fuel_efficency = distance / fuel 
    return fuel_efficency

def secret_code(data):
    data_str = str(data)
    rejig = int(data_str[-1] + data_str[:len(data_str)-1])
    return rejig

def oski_power(x,y):
    power = 1 
    for i in range(y): 
        power = power * x
    return power    

def min_for(num_list):
    minimum = num_list[0]
    for num in num_list: 
        if num < minimum:
            minimum = num
    return minimum

def max_for(num_list):
    maximum = num_list[0]
    for num in num_list:
        if num > maximum: 
            maximum = num 
    return maximum 

def min_while(num_list):
    minimum = num_list[0]
    i = 0
    while i < len(num_list):
        i+=1 
    return minimum 

def max_while(num_list):
    maximum = num_list[0]
    i = 0
    while i < len(num_list):
        i+=1
    return maximum 

def calculate_sum(num):
    num_str = str(num)
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i])
    return sum 

def oski_power(x,y):
    power = 1 
    for i in range(y): 
        power = power * x
    return power


x = 2
y = 3
result = oski_power(x, y) 
print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")
