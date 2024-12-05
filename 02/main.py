from typing import NewType

Level = NewType("Level", str)
Report = NewType("Report", list[Level])
ReportList = NewType("ReportList", list[Report])

def main():
    def read_data() -> ReportList:
        with open("input.txt", "r") as f:
            return [Report(report.split()) for report in f.read().splitlines()]

    def is_no_more_than_three_diff(report: Report) -> bool:
        return all(
            abs(int(report[i + 1]) - int(report[i])) <= 3
            for i in range(len(report) - 1)
        )

    def is_increasing(report: Report) -> bool:
        return all(
            int(report[i]) < int(report[i + 1])
            for i in range(len(report) - 1)
        )

    def is_decreasing(report: Report) -> bool:
        return all(
            int(report[i]) > int(report[i + 1])
            for i in range(len(report) - 1)
        )

    def is_good_report(report: Report) -> bool:
        return is_no_more_than_three_diff(report) and (
            is_increasing(report) or is_decreasing(report)
        )

    def count_good_reports(data: ReportList) -> int:
        good_reports: int = 0

        for report in data:
            if is_good_report(report):
                good_reports += 1
            else:
                for i in range(len(report)):
                    modified_report = report[:i] + report[i + 1 :]
                    if is_good_report(modified_report):
                        good_reports += 1
                        break

        return good_reports

    data = read_data()
    print(count_good_reports(data))


if __name__ == "__main__":
    main()
