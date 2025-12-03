import numpy as np

def main():
    with open("data/day_03.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    banks_raw = raw.split("\n")
    banks = np.array([[int(c) for c in bank] for bank in banks_raw])

    results = []
    for bank in banks:
        num = 0
        start_index = 0
        for i in range(12):
            max_value = np.max(bank[start_index:len(bank)-(11 - i)])
            index = np.where(bank[start_index:] == max_value)[0][0] + start_index

            num = num * 10 + max_value
            start_index = index + 1

        results.append(num)

    print(results)
    print(sum(results))


if __name__ == "__main__":
    main()

