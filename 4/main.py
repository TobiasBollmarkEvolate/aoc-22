from __future__ import annotations  # Allows for typing of Section in Section method arguments (1)


class Section:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def contains(self, section: Section) -> bool:
        return self.low <= section.low and self.high >= section.high

    def overlaps(self, section: Section) -> bool:
        return section.low >= self.low >= section.high or section.low <= self.high <= section.high


def string_to_sections(string: str) -> tuple[Section, Section]:
    section_string1: str
    section_string2: str
    section1_mmin: str
    section1_max: str
    section2_min: str
    section2_max: str
    section_string1, section_string2 = string.split(",")
    section1_min, section1_max = section_string1.split("-")
    section2_min, section2_max = section_string2.split("-")
    section1 = Section(int(section1_min), int(section1_max))
    section2 = Section(int(section2_min), int(section2_max))
    return section1, section2


def main(file_name: str) -> tuple[int, int]:
    count1: int = 0
    count2: int = 0
    with open(file_name) as f:
        for line in f:
            section1, section2 = string_to_sections(line)
            if section1.contains(section2) or section2.contains(section1):
                count1 += 1
            elif section1.overlaps(section2) or section2.overlaps(section1):
                count2 += 1
    return count1, count1 + count2


if __name__ == '__main__':
    print(main('input.txt'))
