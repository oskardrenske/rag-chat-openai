import unittest

from src.user_input_formatter import input_formatter


class UserInputFormatterTestCase(unittest.TestCase):
    def test_single_quote(self):
        user_input = "'quit'"
        formatted_input = input_formatter(user_input)
        self.assertEqual(formatted_input, "quit")

    def test_double_quote(self):
        user_input = '"quit"'
        formatted_input = input_formatter(user_input)
        self.assertEqual(formatted_input, "quit")

    def test_length(self):
        # This is too long to be a command and should not be formatted
        user_input = "longerThan7'Characters"
        formatted_input = input_formatter(user_input)
        self.assertEqual(formatted_input, user_input)

    def test_multiple_words(self):
        # multiple words is not a command
        user_input = "quit c"
        formatted_input = input_formatter(user_input)
        self.assertEqual(formatted_input, user_input)


if __name__ == "__main__":
    unittest.main()
