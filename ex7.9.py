sandwich_orders = ["Regular plain old", "Open Face", "Wrap", "Pinwheel","Grilled", "pastrima"]
finished_sandwiches = [ ]

print("Deli has ran out of Pastrima sandwich")

for sandwich in sandwich_orders:
    print("I made your "+sandwich+ " sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)


for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    
while "pastrima" in sandwich_orders:
   sandwich_orders.remove("pastrima")
print(sandwich_orders)