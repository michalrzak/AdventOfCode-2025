from collections import defaultdict


def main():
    with open("data/day_04.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    lines = raw.split("\n")

    grid = defaultdict(lambda: '.')
    paper_positions = []
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            grid[(x, y)] = c
            if c == '@':
                paper_positions.append((x, y))

    neighbours = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    accessible = 0
    for pos in paper_positions:
        neighbour_count = 0
        for n in neighbours:
            new_pos = (pos[0] + n[0], pos[1] + n[1])
            if grid[new_pos] == '@':
                neighbour_count += 1
        if neighbour_count < 4:
            accessible += 1

    print(accessible)


if __name__ == "__main__":
    main()

