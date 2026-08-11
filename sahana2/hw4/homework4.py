favorite_foods = ["pizza","salad","pappu","sambar","idli"]
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("mac and cheese")
favorite_foods.insert(0,"apple")
del favorite_foods[2]
print(len(favorite_foods))
for x in favorite_foods:
    print(x.upper())
new_list = list()
new_list.append(favorite_foods[::4])
for food in favorite_foods:
    if food == "potato":
        print("A potato!")
    else:
        print("No potato!")

numbers = list()
for i in range(21):
    numbers.append(i)

def get_first_15(numbers):
    return numbers[:15]

step1 = get_first_15(numbers)

def get_every_5th(numbers):
    return numbers[::5]

step2 = get_every_5th(step1)

def reverse_and_stride(numbers):
    newly_added = numbers[::1]
    third_element = newly_added[::3]
    return third_element

step3 = reverse_and_stride(step2)

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for x in row:
            total = total + x 
    return total

list_5x5 = list()
for i in range(5):
    rows = list()
    for j in range(5):
        rows.append(5*i + j +1)
    list_5x5.append(rows)

def multiples_of_three():
    for number in list_5x5:
        for index, num in enumerate(number):
            if num % 3 == 0: 
                number.remove(number[index])
                number.insert(index,"?")
    return list_5x5

new_list = multiples_of_three()

def adding_elements():
    total = 0
    for rows in new_list:
        for numbers in rows:
            if numbers != "?":
                total+=numbers
    return total 

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}            
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52

for name, age in ages.items():
    print(name, age)