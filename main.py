import os
import json
import query
import exploit


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_data_from_json(json_file_path):
    with open(json_file_path, "r") as file:
        return json.load(file)


def save_data_to_json(json_file_path, data):
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)


def paginate_data(data, page_size=10):
    return [data[i : i + page_size] for i in range(0, len(data), page_size)]


def get_user_input(prompt, valid_inputs):
    user_input = ""
    while user_input not in valid_inputs:
        user_input = input(prompt).strip().upper()
    return user_input


def print_pretty_table(header, rows):
    column_widths = [
        max(len(str(item)) for item in column) for column in zip(*rows, header)
    ]

    def print_separator():
        print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

    def print_row(items, is_header=False):
        row_str = "|".join(
            f" {item} ".ljust(width + 2) for item, width in zip(items, column_widths)
        )
        print(f"|{row_str}|")
        if is_header:
            print_separator()

    print_separator()
    print_row(header, is_header=True)
    for row in rows:
        print_row(row)
    print_separator()


def print_nothing_here():
    clear_screen()
    print(
        """
    +-------------------------------------+
    |                                     |
    |     Nothing here. Loading DATA?     |
    |                                     |
    +-------------------------------------+
    """
    )


def fetch_data_online(selected_table, selected_column):
    print(selected_table + ", " + selected_column)
    try:
        # Fetching data
        fetched_data = exploit.send_SQL(selected_column, selected_table)
        return fetched_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}


def main():
    json_file_path = "data_marge.json"
    data = load_data_from_json(json_file_path)

    while True:
        clear_screen()
        table_names = list(data.keys())
        print_pretty_table(
            ["Index", "Table Name"], list(enumerate(table_names, start=1))
        )
        user_input = get_user_input(
            "Select a table (index) or 'Q' to quit: ",
            [str(i) for i in range(1, len(table_names) + 1)] + ["Q"],
        )
        if user_input == "Q":
            break

        selected_table = table_names[int(user_input) - 1]
        columns = list(data[selected_table].keys() if selected_table in data else [])

        while True:
            clear_screen()
            if not columns:
                print_nothing_here()
                user_choice = (
                    input("Press 'G' to get data online, or any other key to go back: ")
                    .strip()
                    .upper()
                )
                if user_choice == "G":
                    # Simulate fetching data for each column
                    for column in columns:
                        fetched_data = fetch_data_online(selected_table, column)
                        data[selected_table][column] = list(fetched_data.values())
                    save_data_to_json(json_file_path, data)
                    data = load_data_from_json(json_file_path)  # Reload updated data
                    columns = list(data[selected_table].keys())
                continue
            print_pretty_table(
                ["Index", "Column Name"], list(enumerate(columns, start=1))
            )
            column_input = get_user_input(
                "Select a column (index), 'B' to go back, or 'Q' to quit: ",
                [str(i) for i in range(1, len(columns) + 1)] + ["B", "Q"],
            )
            if column_input == "B":
                break
            elif column_input == "Q":
                return

            selected_column = columns[int(column_input) - 1]
            column_data = (
                data[selected_table][selected_column]
                if selected_column in data[selected_table]
                else []
            )

            if not column_data:
                print_nothing_here()
                fetch_input = get_user_input(
                    "Press 'G' to fetch data online, or 'B' to go back: ", ["G", "B"]
                )
                if fetch_input == "G":
                    fetched_data = fetch_data_online(selected_table, selected_column)
                    data[selected_table][selected_column] = list(fetched_data.values())
                    save_data_to_json(json_file_path, data)
                    column_data = data[selected_table][selected_column]
                else:
                    continue

            # Pagination for column data
            data_pages = paginate_data(column_data)
            page_index = 0
            while page_index < len(data_pages):
                clear_screen()
                print_pretty_table(
                    ["Index", "Data"], list(enumerate(data_pages[page_index], start=1))
                )
                page_nav = get_user_input(
                    "Press 'N' for next, 'P' for previous, 'B' to go back: ",
                    ["N", "P", "B"],
                )
                if page_nav == "N" and page_index < len(data_pages) - 1:
                    page_index += 1
                elif page_nav == "P" and page_index > 0:
                    page_index -= 1
                elif page_nav == "B":
                    break


if __name__ == "__main__":
    cookies = input("쿠키 값을 입력하세요: ")
    query.set_cookies(cookies)

    main()
