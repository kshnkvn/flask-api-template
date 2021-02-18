import pytest
from flask import Flask

from app import create_app
from config import DevConfig


@pytest.fixture
def app():
    yield create_app(DevConfig)


@pytest.fixture
def client(app: Flask):
    return app.test_client()
