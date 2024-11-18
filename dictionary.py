import operator

def evaluate(keys, values, operation, condition):
    operators = {">": operator.gt, "<": operator.lt}
    sortedata = []

    for i in range(len(values)):
        if operators[operation](int(values[i]), int(condition)):
            sortedata.append((keys[i], values[i]))
    
    print("------------------------------")
    for i in range(len(sortedata)):
        print(f"{sortedata[i][0]}:{sortedata[i][1]:>10}")
    print("------------------------------")
    print(f"Size of sorted data: {len(sortedata)}")

if __name__ == "__main__":
    keys = input("Enter keys separated by spaces: ").split()
    values = []
    while len(values) != len(keys):
        values = input("Enter values separated by spaces: ").split()
    op = input("Enter operation (> or <): ")
    cond = input("Enter condition: ")
    evaluate(keys, values, op, cond)