from server.test.integration import BaseTestCase


class HelloWorld(BaseTestCase):
    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})
