from httpx import post

url_freight = "http://localhost:5000/api/fretes"

def test_post_freight_200():
    request = post(url_freight)
    assert request.status_code == 200

def test_post_freight_not_404():
    request = post(url_freight)
    assert request.status_code != 404

        