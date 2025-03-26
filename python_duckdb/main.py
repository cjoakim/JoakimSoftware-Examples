"""
Usage:
  python main.py <func>
  python main.py env
  python main.py duck1_csv
  python main.py duck2_imdb
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

from docopt import docopt
from dotenv import load_dotenv

from six import moves 

from src.io.fs import FS
from src.os.env import Env
from src.os.system import System


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def check_env():
    load_dotenv(override=True)
    for name in sorted(os.environ.keys()):
        if name.startswith("LOCAL_PG_"):
            print("{}: {}".format(name, os.environ[name]))
    print("check_env - username: {}".format(Env.username()))


def duck1_csv():
    data = duckdb.read_csv("data/postal_codes_nc.csv")
    print(data)
    print(str(type(data))) # <class 'duckdb.duckdb.DuckDBPyRelation'>


def duck2_imdb():
    data = duckdb.read_csv("https://datasets.imdbws.com/name.basics.tsv.gz")
    print(data)
    print(str(type(data))) # <class 'duckdb.duckdb.DuckDBPyRelation'>

    # name.basics.tsv.gz
    # title.akas.tsv.gz
    # title.basics.tsv.gz
    # title.crew.tsv.gz
    # title.episode.tsv.gz
    # title.principals.tsv.gz
    # title.ratings.tsv.gz

        
if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            func = sys.argv[1].lower()
            if func == "env":
                check_env()
            elif func == "duck1_csv":
                duck1_csv()
            elif func == "duck2_imdb":
                duck2_imdb()
            else:
                print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
