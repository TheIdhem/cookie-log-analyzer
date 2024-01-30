from datetime import datetime
import argparse
from exceptions import NonStandardInputFileError

def is_date(timestamp):
    try:
        datetime.fromisoformat(timestamp)
        return True
    except ValueError:
        return False

def is_file_standard(filename):
    with open(filename, 'r') as file:
        if file.read().strip() == "":
            raise NonStandardInputFileError()


def find_most_frequently_used_cookie(date, filename):
    is_file_standard(filename)

    cookie_frequencies = {}

    with open(filename, 'r') as file:
        for line in file:
            cookie, timestamp = line.strip().split(',')
            if not is_date(timestamp):
                continue
            timestamp = datetime.fromisoformat(timestamp)
            if cookie not in cookie_frequencies and timestamp.date().isoformat() == date:
                cookie_frequencies[cookie] = 1
            elif timestamp.date().isoformat() == date:
                cookie_frequencies[cookie] += 1
    
    if(cookie_frequencies):
        max_value = max(cookie_frequencies.values())
        return [cookie for cookie, frequencies in cookie_frequencies.items() if frequencies == max_value]
    else:
        print("Didn't find any frequent cookies.")
        raise NonStandardInputFileError()


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='Cooki file', required=True)
    parser.add_argument('-d', '--date', type=str, help='Date in the format yy-mm-dd', required=True)
    return parser.parse_args()


def print_cookies(cookies):
    for cookie in cookies:
        print(cookie)


if __name__ == '__main__':
    arguments = parse_argument()
    print_cookies(find_most_frequently_used_cookie(arguments.date, arguments.file))