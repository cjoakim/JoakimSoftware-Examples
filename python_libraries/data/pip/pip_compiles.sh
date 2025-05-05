#!/bin/bash

source venv/bin/activate

pip-compile certifi.in
pip-compile charset-normalizer.in
pip-compile idna.in
pip-compile setuptools.in
pip-compile botocore.in
pip-compile urllib3.in
pip-compile requests.in
pip-compile boto3.in
pip-compile python-dateutil.in
pip-compile aiobotocore.in

