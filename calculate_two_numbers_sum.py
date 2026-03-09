# Make a command to add two numbers together
def calculate_sum():
    # Ask the user for the first number and let them use decimals (float)
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number
    second_number = float(input("\033[96mEnter the second number: \033[0m"))
    
    # Add the first number and second number together and save it
    total_sum = first_number + second_number

    # Print the final answer in green text
    print("\033[92mThe sum is:\033[0m", total_sum)

    # This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the addition command we made at the top
    calculate_sum()