# Make a command to ask for 10 numbers and count how many are odd
def count_odd_numbers():
    # Start a counter at zero to keep track of the odd numbers we find
    odd_count = 0

    # Create a loop that will repeat the next steps exactly 10 times
    for i in range(10):
        # Ask the user to type a whole number. 
        # We use 'int' (integer) instead of 'float' because odd/even only works on whole numbers without decimals.
        current_number = int(input("\033[96mEnter integer number " + str(i + 1) + ": \033[0m"))
        
        # The '%' symbol finds the remainder after dividing by 2.
        # If the remainder is NOT zero ('!=' means not equal), the number is odd!
        if current_number % 2 != 0:
            # Add 1 to our running tally of odd numbers
            odd_count = odd_count + 1

    # After the loop finishes checking all 10 numbers, print the final count in green
    print("\033[92mTotal odd numbers:\033[0m", odd_count)