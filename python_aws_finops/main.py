"""
Usage:
  python main.py <func>
  python main.py s3_list_buckets_and_files
  python main.py s3_download_billing_data
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import json
import logging
import sys
import time
import os
import traceback
import urllib.parse

import boto3
import duckdb
import httpx

from docopt import docopt
from dotenv import load_dotenv
#from six import moves 

from src.io.fs import FS
from src.os.env import Env
from src.os.system import System

BILLING_PERIOD_LIT = "BILLING_PERIOD"

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)

def s3_items_filename():
    return "tmp/s3_items.json" 

def s3_list_buckets_and_files():
    try:
        s3_items_list = list()
        s3 = boto3.client('s3')
        bucket_response = s3.list_buckets()  # response is a dict
        for bucket in bucket_response['Buckets']:
            bucket_name = bucket["Name"]
            list_response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1000)
            #print(list_response)
            max_keys = list_response["MaxKeys"]
            key_count = list_response["KeyCount"]
            print("bucket_name: {}, key_count: {}, max_keys: {}".format(
                bucket_name, key_count, max_keys))
            for item in list_response['Contents']:
                #print(item)
                item_doc = dict()
                item_doc["bucket_name"] = bucket_name
                item_doc["key"] = item['Key']
                item_doc["size"] = item['Size']
                item_doc["last_mod"] = str(item['LastModified'])
                item_doc["etag"] = item['ETag'].replace('"','')
                item_doc["download_basename"] = s3_key_to_basename(item['Key'])
                s3_items_list.append(item_doc)
        FS.write_json(s3_items_list, s3_items_filename(), sort_keys=False)
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())

def s3_download_billing_data():
    try:
        s3_items_list = FS.read_json(s3_items_filename())
        billing_bucket = os.environ["AWS_BILLING_BUCKET"]
        billing_item_prefix = os.environ["AWS_BILLING_ITEM_PREFIX"]
        do_downloads = True
        
        print("billing_bucket: {}".format(billing_bucket))
        s3 = boto3.client('s3')
        for idx, item in enumerate(s3_items_list):
            if item['bucket_name'] == billing_bucket:
                key = item["key"]
                filetype = key.split(".")[-1]
                if key.startswith(billing_item_prefix):
                    print("===")
                    bucket_name = item["bucket_name"]
                    outfile = "tmp/{}".format(s3_key_to_basename(key))
                    print(outfile)
                    if do_downloads:
                        try:
                            with open(outfile, 'wb') as f:
                                s3.download_fileobj(bucket_name, key, f)
                                print("downloaded: {} {} -> {}".format(
                                    bucket_name, key, outfile))
                        except Exception as e2:
                            print(str(e2))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())

def s3_key_to_basename(key):
    if key is not None:
        try:
            if BILLING_PERIOD_LIT in key:
                start_idx = key.index(BILLING_PERIOD_LIT) + len(BILLING_PERIOD_LIT) + 1
                rest = key[start_idx:]
                rest = rest.replace("/","--")
                rest = rest.replace("=", "-")
                rest = rest.replace(":", "")
                return rest.strip()
            else:
                return key.replace("/","--").strip()
        except Exception as e:
            print(str(e))
            return None
    else:
        return None

if __name__ == "__main__":
    try:
        load_dotenv(override=True)
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            func = sys.argv[1].lower()
            if func == "s3_list_buckets_and_files":
                s3_list_buckets_and_files()
            elif func == "s3_download_billing_data":
                s3_download_billing_data()
            else:
                print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
