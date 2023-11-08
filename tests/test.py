import unittest
from celeryApp.celery_worker import calculate


class YourFlaskAppTests(unittest.TestCase):

    def test_hello_world(self):
        MOCK_DATA = [
            {'A': '1', 'O': '+', 'B': '2'},
            {'A': '3', 'O': '-', 'B': '4'},
            {'A': '2', 'O': '*', 'B': '5'}
        ]
        response = calculate(MOCK_DATA)
        self.assertEqual(response, 12)


if __name__ == '__main__':
    unittest.main()
