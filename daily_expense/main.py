from typing import List, Dict


def calculate_weekly_expenses(expenses: List[float]):
    total = sum(expenses)

    # Original Solutions
    # ===
    # total = 0

    # for expense in expenses:
    # total += expense
    # ===

    average_daily = round(total / len(expenses), 2)

    dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Not needed with the .index approach
    # max_value = 0

    max_idx = expenses.index(max(expenses))

    # Original Solution
    # ===
    # for idx, expense in enumerate(expenses):
    # if expense > max_value:
    # max_value = expense
    # max_idx = idx
    # ===

    return {
        "total_expenses": total,
        "average_daily_expense": average_daily,
        "highest_expense_day": dow[max_idx],
    }


if __name__ == "__main__":
    daily_expenses = [12.50, 8.75, 15.00, 10.00, 18.25, 9.50, 13.75]
    print(calculate_weekly_expenses(daily_expenses))
