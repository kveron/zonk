from unittest import TestCase
from counterofpoints import CounterOfPoints


class ZonkTestCase(TestCase):
    def test_max_points_is_4000(self):
        maximum = CounterOfPoints.max_points([1, 1, 1, 1, 1, 1])
        self.assertEqual(4000, maximum)

    def test_max_points_is_2400(self):
        maximum = CounterOfPoints.max_points([6, 6, 6, 6, 6, 6])
        self.assertEqual(2400, maximum)

    def test_max_points_is_750(self):
        maximum = CounterOfPoints.max_points([1, 1, 2, 2, 3, 3])
        self.assertEqual(750, maximum)

    def test_max_points_is_1500(self):
        maximum = CounterOfPoints.max_points([1, 2, 3, 4, 5, 6])
        self.assertEqual(1500, maximum)

    def test_max_points_is_150(self):
        maximum = CounterOfPoints.max_points([1, 2, 4, 5, 4, 3])
        self.assertEqual(150, maximum)

    def test_max_points_is_0(self):
        maximum = CounterOfPoints.max_points([2, 6, 6, 2, 4, 3])
        self.assertEqual(0, maximum)

    def test_max_points_is_100(self):
        maximum = CounterOfPoints.max_points([5, 5])
        self.assertEqual(100, maximum)

    def test_max_points_is_1200(self):
        maximum = CounterOfPoints.max_points([2, 2, 1, 2, 1, 1])
        self.assertEqual(1200, maximum)

    def test_max_points_is_1600(self):
        maximum = CounterOfPoints.max_points([5, 5, 5, 5, 5, 1])
        self.assertEqual(1600, maximum)

    def test_max_points_is_2050(self):
        maximum = CounterOfPoints.max_points([1, 1, 1, 1, 5, 3])
        self.assertEqual(2050, maximum)
