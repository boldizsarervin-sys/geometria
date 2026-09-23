import unittest
import math
from geometria_orokles import Negyzet, Teglalap, Kor

class TestNegyzet(unittest.TestCase):

    def test_terulet(self):
        n = Negyzet(5)
        self.assertEqual(n.terulet(), 25)

    def test_kerulet(self):
        n = Negyzet(5)
        self.assertEqual(n.kerulet(), 20)

class TestTeglalap(unittest.TestCase):

    def test_terulet(self):
        t = Teglalap(3, 4)
        self.assertEqual(t.terulet(), 12)

    def test_kerulet(self):
        t = Teglalap(3, 4)
        self.assertEqual(t.kerulet(), 14)

class TestKor(unittest.TestCase):

    def test_terulet(self):
        k = Kor(5)
        self.assertAlmostEqual(k.terulet(), math.pi * 25, places=2)

    def test_kerulet(self):
        k = Kor(5)
        self.assertAlmostEqual(k.kerulet(), math.pi * 10, places=2)

if __name__ == "__main__":
    unittest.main()

    