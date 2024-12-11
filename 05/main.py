from typing import NamedTuple

class Rule(NamedTuple):
    first: int
    second: int

RulesList = list[Rule]
Update = list[int]
UpdateList = list[Update]

class PrintQueue:
    def __init__(self, filename: str = "input.txt") -> None:
        self.filename: str = filename
        self.rules_list: RulesList = []
        self.update_list: UpdateList = []
        self.rules_list, self.update_list = self._read_data()
        self.updates_in_incorrect_order: UpdateList = []
        self.updates_in_correct_order: UpdateList = self._get_updates_in_correct_order()

    def _read_data(self) -> tuple[RulesList, UpdateList]:
        with open(self.filename, "r") as f:
            contents = f.read()
            try:
                first_part, second_part = contents.split("\n\n")
            except ValueError as e:
                print("Error splitting input:", e)
            rules_list: RulesList = [
                Rule(*map(int, line.split("|")))
                for line in first_part.splitlines()
            ]
            update_list: UpdateList = [
                Update(map(int, line.split(",")))
                for line in second_part.splitlines()
            ]
            return rules_list, update_list

    def _get_updates_in_correct_order(self) -> UpdateList:
        correct_updates = []
        for update in self.update_list:
            should_continue = False
            for i, page in enumerate(update):
                preceding_pages = update[:i]
                succeeding_pages = update[i + 1:]
                matching_before_rules: RulesList = [
                    rule for rule in self.rules_list if rule.first == page
                ]
                matching_after_rules: RulesList = [
                    rule for rule in self.rules_list if rule.second == page
                ]
                if any(rule.second in preceding_pages for rule in matching_before_rules):
                    should_continue = True
                    break
                if any(rule.first in succeeding_pages for rule in matching_after_rules):
                    should_continue = True
                    break
            if should_continue:
                self.updates_in_incorrect_order.append(update)
                continue
            correct_updates.append(update)
        return correct_updates

    def _fix_incorrectly_ordered_updates(self) -> None:
        for update in self.updates_in_incorrect_order:
            change_made = False
            first_run = True
            while change_made or first_run:
                change_made = False
                first_run = False
                for i in range(len(update)):
                    should_break = False
                    page = update[i]
                    succeeding_pages = update[i + 1:]
                    matching_after_rules: RulesList = [
                        rule for rule in self.rules_list if rule.second == page
                    ]
                    for rule in matching_after_rules:
                        for succeeding_page in succeeding_pages:
                            if rule.first == succeeding_page:
                                j = update.index(succeeding_page)
                                update[i] = update[j]
                                update[j] = page
                                change_made = True
                                should_break = True
                                break
                        if should_break:
                            break


    def sum_middle_page_numbers_from_correct_updates(self) -> int:
        return sum(update[len(update) // 2] for update in self.updates_in_correct_order)

    def sum_middle_page_numbers_from_incorrect_updates(self) -> int:
        self._fix_incorrectly_ordered_updates()
        return sum(update[len(update) // 2] for update in self.updates_in_incorrect_order)



def main():
    print_queue = PrintQueue()
    print(print_queue.sum_middle_page_numbers_from_correct_updates())
    print(print_queue.sum_middle_page_numbers_from_incorrect_updates())

if __name__ == "__main__":
    main()
