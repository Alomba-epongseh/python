#ex7.1#
car = input("Enter desired car for rental: ")
print("Let me see if i can find you a " +car)

#7.2#
people = int(input("How many people do you have in your dinner group: "))
if(people > 8):
        print("Sorry, you will have to wait for a table")
else:
        print("Table is ready")

#7.3#
number = int(input("Enter a number: "))
if(number%10 == 0):
        print(str(number)+ "is a multiple of 10")
else:
        print(str(number)+ "is not a multiple of 10")