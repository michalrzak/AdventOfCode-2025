import numpy as np


def get_digit_count(num):
    if num == 0:
        return 0
    digit_count = int(np.floor(np.log10(num)) + 1)
    return digit_count


def repeat(num, n):
    digit_count = get_digit_count(num)

    res = num
    for _ in range(n-1):
        res *= (10 ** digit_count)
        res += num

    return res


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
        start_num = 1 # r[0] // (10 ** int(np.ceil(digit_count / 2)))

        out_of_range = False
        per_r_result = set()
        while not out_of_range:
            start_digit_count = get_digit_count(start_num)
            n = int(np.ceil(digit_count / start_digit_count))
            test_num_low = repeat(start_num, n)
            test_num_high = repeat(start_num, n+1)

            if test_num_low >= r[0] and test_num_low <= r[1]:
                per_r_result.add(test_num_low)
            if test_num_high >= r[0] and test_num_high <= r[1]:
                per_r_result.add(test_num_high)

            if (test_num_low > r[1] and n == 2) or n == 1:
                out_of_range = True

            start_num += 1
        results.extend(per_r_result)
    
    print(results)
    print(sum(results))


if __name__ == "__main__":
    main()
