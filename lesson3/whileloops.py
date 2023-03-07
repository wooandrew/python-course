print("\n\n")

'''
    Types of Loops:
        While Loops                 # Continue to run WHILE a condition is TRUE.
        For Loops                   # Iterates through a list
        Do-While Loops
'''

#names = ["Jack", "Joe", "Jacey", "Jane"]

# For Loop
#for name in names:
#    print(name)
#
#counter = 0
#while counter < 500:
#    print(f"{counter}: {names[counter % 4]}")       # counter=20
#
#    if counter == 20:                               # counter=20 so we break
#        break
#
#    counter += 1                                    # counter=20

# We want to print "Hello world!" for 20 iterations, using a WHILE loop
# Do NOT use IF statements

counter = 0
while counter < 21:
    print(f"{counter}: Hello World!")

    counter += 1

# Do the same thing using a FOR loop
# Do NOT use IF statements or LISTS or COUNTER

for value in range(21):
    print(f"{value}: Hello World!")

# Using a WHILE loop, print "Hello World!" while counter is NOT equal to 30.

counter = 0
while True:

    if counter != 30:
        print(f"{counter}: Hello World!")

    counter += 1

