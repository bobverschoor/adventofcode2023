import unittest

from dag1.deel1 import CalibrationDocument


class MyTestCase(unittest.TestCase):
    def test_calibrationvalue1(self):
        cd = CalibrationDocument()
        cd._lines = ["1abc2",
                     "pqr3stu8vwx",
                     "a1b2c3d4e5f",
                     "treb7uchet"]
        self.assertEqual(cd.get_calibration_value(cd._lines[0]), 12)  # add assertion here
        self.assertEqual(cd.get_calibration_value(cd._lines[1]), 38)
        self.assertEqual(cd.get_calibration_value(cd._lines[2]), 15)
        self.assertEqual(cd.get_calibration_value(cd._lines[3]), 77)
        self.assertEqual(cd.sum_calibration_values(), 142)

    def test_calibrationvalues_literal(self):
        cd = CalibrationDocument()
        cd._lines = ["two1nine",
                     "eightwothree",
                     "abcone2threexyz",
                     "xtwone3four",
                     "4nineeightseven2",
                     "zoneight234",
                     "7pqrstsixteen"]
        self.assertEqual(29, cd.get_calibration_value_literal(cd._lines[0]))
        self.assertEqual(83, cd.get_calibration_value_literal(cd._lines[1]))
        self.assertEqual(13, cd.get_calibration_value_literal(cd._lines[2]))
        self.assertEqual(24, cd.get_calibration_value_literal(cd._lines[3]))
        self.assertEqual(42, cd.get_calibration_value_literal(cd._lines[4]))
        self.assertEqual(14, cd.get_calibration_value_literal(cd._lines[5]))
        self.assertEqual(76, cd.get_calibration_value_literal(cd._lines[6]))
        self.assertEqual(cd.sum_calibration_values_literal(), 281)

if __name__ == '__main__':
    unittest.main()
