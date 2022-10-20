import requests

_headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    # 有些视频需要购买才能观看，登录CCTalk后，把cookies复制到这里
    # 解除权限的限制
    "cookie": ""
}


def get(url, params=None):
    return requests.get(headers=_headers, url=url, params=params)


def decode_response(response):
    return response.content.decode()
