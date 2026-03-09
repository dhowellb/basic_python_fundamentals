# Make a command to calculate a number to a certain power (exponents)
def calculate_power():
    # Ask the user for the base number (the big number on the bottom)
    base_number = float(input("\033[96mEnter the base number: \033[0m"))
    
    # Ask the user for the exponent number (the little number on top)
    exponent_number = float(input("\033[96mEnter the exponent number: \033[0m"))
    
    # Calculate the power using the '**' double star symbol
    # This means "base_number to the power of exponent_number"
    power_result = base_number ** exponent_number

    # Print the final calculated answer in green text
    print("\033[92mThe result is:\033[0m", power_result)

    # This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the power command we made at the top
    calculate_power()