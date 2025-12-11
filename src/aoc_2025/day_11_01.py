from copy import copy


def get_path_count(start, end, graph, visited):
    if start == end:
        return 1

    counter = 0
    for neighbor in graph[start]:
        new_visited = copy(visited)
        if neighbor not in new_visited:
            new_visited.add(neighbor)
            counter += get_path_count(neighbor, end, graph, new_visited)

    return counter


def main():
    with open("data/day_11.txt", "r") as file:
        raw = file.read()
    raw = raw.strip()

    lines = raw.split("\n")
    name_connection_raw = [l.split(": ") for l in lines]
    servers = {nc[0]: nc[1].split(" ") for nc in name_connection_raw}

    start = "you"
    end = "out"

    count = get_path_count(start, end, servers, set())
    print(count)


if __name__ == "__main__":
    main()

