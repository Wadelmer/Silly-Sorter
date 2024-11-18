import os

input_dict = {}

key_len = 0
while True:
    os.system('clear') # This function is used to clear the terminal.
    for i, v in input_dict.items():
        print(f"{i:{key_len}<}:{v:>10}") # For loop that prints current keys and values in the dictionary.
    key = input()
    if key == '':
        break # If your input is empty, the program will assume you want to stop.
    key_len = max(len(key), key_len) # Getting the maximum length of the keys so the print looks consistent.
    value = input()
    try:
        input_dict[key] = float(value) # This line tries to convert a string to a float, if it's not possible...
    except ValueError:
        print("That's not a number!") # It notifies you!

# sorted(input_dict.items(), reverse=True)