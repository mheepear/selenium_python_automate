import unittest

class TestSum(unittest.TestCase):

    def test_sum(self, fruits):
        fruits = [1, 2, 3, 4]
        self = [1, 2, 3]
            self.assertEqual(self, fruits, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (self, fruits))

    unittest.test_sum(self, fruits)