# A function named hello() that prints a greeting to the user. 
# This function should accept no arguments and returns nothing.

def hello():
    print("hello user")
hello()

# A function named pack() that accepts three arguments, 
# and returns a single list with the three arguments inside 
# as list elements.


def pack(a,b,c):
    item=[a,b,c]
    return item
print(pack("pink", "blue", "red"))






# A function called eat_lunch(). 
# This function should accept a list of any length, 
# and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" 
# (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". 
# he function should not return anything.

def eat_lunch (food):
    if food:
        for item in food:
            if item == food[0]:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")
    else: 
        print("My lunchbox is empty!")

my_food = []

eat_lunch(my_food)