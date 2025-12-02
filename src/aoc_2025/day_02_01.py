import numpy as np


def get_digit_count(num):
    if num == 0:
        return 0
    digit_count = int(np.floor(np.log10(num)) + 1)
    return digit_count


def main():
    with open("data/day_02.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    ranges_raw = raw.split(",")
    ranges_str = [r.split("-") for r in ranges_raw]
    ranges = [(int(r[0]), int(r[1])) for r in ranges_str]
    assert all([len(r) == 2 for r in ranges])

    results = []
    for r in ranges:
        digit_count = get_digit_count(r[0])
        start_num = r[0] // (10 ** int(np.ceil(digit_count / 2)))

        out_of_range = False
        while not out_of_range:
            start_digit_count = get_digit_count(start_num)
            test_num = start_num * (10 ** start_digit_count) + start_num

            if test_num >= r[0] and test_num <= r[1]:
                results.append(test_num)

            if test_num > r[1]:
                out_of_range = True

            start_num += 1
    
    print(sum(results))


if __name__ == "__main__":
    main()
