import unittest
from run import app


class RunTest(unittest.TestCase):

    # Check for response the error code
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

if __name__ == "__main__":
    unittest.main()