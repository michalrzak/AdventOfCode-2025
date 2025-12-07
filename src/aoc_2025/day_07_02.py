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
    multiples = {start: 1}
    split_counter = 0
    for y in range(len(tychon)):
        new_beams = beams.copy()
        new_multiples = multiples.copy()
        for beam_x in beams:
            if beam_x in splits[y]:
                split_counter += 1
                new_beams.remove(beam_x)
                multiple_l = multiples[beam_x]
                multiple_r = multiples[beam_x]
                new_multiples.pop(beam_x)

                if (beam_x - 1) in new_beams:
                    multiple_l += new_multiples[beam_x - 1]
                if (beam_x + 1) in new_beams:
                    multiple_r += new_multiples[beam_x + 1]

                new_beams.add(beam_x - 1)
                new_multiples[beam_x - 1] = multiple_l
                new_beams.add(beam_x + 1)
                new_multiples[beam_x + 1] = multiple_r
        beams = new_beams
        multiples = new_multiples

    print(beams)
    print(len(beams))
    paths = sum([value for key, value in multiples.items()])
    print(paths)
    print(multiples)


if __name__ == "__main__":
    main()

