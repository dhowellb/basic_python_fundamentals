# Make our own command to check if numbers are exactly the same
def check_if_equal():
    # Ask the user to type the first number. 
    # 'float' lets them type decimals.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user to type the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check if the first number is exactly equal to the second number
    # (We use two equal signs '==' to compare them)
    if first_number == second_number:
        # If they are the same, print "Equal" in green text
        print("\033[92mEqual\033[0m")

        # This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the command we made at the top
    check_if_equal()