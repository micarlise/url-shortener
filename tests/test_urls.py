import pytest


def test_get_all_codes(client):
    assert client.get("/").status_code == 200