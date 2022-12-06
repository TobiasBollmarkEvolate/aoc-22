from __future__ import annotations  # Allows for typing of Section in Section method arguments (1)


class Section:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def contains(self, section: Section) -> bool:
        return self.low <= section.low and self.high >= section.high

    def overlaps(self, section: Section) -> bool:
        return section.low >= self.low >= section.high or section.low <= self.high <= section.high


def string_to_sections(string: str) -> list[Section]:
    sections: list[Section] = []
    for section in string.split(","):
        section_min: str
        section_max: str
        section_min, section_max = section.split("-")
        sections.append(Section(int(section_min), int(section_max)))
    return sections


def main(file_name: str) -> tuple[int, int]:
    count1: int = 0
    count2: int = 0
    with open(file_name) as f:
        for line in f:
            sections: list[Section] = string_to_sections(line)
            if sections[0].contains(sections[1]) or sections[1].contains(sections[0]):
                count1 += 1
            elif sections[0].overlaps(sections[1]) or sections[1].overlaps(sections[0]):
                count2 += 1
    return count1, count1 + count2


if __name__ == '__main__':
    print(main('input.txt'))
