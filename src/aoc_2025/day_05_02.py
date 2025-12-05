

def main():
    with open("data/day_05.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()

    ranges_raw, input_ids_raw = raw.split("\n\n")
    ranges_lines = ranges_raw.split("\n")
    ranges = list(
        map(lambda ele: (int(ele[0]), int(ele[1])),
            map(lambda ele: ele.split("-"), 
                ranges_lines)))

    input_ids = list(map(int, input_ids_raw.split("\n")))

    ranges.sort(key=lambda ele: ele[0])

    combined_all = False
    while not combined_all:
        combined_all = True

        new_ranges = []
        i = 0
        while i < len(ranges):
            r = ranges[i]

            if i == len(ranges) - 1:
                new_ranges.append(r)
                break

            next_r = ranges[i+1]

            if r[1] >= next_r[0] and r[1] <= next_r[1]:
                new_ranges.append((r[0], next_r[1]))
                combined_all = False
                i += 1
            elif r[1] >= next_r[0] and r[1] >= next_r[1]:
                new_ranges.append(r)
                combined_all = False
                i += 1
            else:
                new_ranges.append(r)
            i += 1
        ranges = new_ranges

    results = 0
    for r in ranges:
        results += (r[1] - r[0] + 1)

    print(results)


if __name__ == "__main__":
    main()

