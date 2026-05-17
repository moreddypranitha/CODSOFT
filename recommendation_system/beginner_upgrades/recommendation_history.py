def save_history(item_name):

    with open(
        "saved_history/history.txt",
        "a"
    ) as file:

        file.write(item_name + "\n")