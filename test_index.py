import unittest
from run import app


class IndexTest(unittest.TestCase):

    # Check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

if __name__ == "__main__":
    unittest.main()