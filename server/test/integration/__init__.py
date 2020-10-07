from unittest import TestCase

from fastapi.testclient import TestClient

from server import app


class BaseTestCase(TestCase):
    client = TestClient(app)
