"""
Usage:
  python main.py <func>
  python main.py seed_from_15k_csv
  python main.py gen_pip_compiles_script
  python main.py get_pypi_html_pages
  python main.py parse_pypi_html_pages
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import base64
import json
import logging
import sys
import time
import os
import traceback

import duckdb 

from pprint import pprint

from docopt import docopt
from dotenv import load_dotenv

from six import moves 

from src.util.bytes import Bytes
from src.util.counter import Counter
from src.os.env import Env
from src.io.fs import FS
from src.os.system import System


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)

def seed_from_15k_csv():
    pass 

def gen_pip_compiles_script():
    pass 

def get_pypi_html_pages():
    pass 

def parse_pypi_html_pages():
    pass 


if __name__ == "__main__":
    try:
        func = sys.argv[1].lower()
        if func == "seed_from_15k_csv":
            seed_from_15k_csv()
        elif func == "gen_pip_compiles_script":
            gen_pip_compiles_script()
        elif func == "get_pypi_html_pages":
            get_pypi_html_pages()
        elif func == "parse_pypi_html_pages":
            parse_pypi_html_pages()
        else:
            print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
