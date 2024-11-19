import os
import operator
import time

def collectdata():
    key_len = 0
    input_dict = {}
    while True:
        os.system('clear')
        for i, v in input_dict.items():
            print(f"{i:{key_len}}:{v:>10}")  # For loop that prints current keys and values in the dictionary.
        key = input("\nInsert key: ")
        if key == '':
            break                            # If your input is empty, the program will assume you want to stop.
        key_len = max(len(key), key_len)     # Getting the maximum length of the keys so the print looks consistent.
        value = input("Insert value: ")
        try:
            input_dict[key] = float(value)   # This line tries to convert a string to a float, if it's not possible...
        except ValueError:
            print("That's not a number!")    # It notifies you!
            time.sleep(1)                    # Delay so you can actually see it
    return input_dict, key_len               # Return collected dictionary and largest key length

def filter(input_dict, key_len):
    os.system('clear')
    op = input("Enter operation (>, >= or <, <=): ")
    if (op != '>') and (op != '>=') and (op != '<') and (op != '<='):
        return filter(input_dict, key_len)
    try:
        cond = float(input("Enter condition: "))
    except ValueError:
        print("That's not a number!")
        time.sleep(1)
        return filter(input_dict, key_len)

    operators = {">": operator.gt, "<": operator.lt, ">=": operator.ge, "<=": operator.le} # String-operator look-up dictionary
    filteredata = {}
    if (op == '<') or (op == '<='):
        input_dict = dict(sorted(input_dict.items(), key=operator.itemgetter(1), reverse=True)) # Sorting the values depending on their selected...
    else:
        input_dict = dict(sorted(input_dict.items(), key=operator.itemgetter(1))) # operator, making sure to get the second value to make use of sorted()
    for i, v in input_dict.items():         # For each item in dictionary
        if operators[op](v, float(cond)):   # Check if item value complies with specified operation and condition
            filteredata[i] = v              # Append item-value pair to filtered data if so
    
    print("\n" + "-" * (key_len + 11))
    for i, v in filteredata.items():        # For each item in filtered dictionary
        print(f"{i:{key_len}}:{v:>10}")     # Print item-value pair in formatted fashion
    print("-" * (key_len + 11))
    print(f"\nSize of filtered data: {len(filteredata)}\nShowing values", op, "than", cond)

if __name__ == "__main__":
    args = collectdata()
    filter(args[0], args[1]) # Pass first function's return arguments into second function