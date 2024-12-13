import requests
import json


def read_urls_from_file(filename):
    with open(filename, 'r') as file:
        urls = file.read().splitlines()
    return urls


def send_indexnow_request():
    url = "https://api.indexnow.org/IndexNow"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.indexnow.org"
    }
    data = {
        "host": "c-lby.top",
        "key": "c62d4bb3f732430e93c190aba39592cc",
        "keyLocation": "https://c-lby.top/c62d4bb3f732430e93c190aba39592cc.txt",
        "urlList": read_urls_from_file('sitemap.txt')
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # if response.status_code == 200:
    #     print('Success:', response.json())
    # else:
    #     print('Failed:', response.status_code, response.text)


# 调用函数发送请求
send_indexnow_request()
# print(read_urls_from_file('sitemap.txt'))
