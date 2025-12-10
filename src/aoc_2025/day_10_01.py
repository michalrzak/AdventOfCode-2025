from copy import copy
from queue import Queue
import numpy as np


def press(state, button):
    new_state = copy(state)
    for activation in button:
        new_state[activation] = not new_state[activation]
    return new_state


def bfs(goal, buttons):
    found = False
    queue = Queue()
    queue.put((np.zeros_like(goal, dtype=np.bool), 0))

    seen = {str(np.zeros_like(goal, dtype=np.bool))}
    while not found:
        current, depth = queue.get()
        for button in buttons:
            new_state = press(current, button)

            if np.all(new_state == goal):
                return depth + 1

            repr = str(new_state)
            if repr not in seen:
                queue.put((new_state, depth + 1))
                seen.add(repr)


def to_int_list(item):
    item = item.strip()
    no_brackets = item[1:-1]
    elements = no_brackets.split(",")
    return np.array(list(map(int, elements)))


def main():
    with open("data/day_10.txt", "r") as file:
        raw = file.read()
    raw = raw.strip()
    lines = raw.split("\n")
    elements = [l.split(" ") for l in lines]

    goals = [np.array([c == "#" for c in ele[0][1:-1]]) for ele in elements]
    joltage = [to_int_list(ele[-1]) for ele in elements]
    buttons = [[to_int_list(e) for e in ele[1:-1]] for ele in elements]

    results = []
    for goal, button in zip(goals, buttons):
        print(goal)
        min_presses = bfs(goal, button)
        results.append(min_presses)
    print(results)
    print(sum(results))


if __name__ == "__main__":
    main()

