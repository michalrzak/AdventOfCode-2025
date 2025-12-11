from copy import copy


def get_path_count(start, end, graph, counts):
    if start == end:
        #if "fft" in visited and "dac" in visited:
        #    return 1
        #print(visited)
        counts[start] = 1
        return 1

    if start == "out":
        counts[start] = 0
        return 0

    counter = 0
    for neighbor in graph[start]:
        if neighbor in counts:
            counter += counts[neighbor]
        else:
            #print("visiting", neighbor)
            #visited.add(neighbor)
            counter += get_path_count(neighbor, end, graph, counts)


    counts[start] = counter
    return counter


def main():
    with open("data/day_11.txt", "r") as file:
        raw = file.read()
    raw = raw.strip()

    lines = raw.split("\n")
    name_connection_raw = [l.split(": ") for l in lines]
    servers = {nc[0]: nc[1].split(" ") for nc in name_connection_raw}

    start = "svr"
    end = "out"

    svr_fft_count = get_path_count("svr", "fft", servers, dict())
    print(svr_fft_count)
    fft_dac_count = get_path_count("fft", "dac", servers, dict())
    print(fft_dac_count)
    dac_out_count = get_path_count("dac", "out", servers, dict())
    print(dac_out_count)

    svr_dac_count = get_path_count("svr", "dac", servers, dict())
    print(svr_dac_count)
    dac_fft_count = get_path_count("dac", "fft", servers, dict())
    print(dac_fft_count)
    fft_out_count = get_path_count("fft", "out", servers, dict())
    print(fft_out_count)

    count = svr_fft_count * fft_dac_count * dac_out_count + svr_dac_count * dac_fft_count * fft_out_count
    print(count)


    #count = get_path_count(start, end, servers, dict())
    #@print(count)


if __name__ == "__main__":
    main()

