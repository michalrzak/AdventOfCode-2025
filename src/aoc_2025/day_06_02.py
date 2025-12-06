import re
import numpy as np


def main():
    with open("data/day_06.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    lines = raw.split("\n")

    elements = [re.split(r" +", line.strip()) for line in lines]

    operations = elements[-1]
    input_grid = np.array([[c for c in line] for line in lines[:-1]])
    print(input_grid)

    i_op = 0
    operands = []
    results = []
    for col in input_grid.T:
        if np.all(col == " "):
            if operations[i_op] == "+":
                results.append(np.sum(operands))
            elif operations[i_op] == "*":
                results.append(np.prod(operands))
            else:
                assert False
            i_op += 1
            operands = []
            continue

        valid_elements = col[col != " "]
        num = 0
        for ele in valid_elements:
            num = num * 10 + int(ele)
        operands.append(num)

    # one additional time at the end

    if operations[i_op] == "+":
        results.append(np.sum(operands))
    elif operations[i_op] == "*":
        results.append(np.prod(operands))
    else:
        assert False

    print(results)
    print(np.sum(results))


if __name__ == "__main__":
    main()
