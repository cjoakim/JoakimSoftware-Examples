"""
Usage:
  python main.py <func>
  python main.py env
  python main.py duck1
  python main.py boto
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

import boto3

import duckdb 

from docopt import docopt
from dotenv import load_dotenv

from six import moves 

from src.util.bytes import Bytes
from src.util.counter import Counter
from src.os.env import Env
from src.io.fs import FS
from src.db.mongo_util import MongoUtil
from src.os.system import System


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def check_env():
    load_dotenv(override=True)
    Env.log_standard_env_vars()

    # for name in sorted(os.environ.keys()):
    #     if name.startswith("LOCAL_PG_"):
    #         print("{}: {}".format(name, os.environ[name]))

    print("check_env - username: {}".format(Env.username()))


def duck1():
    data = duckdb.read_csv("data/postal_codes_nc.csv")
    print(data)
    print(str(type(data))) # <class 'duckdb.duckdb.DuckDBPyRelation'>

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

def boto():
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html

    bucket_name = 'cjoakim-test1'

    # Create a boto3 client
    s3 = boto3.client('s3')

    response = s3.list_buckets()

    # Output the bucket names
    print('List of Buckets:')
    for bucket in response['Buckets']:
        print("bucket: {}".format(bucket["Name"]))

    print('Uploading:')
    with open("data/postal_codes_nc.csv", "rb") as f:
        s3.upload_fileobj(f, bucket_name, "postal_codes_nc.csv")

    print('Downloading:')   
    with open('tmp/postal_codes_nc.csv', 'wb') as f:
        s3.download_fileobj(bucket_name, 'postal_codes_nc.csv', f)

    response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=100)
    print(response)
    for c in response['Contents']:
        key, size = c['Key'], c['Size']
        print("key: {}  ({}) in {}".format(key, size, bucket_name))


def boto_old():
    # This seems to use the old 'boto3.resource' approach;
    # prefer the newer 'boto3.client' approach in the above boto3() method.

    bucket_name = 'cjoakim-test1'

    s3 = boto3.resource('s3')

    bucket = s3.Bucket(bucket_name)

    for b in s3.buckets.all():
        print("S3 bucket name: {}".format(b.name))

    # Upload a new file
    with open('requirements.txt', 'rb') as data:
        bucket.put_object(Key='requirements2.txt', Body=data)

    # List the contents of a bucket
    for bucket_object in bucket.objects.all():
        print("key: {} in bucket: {}".format(bucket_object.key, bucket_name))

    #s3.download_file(bucket_name, 'requirements2.txt', 'requirements2_downloaded.txt')
    client = boto3.client('s3')
    with open('requirements2.txt', 'wb') as f:
        client.download_fileobj(bucket_name, 'requirements2.txt', f)
        

if __name__ == "__main__":
    try:
        func = sys.argv[1].lower()
        if func == "env":
            check_env()
        elif func == "duck1":
            duck1()
        elif func == "boto":
            boto()
        else:
            print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
