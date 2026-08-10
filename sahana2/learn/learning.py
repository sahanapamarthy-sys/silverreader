import numpy as np  

E = ['one', 'two', 'three', 'four']
S = ['uno', 'dos', 'tres', 'cuatro']

EtoS = dict()

for e,s in zip(E,S): 
    EtoS[e] = s
print(EtoS)


name = "sahana pamarthy"
lst = name.split( )
birth_year = 2006
death_year = 200003 

radius = 3.2
area = np.pi * radius**2

print('The area of the circle is ' + str(area))

print(f'{" Final tally ":=^30}')
print(f'{"EGU:":<15}{"7_303_480":>15}')
print(f'{"NMM:":<15}{"3_316_142":>15}')
print(f'{" ":-<30}')
print(f'{"Total:":>15}{"10_619_622":>15}')
