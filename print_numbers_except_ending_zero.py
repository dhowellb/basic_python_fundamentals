# Make a command to print numbers up to 100, but skip the ones ending in zero
def print_numbers_except_ending_zero():
    # Print a title message in cyan text so the user knows what is happening
    print("\033[96mNumbers from 0 to 100 except those ending in zero:\033[0m")

    # Create a loop that goes from 0 all the way to 100.
    # We use '101' because Python always stops right before the last number!
    for i in range(101):
        # The '%' symbol finds the remainder after dividing by 10.
        # If the remainder is NOT zero ('!=' means not equal), the number does NOT end in zero!
        if i % 10 != 0:
            # Print the number we just found in green text
            # We use 'str(i)' to turn the number into text so it prints correctly with the color
            print("\033[92m" + str(i) + "\033[0m")

# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the printing command we made at the top
    print_numbers_except_ending_zero()