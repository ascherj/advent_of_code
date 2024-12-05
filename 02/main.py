def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    good_reports = 0

    def is_no_more_than_three_diff(report):
        parts = report.split()
        return all(
            abs(int(parts[i + 1]) - int(parts[i])) <= 3
            for i in range(len(parts) - 1)
        )

    def is_increasing(report):
        parts = report.split()
        return all(
            int(parts[i]) < int(parts[i + 1])
            for i in range(len(parts) - 1)
        )

    def is_decreasing(report):
        parts = report.split()
        return all(
            int(parts[i]) > int(parts[i + 1])
            for i in range(len(parts) - 1)
        )

    def is_good_report(report):
        return is_no_more_than_three_diff(report) and (
            is_increasing(report) or is_decreasing(report)
        )

    for report in data:
        if is_good_report(report):
            good_reports += 1

    print(good_reports)


if __name__ == "__main__":
    main()
