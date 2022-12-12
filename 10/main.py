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


def main(file_name: str) -> tuple[int, int]:
    clock = Clock([20, 60, 100, 140, 180, 220])
    value = 1
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            args = line.split()
            if args[0] == "noop":
                clock.incr(value)
            elif args[0] == "addx":
                clock.incr(value)
                clock.incr(value)
                value += int(args[1])
    return clock.monitor_sum(), 0


if __name__ == '__main__':
    print(main('input.txt'))
