"""
Usage:
  python main.py <func>
  python main.py seed_from_15k_csv 10
  python main.py gen_pip_compiles_script
  python main.py parse_pip_compiles 1
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

#from six import moves 

from src.util.bytes import Bytes
from src.util.counter import Counter
from src.os.env import Env
from src.io.fs import FS
from src.os.system import System
from src.util.requirements import Libraries, RequirementsTxtParser


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)

def seed_from_15k_csv(first_n):
    libs = FS.read_csv_as_dicts("data/csv/top-pypi-packages.csv")
    for idx, lib in enumerate(libs):
        if idx < first_n:
            #print("{} {}".format(idx, lib))
            libname = lib['project']
            content = "{}".format(libname).strip()
            outfile = "data/pip/{}.in".format(libname)
            FS.write(content, outfile)

def gen_pip_compiles_script():
    script_lines = list()
    script_lines.append("#!/bin/bash")
    script_lines.append("")
    script_lines.append("source venv/bin/activate")
    script_lines.append("")
    files = FS.list_files_in_dir("data/pip")
    filenum = 0
    for f in files:
        if f.endswith(".in"):
            filenum = filenum + 1
            script_lines.append("")
            script_lines.append("echo '========== {} {} =========='".format(filenum, f))
            script_lines.append("pip-compile {}".format(f))
    script_lines.append("")
    FS.write_lines(script_lines, "data/pip/pip_compiles.sh")

def parse_pip_compiles():
    pip_filenames_dict = dict()
    files = FS.list_files_in_dir("data/pip")

    # first get a list of all the *.in, *.txt, and *.json files in the pip 
    # directory to determine which files need to be parsed.
    for f in files:
        stripped = f.strip()
        if is_pip_processing_file(stripped):
            pip_filenames_dict[stripped] = False
    print("{} files in pip_filenames_dict".format(len(pip_filenames_dict)))

    # second loop, the parsing loop, parse a file if not yet parsed
    for f in files:
        filename = f.strip()
        if filename.endswith(".txt"):  # the output of a pip-compile
            libname = filename.split(".")[0]
            jsonfile = "{}.json".format(libname)
            if jsonfile in pip_filenames_dict.keys():
                print("already parsed: {}".format(filename))
            else:
                if "boto3.txt" in filename:
                    outfile = "data/pip/{}".format(jsonfile)
                    print("===")
                    print("parsing: {}".format(filename))
                    rtp = RequirementsTxtParser()
                    results = rtp.parse(filename)
                    #print(json.dumps(results, sort_keys=False, indent=2))
                    FS.write_json(results, outfile, sort_keys=False)

def is_pip_processing_file(filename):
    if filename.endswith(".in"):
        return True
    if filename.endswith(".txt"):
        return True
    if filename.endswith(".json"):
        return True
    return False 

def get_pypi_html_pages():
    pass 

def parse_pypi_html_pages():
    pass 



if __name__ == "__main__":
    try:
        func = sys.argv[1].lower()
        if func == "seed_from_15k_csv":
            first_n = int(sys.argv[2])
            seed_from_15k_csv(first_n)
        elif func == "gen_pip_compiles_script":
            gen_pip_compiles_script()
        elif func == "parse_pip_compiles":
            parse_pip_compiles()
        elif func == "get_pypi_html_pages":
            get_pypi_html_pages()
        elif func == "parse_pypi_html_pages":
            parse_pypi_html_pages()
        else:
            print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
