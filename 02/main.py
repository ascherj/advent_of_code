from typing import NewType

Level = NewType("Level", str)
Report = NewType("Report", list[Level])
ReportList = NewType("ReportList", list[Report])

class ReportAnalyzer:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self._read_data()

    def _read_data(self) -> ReportList:
        with open(self.filename, "r") as f:
            return [Report(report.split()) for report in f.read().splitlines()]

    def _is_no_more_than_three_diff(self, report: Report) -> bool:
        return all(
            abs(int(report[i + 1]) - int(report[i])) <= 3
            for i in range(len(report) - 1)
        )

    def _is_increasing(self, report: Report) -> bool:
        return all(
            int(report[i]) < int(report[i + 1])
            for i in range(len(report) - 1)
        )

    def _is_decreasing(self, report: Report) -> bool:
        return all(
            int(report[i]) > int(report[i + 1])
            for i in range(len(report) - 1)
        )

    def _is_good_report(self, report: Report) -> bool:
        return self._is_no_more_than_three_diff(report) and (
            self._is_increasing(report) or self._is_decreasing(report)
        )

    def count_good_reports(self) -> int:
        good_reports: int = 0

        for report in self.data:
            if self._is_good_report(report):
                good_reports += 1
            else:
                for i in range(len(report)):
                    modified_report = report[:i] + report[i + 1:]
                    if self._is_good_report(modified_report):
                        good_reports += 1
                        break

        return good_reports

def main():
    analyzer = ReportAnalyzer("input.txt")
    print(analyzer.count_good_reports())

if __name__ == "__main__":
    main()
