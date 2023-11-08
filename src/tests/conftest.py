import pytest
from fastapi.testclient import TestClient
from main import app
from settings import (
    app_settings as _app_settings,
    logging_settings as _logging_settings,
)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def app_settings():
    return _app_settings


@pytest.fixture
def logging_settings():
    return _logging_settings
