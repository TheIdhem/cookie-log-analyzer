import unittest
from unittest.mock import mock_open, patch
from cookie_log_analyzer import find_most_frequently_used_cookie
from exceptions import NonStandardInputFileError

class TestCookieLogAnalyzer(unittest.TestCase):
    def test_most_active_cookie_with_single_output(self):
        cookie_log_data = [
            "cookie,timestamp\n",
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n",
        ]

        with patch("builtins.open", mock_open(read_data="".join(cookie_log_data))):
            result = find_most_frequently_used_cookie("2018-12-09", "fake_filename.csv")

        self.assertEqual(result, ["AtY0laUfhglK3lC7"])

    
    def test_most_active_cookie_with_double_output(self):
        cookie_log_data = [
            "cookie,timestamp\n",
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n",
        ]

        with patch("builtins.open", mock_open(read_data="".join(cookie_log_data))):
            result = find_most_frequently_used_cookie("2018-12-08", "fake_filename.csv")

        self.assertEqual(result, ["SAZuXPGUrfbcn5UA","4sMM2LxV07bPJzwf"])


    def test_input_file_is_empty(self):
        cookie_log_data = [
        ]

        with self.assertRaises(Exception) as context:
            with patch("builtins.open", mock_open(read_data="".join(cookie_log_data))):
                find_most_frequently_used_cookie("2018-12-08", "fake_filename.csv")

        exception = context.exception
        self.assertEqual(str(exception), str(NonStandardInputFileError()))
        
    
    def test_input_csv_file_is_empty(self):
        cookie_log_data = [
            "cookie,timestamp\n",
        ]

        with self.assertRaises(Exception) as context:
            print("2")
            with patch("builtins.open", mock_open(read_data="".join(cookie_log_data))):
                find_most_frequently_used_cookie("2018-12-08", "fake_filename.csv")

        exception = context.exception
        self.assertEqual(str(exception), str(NonStandardInputFileError()))
    

if __name__ == '__main__':
    unittest.main()

