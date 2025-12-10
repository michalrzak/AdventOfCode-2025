from copy import copy
from queue import Queue
import numpy as np
from scipy.optimize import milp, LinearConstraint


def press(state, button):
    new_state = copy(state)
    for activation in button:
        new_state[activation] += 1
    return new_state


def bfs(goal, buttons):
    found = False
    queue = Queue()
    queue.put((np.zeros_like(goal), 0))

    seen = {str(np.zeros_like(goal))}
    build_log = dict()
    while not found:
        current, depth = queue.get()
        #print(current)
        for button in buttons:
            new_state = press(current, button)

            if np.all(new_state == goal):
                return depth + 1

            if np.any(new_state > goal):
                continue

            diff = goal - new_state
            gcd = np.gcd.reduce(diff)
            diff_norm = diff / gcd
            print(diff_norm)
            if str(diff_norm) in build_log:
                return depth + 1 + build_log[str(diff_norm)] * gcd

            repr = str(new_state)
            if repr not in seen:
                queue.put((new_state, depth + 1))
                seen.add(repr)
                build_log[repr] = depth + 1


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
    for goal, button in zip(joltage, buttons):
        a = np.zeros((len(goal), len(button)))
        for i, b in enumerate(button):
            col = np.zeros(len(goal))
            col[b] = 1
            a[:, i] = col


        constraint = LinearConstraint(a, goal, goal)
        solution = milp(
            np.ones(len(button)),
            integrality=np.ones(len(button)),
            constraints=constraint
        )
        print(solution.x)
        min_presses = sum(np.round(solution.x))

        results.append(min_presses)
    print(results)
    print(sum(results))


if __name__ == "__main__":
    main()

