class Section:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def contains(self, section):
        return self.low <= section.low and self.high >= section.high


def part1(line: str):
    section_string1, section_string2 = line.split(",")
    section1_min, section1_max = section_string1.split("-")
    section2_min, section2_max = section_string2.split("-")
    section1 = Section(int(section1_min), int(section1_max))
    section2 = Section(int(section2_min), int(section2_max))
    return 1 if section1.contains(section2) or section2.contains(section1) else 0


def main(file_name: str) -> tuple[int, int]:
    count1: int = 0
    with open(file_name) as f:
        for line in f:
            print(line)
            count1 += part1(line)
            print(count1)

    return count1, 0


if __name__ == '__main__':
    print(main('input.txt'))
