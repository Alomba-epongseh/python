#3.4#
invitees = ["Mary","Paul","Peter"]
for invitee in invitees:
    print("Hello, "+invitee+" we are cordiately inviting you for a little get together at the James' Villa")

#3.5#
print("Its so sad that one of our guest Mr "+invitees[2]+ " can't join us. ")
invitees[2] = "Susan"
for invitee in invitees:
    print("Hello, "+invitee+" we are cordiately inviting you for a little get together at the James' Villa")

#3.6#
print("We bring to you some good news today. We found a bigger space and we will be extending invites to more people")
invitees.insert(0, "Mike")
invitees.insert(2, "Queen")
invitees.append("Joseph")
print(invitees)
for invitee in invitees:
    print("The James family will like the presence of "+invitee+ " to join them celebrate during a shared meal on saturday")