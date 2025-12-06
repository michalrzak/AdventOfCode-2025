import re
import numpy as np


def main():
    with open("data/day_06.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    lines = raw.split("\n")

    elements = [re.split(r" +", line.strip()) for line in lines]

    operations = elements[-1]
    elements_ints = [[int(ele) for ele in row] for row in elements[:-1]]
    numbers = np.array(elements_ints)

    print([len(ele) for ele in elements])
    print(operations)
    print(numbers)

    results = []
    for op, col in zip(operations, numbers.T):
        res = 0
        if op == "+":
            res = np.sum(col)
        elif op == "*":
            res = np.prod(col)
        else:
            assert False
        results.append(res)

    print(results)
    print(np.sum(results))

if __name__ == "__main__":
    main()
