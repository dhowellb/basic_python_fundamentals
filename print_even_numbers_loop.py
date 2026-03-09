# Make a command to find and print all even numbers up to 100
def print_even_numbers():
    # Print a title message in cyan text so the user knows what is happening
    print("\033[96mEven numbers from 0 to 100:\033[0m")

    # Create a loop that goes from 0 all the way to 100.
    # We use '101' because Python always stops right before the last number!
    for i in range(101):
        # The '%' symbol finds the remainder after dividing by 2.
        # If the remainder is exactly zero ('==' means exactly equal), it is an even number!
        if i % 2 == 0:
            # Print the even number we just found in green text
            # We use 'str(i)' to turn the number into text so it can be printed with the color code
            print("\033[92m" + str(i) + "\033[0m")