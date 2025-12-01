import numpy as np

def add_c(l, r):
    i = l + r
    zero_passes = 0
    print("i", i)

    if i > 99:
        zero_passes = i // 100
        i = i % 100

    elif i <= 0:
        zero_passes = - ((i - 1) // 100)
        if l == 0 or r == 0:
            zero_passes -= 1
        i = i % 100

    # if i < 0:
    #     print(i)
    #     print(i%100)
    #     i = 100 - (i % 100)
    #     print(i)

    print("zp", zero_passes)
    print("res", i)
    print("-----")
    return i, zero_passes

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
    results_z = []
    for ele in turns:
        current, zero_pass = add_c(current, ele)
        results.append(current)
        results_z.append(zero_pass)
    results = np.array(results)

    print(np.sum(results_z))


if __name__ == "__main__":
    main()

