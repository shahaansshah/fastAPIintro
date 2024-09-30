import requests
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


# check that the homepage returns a successful status code
def test_app():
    resp = client.get("/")
    assert resp.raise_for_status() != requests.exceptions.HTTPError


# check that "/facts" works as it should
def test_get_cat_facts():

    resp = client.get("/facts")

    # check that get_cat_facts()'s response is successful
    assert resp.raise_for_status() != requests.exceptions.HTTPError

    # check that the "data" portion is returning a cat fact
    resp = resp.json()
    assert list(resp.keys()) == ["fact"]


# check that "/breeds works as it should"
def test_get_cat_breeds():

    resp = client.get("/breeds")

    # check that get_cat_breeds()'s response is successful
    assert resp.raise_for_status() != requests.exceptions.HTTPError

    # check that the "data" portion is returning a cat fact
    resp = resp.json()
    assert list(resp.keys()) == ["breed"]
