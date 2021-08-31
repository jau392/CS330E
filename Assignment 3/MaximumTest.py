from unittest import main, TestCase
from Maximum import maximum

class MyUnitTests(TestCase):
    def test_1(self):
        self.assertEqual(max([1, 2, 3]), 3)

    def test_2(self):
        self.assertEqual(max([-100, 1, 99]), 99)

    def test_3(self):
        self.assertEqual(max([1, 1, 1]), 1)

if __name__ == "__main__":
    main()
