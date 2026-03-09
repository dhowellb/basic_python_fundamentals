# Make a command to ask for 10 numbers and add them all up
def calculate_ten_numbers_sum():
    # Start a running total at zero. We use 0.0 because we are using decimals.
    total_sum = 0.0

    # Create a loop that will repeat the indented code exactly 10 times
    for i in range(10):
        # Ask the user to type a number. 
        # 'str(i + 1)' is a clever trick so it asks for "number 1" first instead of "number 0"
        current_number = float(input("\033[96mEnter number " + str(i + 1) + ": \033[0m"))
        
        # Add the number they just typed to our running total
        total_sum = total_sum + current_number

    # After the loop finishes all 10 times, print the final answer in green text
    print("\033[92mThe total sum is:\033[0m", total_sum)