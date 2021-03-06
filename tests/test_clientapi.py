import os
import unittest
from helloworld import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/status')
    assert response.data == b'ok'

def test_clienthello( client):
    response = client.get('/api/v1/hello')
    assert response.data == b'Hi'
