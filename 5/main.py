import copy

CARGOHOLD: dict = {
    "1": ["Q", "F", "L", "S", "R"],
    "2": ["T", "P", "G", "Q", "Z", "N"],
    "3": ["B", "Q", "M", "S"],
    "4": ["Q", "B", "C", "H", "J", "Z", "G", "T"],
    "5": ["S", "F", "N", "B", "M", "H", "P"],
    "6": ["G", "V", "L", "S", "N", "Q", "C", "P"],
    "7": ["F", "C", "W"],
    "8": ["M", "P", "V", "W", "Z", "G", "H", "Q"],
    "9": ["R", "N", "C", "L", "D", "Z", "G"]
}


class Cargo:
    def __init__(self, cargo: dict[str:list[str]]):
        self.cargo = cargo

    def move(self, source: str, target: str, amount: int = 1, multi: bool = False):
        in_move = []
        for i in range(amount):
            in_move.append((self.cargo[source].pop(0)))
        if multi:
            in_move.reverse()
        for item in in_move:
            self.cargo[target].insert(0, item)

    def __str__(self) -> str:
        ret: str = ""
        for i, item in self.cargo.items():
            ret = f'{ret}{item[0]}'
        return ret


def main(file_name: str) -> tuple[str, str]:
    part1: Cargo = Cargo(copy.deepcopy(CARGOHOLD))
    part2: Cargo = Cargo(copy.deepcopy(CARGOHOLD))
    with open(file_name) as f:
        for line in f:
            words: list = line.split()
            part1.move(words[3], words[5], int(words[1]))
            part2.move(words[3], words[5], int(words[1]), multi=True)
    return str(part1), str(part2)


if __name__ == '__main__':
    print(main('input.txt'))
