# For Loops

guests = ["Jon", "Jack", "James", "Kate", "Christine"]

# Bad programming:
# print(guests[0])
# print(guests[1])
# print(guests[2])

# We want to use loops
for guest in guests:
    print(f'Our guest is: {guest}')

for guest in guests:

    if guest == "Jon":
        print("Our esteemed guest Jon has arrived!")
    elif guest == "Christine":
        print("Christine is here!")

# Print "Hello World" 30 times
print(range(30))

for x in range(30):
    print(f"{x}: Hello World")
