import requests
from fastapi.testclient import TestClient
import main


def test_get_cat_facts():
    # check that get_cat_facts()'s response is successful
    resp = requests.get("https://catfact.ninja/facts")
    assert resp.raise_for_status() != requests.exceptions.HTTPError

    # check for a few keys in the response's data
    resp = resp.json()
    keys = list(resp.keys())
    assert "data" in keys
    assert "links" in keys
    assert "total" in keys

    # check that data of interest is formatted as expected
    data_keys = list(resp["data"][-1].keys())
    assert data_keys == ["fact", "length"]


def test_get_cat_breeds():
    # check that get_cat_breeds()'s response is successful
    resp = requests.get("https://catfact.ninja/breeds")
    assert resp.raise_for_status() != requests.exceptions.HTTPError

    # check for a few keys in the response's data
    resp = resp.json()
    keys = list(resp.keys())
    assert "data" in keys
    assert "links" in keys
    assert "total" in keys

    # check that data of interest is formatted as expected
    data_keys = list(resp["data"][-1].keys())
    assert data_keys == ["breed", "country", "origin", "coat", "pattern"]
