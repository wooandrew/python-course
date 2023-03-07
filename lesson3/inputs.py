print("\n\n\n")

# Inputs allow users to interact with with python script

#V  V   V         V Paramter
age = input("How old are you? ")    # <- With respect to the input function, 
                                    # anything inside quotes is the PROMPT      <- input(prompt)

print(f"You are {age} years old!")

#     V "casting" -> changing one variable type into another variable type : for example, str -> int
if int(age) < 50:
    print(f"You are {age} years old, which is less than 50!")
