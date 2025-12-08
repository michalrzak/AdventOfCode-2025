def eq(posl, posr):
    return posl[0] == posr[0] and posl[1] == posr[1] and posl[2] == posr[2]


def distance(posl, posr):
    return (
        (posl[0] - posr[0]) ** 2 + 
        (posl[1] - posr[1]) ** 2 + 
        (posl[2] - posr[2]) ** 2
    )


def main():
    with open("data/day_08.txt", "r") as file:
        raw = file.read()
    raw = raw.strip()

    lines = raw.split("\n")
    coordinates = [tuple(map(int, l.split(","))) for l in lines]

    all_distances = []

    for i1, pos1 in enumerate(coordinates):
        for i2, pos2 in enumerate(coordinates[i1:]):
            real_i2 = i2 + i1
            if i1 == real_i2:
                continue
            all_distances.append(((i1, real_i2), distance(pos1, pos2)))

    all_distances_sorted = sorted(all_distances, key=lambda ele: ele[1])

    circuits = []
    seen_items = set()
    for i, item in enumerate(all_distances_sorted):
        l, r = item[0]

        found_l = None
        for i_c, c in enumerate(circuits):
            if l in c:
                found_l = i_c
                break

        found_r = None
        for i_c, c in enumerate(circuits):
            if r in c:
                found_r = i_c
                break

        if found_l is None and found_r is None:
            circuits.append(set(item[0]))

        if found_l is None and found_r is not None:
            circuits[found_r].add(l)

        if found_l is not  None and found_r is None:
            circuits[found_l].add(r)

        if found_l is not None and found_r is not None:
            if found_r == found_l:
                continue
            circ_l = circuits[found_l]
            circ_r = circuits[found_r]

            if found_r < found_l:
                first = found_l
                second = found_r
            else:
                first = found_r
                second = found_l

            circuits.pop(first)
            circuits.pop(second)

            new_circ = circ_l.union(circ_r)
            circuits.append(new_circ)

        seen_items.add(l)
        seen_items.add(r)
        if len(seen_items) == len(coordinates):
            break

    last = all_distances_sorted[i][0]
    print(last)
    print(len(circuits))
    print(coordinates[last[0]][0] * coordinates[last[1]][0])


if __name__ == "__main__":
    main()
