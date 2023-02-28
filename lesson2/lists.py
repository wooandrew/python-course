# Lists

lst0 = [1, 2, "Hello World", 2.33]

print(lst0[3])

# Lists are for grouping similar items, generally
guests = ["John", "Jack", "Kaitlyn", "Gary"]            # For example, this is a list of guests

guests.pop(1)                                           # list.pop(arg=index), if no arguments are provided, last element is removed.
print(guests)

guests.insert(3, "Alex")                                # inserts "Alex" at index 3
print(guests)

guests.append("Christie")                               # append adds to end of list
print(guests)

guests[0] = "Jon"                                       # change value of list item using assignment operator
print(guests)

'''
if guests[2] == "Kaitlyn":
    print("Guest is Kaitlyn!")
elif guests[3] == "Gary":
    print("Guest is Gary!")

if guests[1] == "Jen":
    print("Guest is Jen!")
else:
    print("Unknown Guest!")
'''
