if __name__ == "__main__":
    current_animals: dict[int] = {"lion": 5, "tiger": 3, "elephant": 2}

    while True:
        user_input: str = input("Enter an animal name: ").lower()
        try:
            int(user_input)
            print("Numbers are not valid, please try again")
        except Exception as e:
            break

    try:
        print(
            f"There are {current_animals[user_input]} {user_input.capitalize()}s in the zoo."
        )
    except KeyError:
        current_animals[user_input] = 1
        print(f"{user_input.capitalize()} added to the zoo with a count of 1.")
