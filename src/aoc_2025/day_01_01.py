import numpy as np

def add_c(l, r):
    i = l + r

    if i > 99 or i < 0:
        i = i % 100
    # if i < 0:
    #     print(i)
    #     print(i%100)
    #     i = 100 - (i % 100)
    #     print(i)

    return i

def main() -> None:
    with open("data/day_01.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    lines = raw.split("\n")

    directions = np.array([1 if ele[0] == "R" else -1 for ele in lines])
    values = np.array([int(ele[1:]) for ele in lines])

    turns = directions * values

    current = 50
    results = []
    for ele in turns:
        current = add_c(current, ele)
        results.append(current)
    results = np.array(results)
    print(results)

    res = np.sum(results == 0)
    print(current)

    print(res)


if __name__ == "__main__":
    main()

