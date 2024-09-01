# using *continue* keyword within loops
number = 0 # initialising variable

while number < 7: # while loop condition
    number += 3 # counter increment

    if number == 6: # if conditional statement with continue keyword
        continue # it skips the iteration if number == 6

    print(number) # print statment

    # Output:
    # 3
    # 9