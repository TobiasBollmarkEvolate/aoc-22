class CRT:
    def __init__(self, size: tuple[int, int]):
        self._pixels: list[bool] = []
        self._width = size[0]
        self._height = size[1]
        self._pos = 0
        self._row = 0
        for _ in range(self._height * self._width):
            self._pixels.append(False)

    def draw(self, value):
        if self._pos % self._width == 0:
            print("")
            self._row += 1
            self._pos = 0
        if value in [self._pos - 1, self._pos, self._pos + 1]:
            print("#", end="")
        else:
            print(".", end="")
        self._pos += 1
        if self._pos > len(self._pixels):
            self._row = 0


class Clock:
    def __init__(self, monitors: list[int]):
        self._tick: int = 0
        self._monitors: list[list[int, int]] = []
        for monitor in monitors:
            self._monitors.append([monitor, 0])

    def incr(self, value):
        self._tick += 1
        for monitor in self._monitors:
            if self._tick == monitor[0]:
                monitor[1] = value * monitor[0]

    def monitor_sum(self):
        ret = 0
        for monitor in self._monitors:
            ret += monitor[1]
        return ret


def main(file_name: str) -> int:
    clock = Clock([20, 60, 100, 140, 180, 220])
    screen = CRT((40, 6))
    value = 1
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            args = line.split()
            if args[0] == "noop":
                clock.incr(value)
                screen.draw(value)
            elif args[0] == "addx":
                clock.incr(value)
                screen.draw(value)
                clock.incr(value)
                screen.draw(value)
                value += int(args[1])
    print("")
    return clock.monitor_sum()


if __name__ == '__main__':
    print(main('input.txt'))
