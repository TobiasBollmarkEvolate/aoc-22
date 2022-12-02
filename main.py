def dec1(file_name: str) -> tuple[int, int]:
    sums: list[int] = []
    count: int = 0
    with open(file_name) as f:
        for line in f:
            if line == '\n':
                sums.append(count)
                sums.sort()
                sums = sums[-3:]  # Only keep the top 3 in memory
                count = 0
            else:
                count += int(line)
        return sums[-1:][0], sum(sums)


def dec2(file_name: str) -> int:
    player_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    def points(p1: str, p2: str):
        if p1 == "A":  # Rock
            if p2 == "Y":  # Paper
                return 6
            elif p2 == "Z":  # Scissors
                return 0
        elif p1 == "B":  # Paper
            if p2 == "X":  # Rock
                return 0
            elif p2 == "Z":  # Scissors
                return 6
        elif p1 == "C":  # Scissors
            if p2 == "X":  # Rock
                return 6
            elif p2 == "Y":  # Paper
                return 0
        return 3

    def hand(i):
        pass

    score: int = 0
    with open(file_name) as f:
        for line in f:
            opponent, player = line.split()
            score += points(opponent, player) + player_points[player]
    return score


if __name__ == '__main__':
    print(dec1('input1.txt'))
    print(dec2('input2.txt'))
