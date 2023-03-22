factors =[3,6,9,12,15,18,21,24,27,30]
print(factors)
for x in factors:
    print(x)
''''
your  code fotr the multiples have issues. u didnot use for loop to ptint

#create and empty list
#use for ....in range(*, *, *):
    print ..... 

then  add it to the epty list    
'''''

#ex4.8#
def cube(n):
    Cubes = []
    for i in range(1,n+1):
        m = i**3
        Cubes.append(m)
    return Cubes

cube = cube(10)
print(cube) # hope u understand this code. its not just a copied code. 


#ex4.8 method 2#
Cube =[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
for x in Cube:
    print(x)
# this code doesnt looks correct