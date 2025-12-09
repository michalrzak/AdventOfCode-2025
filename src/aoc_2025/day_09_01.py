

def main():
    with open("data/day_09.txt", "r") as file:
        raw = file.read()
    raw = raw.strip()
    lines = raw.split("\n")

    print(lines)
    coords = [tuple(map(int, l.split(","))) for l in lines]

    rectangles = []
    for i1, c1 in enumerate(coords):
        for c2 in coords[i1 + 1:]:
            rectangles.append(abs(c1[0] - c2[0] + 1) * abs(c1[1] - c2[1] + 1))

    print(max(rectangles))


if __name__ == "__main__":
    main()

