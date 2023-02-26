import sys #needed setting command line parameters
import sensors_main
import unittest
from unittest.mock import patch

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.

    # Placeholder for the test case test_check_limits3. To be designed
    # and implemented. 

    def test_how_many_lines_in_read_sensors(self):
        result = len(sensors_main.read_sensors())
        self.assertEqual(result, 24)

# ******************** Integration test***************

# Redirect console output to sys.stdout in order
# check its content from the 
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        # set commandline parameters for the test case
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main from sensors_main.py
        sensors_main.main()

        # check that the console output is expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")


if __name__ == '__main__':
    unittest.main()