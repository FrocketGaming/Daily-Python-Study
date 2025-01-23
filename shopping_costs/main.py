def calculate_total_cost(shopping_list: dict[str, int, float]) -> float:
    total_cost: int = 0
    for rows in shopping_list:
        total_cost += rows["quantity"] * rows["price_per_unit"]

    return round(total_cost, 2)


if __name__ == "__main__":
    shopping_list = [
        {"name": "Apple", "quantity": 4, "price_per_unit": 0.5},
        {"name": "Banana", "quantity": 6, "price_per_unit": 0.3},
        {"name": "Milk", "quantity": 1, "price_per_unit": 1.2},
    ]

    total_cost = calculate_total_cost(shopping_list)
