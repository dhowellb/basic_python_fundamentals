# Make a command to divide two numbers
def calculate_quotient():
    # Ask the user for the first number and let them use decimals (float)
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check to make sure the second number is not zero 
    # (because dividing by zero breaks the computer's math!)
    if second_number != 0:
        # If it is not zero, divide the first number by the second number using '/'
        total_quotient = first_number / second_number
        
        # Print the final divided answer in green text
        print("\033[92mThe quotient is:\033[0m", total_quotient)
        
    # If the second number IS zero, do this instead:
    else:
        # Print an error message in red text so the user knows what went wrong
        print("\033[91mCannot divide by zero.\033[0m")