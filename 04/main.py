from collections import deque

class XmasWordSearcher:
    DIRECTIONS: tuple[tuple[int, int], ...] = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

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

    def _check_direction(self, start_row: int, start_col: int, word: str, direction: tuple[int, int]) -> int:
        row, col = start_row, start_col
        for char in word:
            if not self._inbounds(row, col) or self.grid[row][col] != char:
                return 0
            row += direction[0]
            col += direction[1]
        return 1

    # def _bfs(self, row: int, col: int, word: str) -> int:
    #     matches = 0
    #     q: deque[tuple[int, int, str, tuple[int, int]]] = deque()
    #     q.append((row, col, word, (0, 0)))

    #     if len(word) == 1 and self.grid[row][col] == w[0]:
    #         return 1

    #     for (dr, dc) in self.DIRECTIONS:
    #         if (
    #             0 <= (row + dr) < self.rows and
    #             0 <= (col + dc) < self.cols and
    #             self.grid[row + dr][col + dc] == word[1]
    #         ):
    #             q.append((row + dr, col + dc, word[1:], (dr, dc)))

    #     while q:
    #         r, c, w, (dr, dc) = q.popleft()

    #         if len(w) == 1 and self.grid[r][c] == w[0]:
    #             matches += 1
    #             continue

    #         if len(w) > 1:
    #             if (
    #                 0 <= (r + dr) < self.rows and
    #                 0 <= (c + dc) < self.cols and
    #                 self.grid[r + dr][c + dc] == w[1]
    #             ):
    #                 q.append((r + dr, c + dc, w[1:], (dr, dc)))

    #     return matches

    def search_for_word(self, word: str) -> int:
        matches = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == word[0]:
                    for (dr, dc) in self.DIRECTIONS:
                        matches += self._check_direction(r, c, word, (dr, dc))

        return matches

def main():
    searcher = XmasWordSearcher("input.txt")
    print(searcher.search_for_word("XMAS"))

if __name__ == "__main__":
    main()
