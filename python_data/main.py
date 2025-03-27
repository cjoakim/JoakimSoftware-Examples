"""
Usage:
  python main.py <func>
  python main.py merge_car_makes
  python main.py download_cars_data
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


def merge_car_makes():
    infiles = [ "../data/cars/makes1.json", "../data/cars/makes2.json" ]
    all_car_makes = dict()
    for infile in infiles:
        data = FS.read_json(infile)
        results = data["results"]
        for result in results:
            make = result["make"]
            all_car_makes[make] = 1
    FS.write_json(all_car_makes, "tmp/all_car_makes.json")

def download_cars_data():
    pass

        
if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            func = sys.argv[1].lower()
            if func == "env":
                check_env()
            elif func == "merge_car_makes":
                merge_car_makes()
            elif func == "download_cars_data":
                download_cars_data()
            else:
                print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
