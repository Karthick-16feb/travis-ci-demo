# test_script.py
import unittest
from script import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "YOO , PEOPLE !!! Travis CI Here !!!")

if __name__ == "__main__":
    unittest.main()
