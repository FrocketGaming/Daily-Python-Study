def remove_dupes(names):
    set_names = set(names)
    return list(set_names)


def sort_list(names):
    if isinstance(names, list):
        return sorted(names)
    return None


def main(names):
    refined_names = remove_dupes(names)
    sorted_names = sort_list(refined_names)
    return sorted_names


if __name__ == "__main__":
    guests = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
    results = main(guests)
