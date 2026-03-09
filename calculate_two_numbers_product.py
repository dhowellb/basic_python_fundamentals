# Make a command to multiply two numbers together
def calculate_product():
    # Ask the user for the first number and let them use decimals (float)
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number
    second_number = float(input("\033[96mEnter the second number: \033[0m"))
    
    # Multiply the first number and second number together using the '*' star symbol
    total_product = first_number * second_number

    # Print the final multiplied answer in green text
    print("\033[92mThe product is:\033[0m", total_product)

    # This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the multiplication command we made at the top
    calculate_product()