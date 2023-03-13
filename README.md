# ShellPride 🏳️‍🌈 :transgender_flag:
[![PyPI version](https://img.shields.io/pypi/v/ShellPride.svg)](https://pypi.org/project/ShellPride/)
[![License](https://img.shields.io/pypi/l/ShellPride.svg)](https://github.com/ccmorenos/ShellPride/blob/main/LICENSE)
[![Test Python Package](https://github.com/ccmorenos/ShellPride/actions/workflows/test-python.yml/badge.svg?branch=main)](https://github.com/ccmorenos/ShellPride/actions/workflows/test-python.yml) [![Upload Python Package](https://github.com/ccmorenos/ShellPride/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ccmorenos/ShellPride/actions/workflows/python-publish.yml)

Shell scripts of pride flags to decorate the console.

## Installation

### From command

The package is available in the
[Python Package Index (PyPi)](https://pypi.org/project/ShellPride/).

```bash
python3 -m pip install ShellPride
```

## Usage

To use the decorator, run.

```shell
pridesh [-h] -f FLAGS [FLAGS ...] [-L LENGTH] [-d DECORATOR] [-n NAME]
        [-p PRONOUNS] [-zs ZODIAC_SOLAR] [-za ZODIAC_ASCENDANT]
        [-zm ZODIAC_MOON]
```

Where:

* `-h, --help`: Show the help message and exit.

* `-f FLAGS [FLAGS ...], --flags FLAGS [FLAGS ...]`: Configure the flags to be
  shown.

* `-L LENGTH, --length LENGTH`: Length of the flags.

* `-lf, --list_flags`: List all the posible flags and exit.

* `-d DECORATOR, --decorator DECORATOR`: Add the color for the decorator
letters.

* `-n NAME, --name NAME`: Add your name.

* `-p PRONOUNS, --pronouns PRONOUNS`: Add your pronouns.

* `-zs ZODIAC_SOLAR, --zodiac_solar ZODIAC_SOLAR`: Add your solar zodiac sign.

* `-za ZODIAC_ASCENDANT, --zodiac_ascendant ZODIAC_ASCENDANT`: Add your
  ascendant zodiac sign.

* `-zm ZODIAC_MOON, --zodiac_moon ZODIAC_MOON`: Add your moon zodiac sign.
