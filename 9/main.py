class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def cordinates(self):
        return self.x, self.y

    def __str__(self):
        return str((self.x, self.y))


def move(line, pos_h, pos_t):
    direction: str
    steps: int
    positions: set = set()
    direction, steps = line.split()
    for _ in range(int(steps)):
        if direction == "L":
            pos_h.x -= 1
        elif direction == "R":
            pos_h.x += 1
        elif direction == "U":
            pos_h.y += 1
        elif direction == "D":
            pos_h.y -= 1
        follow(pos_h, pos_t)
        positions.add(pos_t.cordinates())
    return positions


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
    pos_h = Position(0, 0)
    pos_t = Position(0, 0)
    positions: set = set()
    with open(file_name) as f:
        for line in f:
            positions.update(move(line.strip(), pos_h, pos_t))
    return len(positions), 0


if __name__ == '__main__':
    print(main('input.txt'))
