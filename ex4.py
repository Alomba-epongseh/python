factors =[3,6,9,12,15,18,21,24,27,30]
print(factors)
for x in factors:
    print(x)


#ex4.8#
def cube(n):
    Cubes = []
    for i in range(1,n+1):
        m = i**3
        Cubes.append(m)
    return Cubes

cube = cube(10)
print(cube)


#ex4.8 method 2#
Cube =[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
for x in Cube:
    print(x)