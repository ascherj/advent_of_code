import re

class CorruptedMemoryScanner:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self._read_data()

    def _read_data(self) -> str:
        with open(self.filename, "r") as f:
            return "".join(f.read().splitlines())

    def _find_valid_mul_instructions(self) -> list[str]:
        """
        Find all valid mul instructions in the data. A valid mul instruction is a sequence of characters that can be interpreted as a multiplication operation.
        Valid arguments to the mul function are two numbers, each 1-3 digits long.
        """
        pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
        return re.findall(pattern, self.data)

    def _sum_valid_mul_instructions(self) -> int:
        return sum(int(a) * int(b) for a, b in self._find_valid_mul_instructions())

def main():
    scanner = CorruptedMemoryScanner("input.txt")
    print(scanner._sum_valid_mul_instructions())

if __name__ == "__main__":
    main()
