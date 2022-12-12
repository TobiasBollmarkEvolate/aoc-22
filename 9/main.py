class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def cordinates(self):
        return self.x, self.y

    def __str__(self):
        return str((self.x, self.y))


def move(line: str, rope: list[Position]):
    direction: str
    steps: int
    positions2: set = set()
    positions10: set = set()
    direction, steps = line.split()
    for _ in range(int(steps)):
        if direction == "L":
            rope[0].x -= 1
        elif direction == "R":
            rope[0].x += 1
        elif direction == "U":
            rope[0].y += 1
        elif direction == "D":
            rope[0].y -= 1
        for i, pos in enumerate(rope[1:]):
            follow(rope[i], pos)
            if i == 0:
                positions2.add(pos.cordinates())
            elif i == 8:
                positions10.add(pos.cordinates())
    return positions2, positions10


def follow(pos_h: Position, pos_t: Position):
    diff_x = pos_h.x - pos_t.x
    diff_y = pos_h.y - pos_t.y
    if not diff_x:
        if diff_y == 2:
            pos_t.y += 1
        elif diff_y == -2:
            pos_t.y -= 1
    elif not diff_y:
        if diff_x == 2:
            pos_t.x += 1
        elif diff_x == -2:
            pos_t.x -= 1
    elif abs(diff_y) > 1 or abs(diff_x) > 1:  # Diagonal with more than 1 diff
        if diff_x > 0:
            pos_t.x += 1
        else:
            pos_t.x -= 1
        if diff_y > 0:
            pos_t.y += 1
        else:
            pos_t.y -= 1


def main(file_name: str) -> tuple[int, int]:
    rope: list[Position] = []
    for _ in range(10):
        rope.append(Position(0, 0))
    position2: set = set()
    position10: set = set()
    with open(file_name) as f:
        for line in f:
            ret_position2, ret_position10 = move(line.strip(), rope)
            position2.update(ret_position2)
            position10.update(ret_position10)
    return len(position2), len(position10)


if __name__ == '__main__':
    print(main('input.txt'))
