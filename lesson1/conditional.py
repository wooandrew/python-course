# If/Else statements
# conditional

#x = 10

# mathematical conditions
# equals, greater than, less than, greater than or equal to, less than or equal to
# ==, >, <, >=, <=

#if x <= 20:
#    print("x equals 20. The statement x == 20 is true.")
#elif x <= 19:
#    print("x equals 19. The statement x == 19 is true.")
#else:
#    print(f"x equals {x}. Defaulted to else.")

# ------------------------------------------------------
#if x == 10:
#    print("Hello World")
#if x < 20:
#    print("Hello world! 2")

# 

# name = "John"
# age = 30
# 
# '''
# Objective:
# 
#     if name equals Samantha, print:
#         John is {age} years old.
# 
#     otherwise print:
#         "Oops! We don't know who Samantha is."
# 
# '''
# if name == "Samantha":
#     print(f"John is {age} years old.")
# else:
#     print("Oops! We don't know who Samantha is.")

name = "John"
age = 20

'''
Objective / Problem Domain:

    if name is John
    ADD 30 to age.
    and PRINT John is {age}.

    else if name is Kat
    SUBTRACT 10 from age
    and PRINT Kat is {age}.

    otherwise
    PRINT error
'''

if name == "John":
    age += 30               # OR age = age + 30
    print(f"John is {age}.")
elif name == "Kat":
    age -= 10
    print(f"Kat is {age}.")
else:
    print("error")


if name == "John" and age == 20:
    print("John is 20 years old.")

if name == "John" or name == "Kate":
    print("John or Kate is 20 years old.")
