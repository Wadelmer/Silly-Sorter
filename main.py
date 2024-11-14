input_dict = {}

while True:
    insert = input()
    if insert == '-s':
        break
    elif insert == '':
        pass
    else:
        while True:
            value = input()
            if value != '':
                if value.isdecimal():
                    value = int(value)
                    input_dict[insert] = value
                    print(input_dict)
                    break
                elif value == '-s':
                    break
                else:
                    print("The value must be a decimal!")

chosen_opt = input("Options:\n0 -> From largest to smallest\n(Use 1 instead for the opposite option)\n\n2 -> Sort from range\n\n")
if chosen_opt == '0':
    print(dict(sorted(input_dict.items())))
elif chosen_opt == '1':
    print(dict(sorted(input_dict.items(), reverse=True)))

    # Sort doesn't want to work, I will fix it later when I feel like it lol