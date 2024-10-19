import unittest
from unittest.mock import patch

import helpers


class TicTacToeGameTest (unittest.TestCase):

    @patch('builtins.input', side_effect=['2,2'])
    def testGetUserInput_with_valid_input(self, mock_input):
        # Test with valid input '2,2'
        result = helpers.get_user_input()
        self.assertEqual(result, (2, 2))

    @patch('builtins.input', side_effect=['4,4', '2,2'])
    def testGetUserInput_with_invalid_then_valid_input(self,mock_input):
        # First input is invalid ('4,4'), second input is valid ('2,2')
        result = helpers.get_user_input()
        self.assertEqual(result, (2, 2))

    @patch('builtins.input', side_effect=['abc', '1,3'])
    def testGetUserInput_with_invalid_non_numeric_then_valid_input(self,mock_input):
        # First input is invalid ('abc'), second input is valid ('1,3')
        result = helpers.get_user_input()
        self.assertEqual(result, (1, 3))

if __name__ == "__main__":
    unittest.main()
