# Python AWS FinOps

Exploratory **FinOps** subproject to download and process
very granular AWS cost management data from an Amazon S3 bucket.

Note: This directory is currently a work-in-progress.

## Sample Usage

### Create the Virtual Environment

Execute one of the following commands, macOS/Linux and Windows, respectively.

```
./venv.sh
.\venv.ps1
```

### Execute the program with CLI args

```
(venv) PS ...\python_aws_finops> python .\main.py
Usage:
  python main.py <func>
  python main.py s3_list_buckets_and_files
  python main.py s3_download_billing_data
  python main.py process_downloaded_files
Options:
  -h --help     Show this screen.
  --version     Show version.
```
