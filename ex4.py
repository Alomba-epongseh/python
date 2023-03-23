def multiple(n):
    multiples = []
    for x in range(1,n+1):
        m = x * 3
        multiples.append(m)
    return multiples

Multiple = multiple(10)
print(Multiple)

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
print(cube) # hope u understand this code. its not just a copied code. #yes i do understand it
