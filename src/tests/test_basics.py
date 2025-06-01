#!/usr/bin/env python

from fastapi.testclient import TestClient
import sys
sys.path.append('.')
from src.main import fruitapi

client = TestClient(fruitapi)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
 
def test_get_count_0():
    response = client.get("/fruit/count")
    assert response.status_code == 200, "Expecting HTTP response code 200, got: {}".format(response.status_code)
    assert int(response.json()) == 0, "Expecting fruit count = 0, got : {}".format(int(response.json()))
 
def test_get_nonexistant_id():
    response = client.get("/fruit/8432")
    assert response.status_code == 400, "Expecting HTTP response code 400, got: {}".format(response.status_code)

def test_add_fruit_1():
    response = client.post(
        "/fruit",
        json={"fruit": "apple", "color": "red", "fruit_id": 25}
    )
    assert response.status_code == 200, "Expecting HTTP response code 200, got: {}".format(response.status_code)

def test_add_fruit_2():
    response = client.post(
        "/fruit",
        json={"fruit": "banana", "color": "yellow", "fruit_id": 771}
    )
    assert response.status_code == 200, "Expecting HTTP response code 200, got: {}".format(response.status_code)

def test_get_fruit_1():
    response = client.get("/fruit/25")
    assert response.status_code == 200, "Expecting HTTP response code 200, got: {}".format(response.status_code)
    assert response.json() == {"fruit": "apple", "color": "red", "fruit_id": 25}, "Expecting JSON response with different content, got : {}".format(response.json())

def test_get_fruit_all():
    response = client.get("/fruit/all")
    assert response.status_code == 200, "Expecting HTTP response code 200, got: {}".format(response.status_code)
    assert response.json() == [{'fruit_id': 25, 'fruit': 'apple', 'color': 'red'}, {'fruit_id': 771, 'fruit': 'banana', 'color': 'yellow'}], "Expecting JSON response with different content, got : {}".format(response.json())

def test_delete_fruit():
    response = client.delete("/fruit/25")
    assert response.status_code == 200, "Expecting HTTP response code 200, got: {}".format(response.status_code)

def test_get_fruit_2():
    response = client.get("/fruit/25")
    assert response.status_code == 400, "Expecting HTTP response code 400, got: {}".format(response.status_code)
