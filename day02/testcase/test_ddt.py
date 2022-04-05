import pytest

from day01.my_requests import MyRequests
datas = [
    {"method":"post", "url": "http://api.lemonban.com/futureloan/member/register", "req_data":{"mobile_phone":"13429570008","pwd":"123456789","reg_name": "pytest01"}},
    {"method":"post", "url": "http://api.lemonban.com/futureloan/member/login", "req_data":{"mobile_phone":"13429570008","pwd":"123456789"}},
    {"method":"post", "url": "http://api.lemonban.com/futureloan/member/recharge", "req_data":{"member_id": None, "amount": 1000}}
]

#创建请求对象
mr = MyRequests()

@pytest.mark.parametrize("item",datas)
def test_api(item):
    resp = mr.send_requests(item["method"],item["url"],item["req_data"])
    print(resp.json())
    assert resp.json()["code"] == 0
