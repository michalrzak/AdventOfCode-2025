from copy import copy
from functools import cache
from types import FrameType


def print_grid(grid, grid_size):
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            c = "#" if (x, y) in grid else "."
            print(c, end="")
        print("")


@cache
def rotate_90(present_set, grid_size):
    new_present = set()
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if (x, y) not in present_set:
                continue
            new_present.add(((2-y), x))
    return frozenset(new_present)


def flip_x(grid, grid_size):
    return frozenset({(grid_size[0] - pos[0] - 1, pos[1]) for pos in grid})


def flip_y(grid, grid_size):
    return frozenset({(pos[0], grid_size[1] - pos[1] - 1) for pos in grid})


def add_pos(lhs, rhs):
    return lhs[0] + rhs[0], lhs[1] + rhs[1]


def try_to_place(grid, present, pos, grid_size):
    shifted_present = {add_pos(p, pos) for p in present}
    if not all(map(lambda ele: ele[0] < grid_size[0] and ele[1] < grid_size[1], shifted_present)):
        return False
    #print_grid(shifted_present, (12, 5))
    if len(shifted_present.intersection(grid)) != 0:
        return False

    grid.update(shifted_present)
    return True


def place_present(grid, grid_size, presents, present_counts, seen):
    frozen_grid = frozenset(grid)
    if frozen_grid in seen:
        return False

    frozen_grid_fx = flip_x(frozen_grid, grid_size)
    frozen_grid_fy = flip_y(frozen_grid, grid_size)
    frozen_grid_fxy = flip_x(frozen_grid_fy, grid_size)
    seen.add(frozen_grid)
    seen.add(frozen_grid_fx)
    seen.add(frozen_grid_fy)
    seen.add(frozen_grid_fxy)

    #print(len(seen))

    if all(map(lambda ele: ele == 0, present_counts)):
        return True

    for i, present_count in enumerate(present_counts):
        if present_count == 0:
            continue

        new_count = copy(present_counts)
        new_count[i] -= 1

        for y in range(grid_size[1]):
            for x in range(grid_size[0]):

                present = presents[i]
                for rot in range(4):
                    new_grid = copy(grid)
                    placed = try_to_place(new_grid, present, (x, y), grid_size)
                    if placed:
                        #print_grid(new_grid, grid_size)
                        #print()
                        #import pdb;pdb.set_trace()
                        found = place_present(new_grid, grid_size, presents, new_count, seen)
                        if found:
                            return True

                    present = rotate_90(present, (3, 3))

        # break after first non zero count
        break

    return False


def main():
    with open("data/day_12.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    blocks = raw.split("\n\n")

    presents = []
    for block in blocks[:-1]:
        lines = block.split("\n")
        present = set()
        for y, l in enumerate(lines[1:]):
            for x, c in enumerate(l):
                if c == "#":
                    present.add((x, y))
        presents.append(frozenset(present))

    grids = []
    grid_sizes = []
    present_counts = []
    lines = blocks[-1].split("\n")
    for l in lines:
        grid_size, present_count_raw = l.split(": ")
        x_size, y_size = grid_size.split("x")
        grid = set()
        present_count = list(map(int, present_count_raw.split(" ")))

        grids.append(grid)
        grid_sizes.append((int(x_size), int(y_size)))
        present_counts.append(present_count)

    present_areas = [len(p) for p in presents]
    count = 0
    for i in range(len(grids)):
        print(i)
        required_size = sum(present_areas[j] * pc for j, pc in enumerate(present_counts[i]))
        if required_size > (grid_sizes[i][0] * grid_sizes[i][1]):
            continue
        if place_present(grids[i], grid_sizes[i], presents, present_counts[i], set()):
            count += 1
    print(count)


if __name__ == "__main__":
    main()

