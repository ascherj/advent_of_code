class XmasWordSearcher:
    DIRECTIONS: tuple[tuple[int, int], ...] = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    MAS_DIRECTIONS = {
        (1, 1): { # down-right
            (2, 0): (-1, 1),
            (0, 2): (1, -1)
        },
        (1, -1): { # down-left
            (0, -2): (1, 1),
            (2, 0): (-1, -1)
        },
        (-1, 1): { # up-right
            (-2, 0): (1, 1),
            (0, 2): (-1, -1)
        },
        (-1, -1): { # up-left
            (0, -2): (-1, 1),
            (-2, 0): (1, -1)
        }
    }

    def __init__(self, filename: str):
        self.filename: str = filename
        self.grid: list[list[str]] = self._create_grid()

    def _read_data(self) -> str:
        with open(self.filename, "r") as f:
            return f.read()

    def _create_grid(self) -> list[list[str]]:
        return [list(row) for row in self._read_data().split("\n")][:-1]

    @property
    def rows(self) -> int:
        return len(self.grid)

    @property
    def cols(self) -> int:
        return len(self.grid[0])

    def _inbounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def _check_direction(self, start_row: int, start_col: int, word: str, direction: tuple[int, int]) -> bool:
        row, col = start_row, start_col
        for char in word:
            if not self._inbounds(row, col) or self.grid[row][col] != char:
                return False
            row += direction[0]
            col += direction[1]
        return True

    def search_for_word(self, word: str) -> int:
        matches = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == word[0]:
                    for (dr, dc) in self.DIRECTIONS:
                        matches += 1 if self._check_direction(r, c, word, (dr, dc)) else 0

        return matches

    def search_for_mas(self) -> int:
        matches = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "M":
                    for (dr, dc) in self.MAS_DIRECTIONS.keys():
                        if self._check_direction(r, c, "MAS", (dr, dc)):
                            for (r2, c2), direction in self.MAS_DIRECTIONS[(dr, dc)].items():
                                if self._check_direction(r + r2, c + c2, "MAS", direction):
                                    matches += 1
                                    break

        return int(matches / 2)

def main():
    searcher = XmasWordSearcher("input.txt")
    print("Part 1:", searcher.search_for_word("XMAS"))
    print("Part 2:", searcher.search_for_mas())

if __name__ == "__main__":
    main()
