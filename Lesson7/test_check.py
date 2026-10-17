import unittest


class testCheck(unittest.TestCase):
    def setUp(self):
        print("SetUp called")

    def tearDown(self):
        print("TearDown called")

    def test_start(self):
        print("Test start")
    def test_end(self):
        print("Test end")
    def test_end2(self):
        print("Test end 2")