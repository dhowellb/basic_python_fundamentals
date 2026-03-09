#Make our own command to find the bigger number
def get_bigger_number():
    # Ask the user for the first number. 
    # 'float' lets them type decimals. The weird code makes the text colored.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check if the first number is bigger than the second
    if first_number > second_number:
        # If it is bigger, print the first number in green
        print("\033[92mThe bigger number is:\033[0m", first_number)
        
    # Check if the second number is bigger instead
    elif second_number > first_number:
        # If it is bigger, print the second number in green
        print("\033[92mThe bigger number is:\033[0m", second_number)
        
    # If neither is bigger, they must be exactly the same
    else:
        # Print that they are equal in yellow
        print("\033[93mBoth numbers are equal.\033[0m")