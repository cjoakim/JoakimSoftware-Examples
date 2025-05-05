#!/bin/bash

source venv/bin/activate


echo '========== 1 certifi.in =========='
pip-compile certifi.in

echo '========== 2 charset-normalizer.in =========='
pip-compile charset-normalizer.in

echo '========== 3 idna.in =========='
pip-compile idna.in

echo '========== 4 setuptools.in =========='
pip-compile setuptools.in

echo '========== 5 botocore.in =========='
pip-compile botocore.in

echo '========== 6 urllib3.in =========='
pip-compile urllib3.in

echo '========== 7 requests.in =========='
pip-compile requests.in

echo '========== 8 boto3.in =========='
pip-compile boto3.in

echo '========== 9 python-dateutil.in =========='
pip-compile python-dateutil.in

echo '========== 10 aiobotocore.in =========='
pip-compile aiobotocore.in

