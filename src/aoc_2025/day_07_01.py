

def main():
    with open("data/day_07.txt", "r") as file:
        raw = file.read()

    raw = raw.strip()
    lines = raw.split("\n")

    start = lines[0].index("S")
    tychon = lines[1:]

    splits = dict()
    for y, line in enumerate(tychon):
        indices = [i for i, c in enumerate(line) if c == "^"]
        splits[y] = indices

    beams = {start}
    split_counter = 0
    for y in range(len(tychon)):
        new_beams = beams.copy()
        for beam_x in beams:
            if beam_x in splits[y]:
                split_counter += 1
                new_beams.remove(beam_x)
                new_beams.add(beam_x + 1)
                new_beams.add(beam_x - 1)
        beams = new_beams

    print(beams)
    print(len(beams))
    print(split_counter)


if __name__ == "__main__":
    main()

