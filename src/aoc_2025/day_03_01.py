import numpy as np

def main():
    with open("data/day_03.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    banks_raw = raw.split("\n")
    banks = np.array([[int(c) for c in bank] for bank in banks_raw])

    max_values = np.max(banks[:, :-1], axis=1, keepdims=True)
    print(max_values)

    results = []
    for bank, mv in zip(banks, max_values):
        o = np.where(bank == mv)[0][0]
        other_num = np.max(bank[o+1:])
        value = mv * 10 + other_num
        results.append(value)

    print(results)
    print(sum(results))


if __name__ == "__main__":
    main()

