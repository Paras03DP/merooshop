import unittest
from run import app


class AddProductTest(unittest.TestCase):

    # Check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertEqual(response.content_type, "application/json")

if __name__ == "__main__":
    unittest.main()