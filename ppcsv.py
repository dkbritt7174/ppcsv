#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""ppcsv.py Finds Primes Really Fast and stores them in primelist.csv."""

import sys
from datetime import datetime
import fastcsv
from pyprimesieve import primes

# Copyright 2020 David Kevin Britt
#
# dkbritt7174@gmail.com
# This file contains the PyPrimeSieve module.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.


__copyright__ = "Copyright (C) 1-10-2020 David Kevin Britt"
__license__ = "GPL"
__version__ = "3.1"
__maintainer__ = "David Kevin Britt"
__email__ = "dkbritt64118@gmail.com"
__status__ = "Beta"

DT = datetime.now()

def main() -> None:
    """Python ppcsv.py (n) and n is the upper limit."""


def testforinput():
    """If no input display example."""

    try:
        sys.argv[1]
    except IndexError:
        sys.exit(main.__doc__)



testforinput()
LIMIT_MAX = sys.argv[1]
CSVPRIME_LIST = primes(int(LIMIT_MAX))


def writetocsv():
    """ Writes the numbers to .csv file very quickly."""

    with open('PRIMELIST.csv', 'w', encoding='cp932') as file_iter:
        writer = fastcsv.Writer(file_iter)
        writer.writerow(CSVPRIME_LIST)
        writer.flush()

writetocsv()


print()
print(datetime.now() - DT, "Seconds")
