# Cookie Log Analyzer

Cookie Log Analyzer is a command-line program written in Python that processes a log file containing cookie data and identifies the most active cookie(s) for a specific day.

## Usage

### Prerequisites

- Python 3.11 installed on your machine

### Installation

No installation is required. Just clone the repository to your local machine:

```bash
git clone https://github.com/TheIdhem/cookie-log-analyzer.git
cd cookie-log-analyzer
```

### Running the Program

```bash
python cookie_log_analyzer.py -f <filename> -d <yyyy-mm-dd>
```

#### Example:

```bash
python cookie_log_analyzer.py -f cookie_log.csv -d 2018-12-09
```

#### Output

The program will print the most active cookie(s) for the specified date to the console.

### Run tests

```bash
python3 -m unittest
```

### Assumptions

- The -d parameter takes the date in the UTC time zone.
- The cookie log file is sorted by timestamp.

## Contact

Mehdi Fallahi - [@the_idhem](https://twitter.com/the_idhem) - mehdi.fallahi.moh@gmail.com
