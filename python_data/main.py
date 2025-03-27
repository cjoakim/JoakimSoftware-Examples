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
import urllib.parse

import duckdb
import httpx

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
    infile = "../data/cars/all_car_makes.json"
    all_car_makes = FS.read_json(infile)
    for idx, make in enumerate(all_car_makes):
        print("{}: {}".format(idx, make))
        download_models_for_make(make)

        #r = httpx.get('https://www.example.org/')
        # >>> r.status_code
        # 200
        # >>> r.headers['content-type']
        # 'text/html; charset=UTF-8'
        # >>> r.text

def download_models_for_make(make):
    url_template = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/all-vehicles-model/records?select=make%2C%20model%2C%20city08u%2C%20highway08u%2C%20comb08u%2C%20cylinders%2C%20displ%2C%20drive%2C%20eng_dscr%2C%20fueltype1%2C%20id%2C%20trany%2C%20vclass%2C%20year%2C%20mfrcode%2C%20basemodel&where=make%20%3D%20%22{}%22&order_by=make%2C%20model%2C%20year&limit={}&offset={}"
    continue_to_process, limit, offset, seq = True, 100, -100, 0
    encoded_make = urllib.parse.quote(make)
    print("MAKE: {}  encoded: {}".format(make, encoded_make))

    while continue_to_process:
        seq = seq + 1
        if seq > 100:
            continue_to_process = False
        else:
            try:
                offset = offset + limit
                url = url_template.format(encoded_make, limit, offset)
                print("URL: {}".format(url))
                outfile = "tmp/{}-{}.json".format(make.replace(" ", "_"), seq)
                time.sleep(1)
                resp = httpx.get(url)
                if resp.status_code == 200:
                    obj = json.loads(resp.text)
                    results = obj["results"]
                    if len(results) < 1:
                        continue_to_process = False
                    else:
                        FS.write_json(results, outfile)
            except Exception as e:
                continue_to_process = False
                logging.critical(str(e))
                print(traceback.format_exc())


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
