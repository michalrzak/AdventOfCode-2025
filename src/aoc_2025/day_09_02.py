from collections import defaultdict


def floodfill(grid, start):
    visited = {start}
    next = [start]

    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while len(next) != 0:
        pos = next.pop()
        if grid[pos] == 1:
            continue
        grid[pos] = 1

        for n in neighbors:
            new_pos = (pos[0] + n[0], pos[1] + n[1])
            if new_pos not in visited:
                visited.add(new_pos)
            next.append(new_pos)


def make_line(grid, c1, c2):
    len_x = c1[0] - c2[0]
    len_y = c1[1] - c2[1]

    if len_x != 0:
        smaller = c1[0] if len_x < 0 else c2[0]
        larger = c1[0] if len_x > 0 else c2[0]

        for ele_x in range(smaller, larger+1):
            grid[ele_x, c1[1]] = 1

    else:
        smaller = c1[1] if len_y < 0 else c2[1]
        larger = c1[1] if len_y > 0 else c2[1]
        for ele_y in range(smaller, larger+1):
            grid[c1[0], ele_y] = 1


def main():
    with open("data/day_09.txt", "r") as file:
        raw = file.read()
    raw = raw.strip()
    lines = raw.split("\n")

    print(lines)
    coords = [tuple(map(int, l.split(","))) for l in lines]
    x_coord = list(set([ele[0] for ele in coords]))
    y_coord = list(set([ele[1] for ele in coords]))
    x_coord.sort()
    y_coord.sort()
    x_map = {x: i+1 for i, x in enumerate(x_coord)}
    x_map_flipped = {i: x for i, x in enumerate(x_coord)}
    y_map = {y: i+1 for i, y in enumerate(y_coord)}
    y_map_flipped = {i: y for i, y in enumerate(y_coord)}

    grid = defaultdict(lambda: 0)
    for i in range(len(coords)):
        c1 = coords[i]
        c2 = coords[(i + 1) % len(coords)]
        c1_mapped = (x_map[c1[0]], y_map[c1[1]])
        c2_mapped = (x_map[c2[0]], y_map[c2[1]])
        make_line(grid, c1_mapped, c2_mapped)

    start = (x_map[coords[100][0]] + 1, y_map[coords[100][1]] - 1)
    floodfill(grid, start)

    points = set([k for k, v in grid.items() if v == 1])

    rectangles = []
    for i1, c1 in enumerate(coords):
        for c2 in coords[i1 + 1:]:
            c1_mapped = (x_map[c1[0]], y_map[c1[1]])
            c2_mapped = (x_map[c2[0]], y_map[c2[1]])
            corners = [
                c1_mapped,
                (c1_mapped[0], c2_mapped[1]),
                c2_mapped,
                (c2_mapped[0], c1_mapped[1])
            ]
            new_grid = defaultdict(lambda: 0)
            for i in range(len(corners)):
                rc1 = corners[i]
                rc2 = corners[(i + 1) % len(corners)]
                make_line(new_grid, rc1, rc2)

            points_rect = set([k for k, v in new_grid.items() if v == 1])
            if len(points_rect.difference(points)) == 0:
                rectangles.append((abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1))

    print(max(rectangles))


if __name__ == "__main__":
    main()

