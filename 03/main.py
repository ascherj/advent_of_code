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

    def _process_data(self) -> int:
        sum = 0
        dont_text = "don't()"
        do_text = "do()"
        enabled = True
        curr = 0
        while curr < len(self.data):
            if self.data[curr:].startswith(dont_text):
                curr += len(dont_text)
                enabled = False
            elif self.data[curr:].startswith(do_text):
                curr += len(do_text)
                enabled = True
            else:
                pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
                match = re.match(pattern, self.data[curr:])
                if match and enabled:
                    sum += int(match.group(1)) * int(match.group(2))
                    curr += len(match.group())
                else:
                    curr += 1
        return sum

def main():
    scanner = CorruptedMemoryScanner("input.txt")
    print(scanner._process_data())

if __name__ == "__main__":
    main()
