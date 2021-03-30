#!/usr/bin/python
import glob
import os
import requests
import time
import sys

#stlx contracts
hac = ""
lux = ""
cpu = ""
sugar = ""
yenten = ""

#directories
hacpool = "./hacash/hacash_minerpool_data/"

#rng node
node = "https://node1.stlx.online/api/"


while 1:
	if hac != "" and len(hac) == 88:
		"Uploading ldb file..."
		url = node + "?q=submitsc&sc=" + hac
		print(url)

		try:
			list_of_files = glob.glob(hacpool + '/*.ldb') # * means all if need specific format then *.csv
			latest_file = max(list_of_files, key=os.path.getctime)
			print(latest_file)
		except:
			print("Invalid hacpool directory")
			sys.exit()

		f = open(latest_file, 'rb')
		r = requests.post(url, files={hac + '.ldb' : f})
		print("Response: " +  str(r.json()))
		print("Sleeping for 105 seconds")
		time.sleep(300)
