import csv
import os

def ReadCSVasDict(csv_file):
	try:
		with open(csv_file) as csvfile:
		    reader = csv.DictReader(csvfile)
		    for row in reader:
		    	print row['Row'], row['Name'], row['Country']
	except IOError as (errno, strerror):
	        print("I/O error({0}): {1}".format(errno, strerror)) 	
	return

def WriteDictToCSV(csv_file,csv_columns,dict_data):
	try:
		with open(csv_file, 'w') as csvfile:
		    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
		    writer.writeheader()
		    for data in dict_data:
		    	writer.writerow(data)
	except IOError as (errno, strerror):
	        print("I/O error({0}): {1}".format(errno, strerror)) 	
	return            

csv_columns = ['Row','Name','Country']
dict_data = [
	{'Row': 1, 'Name': 'Alex', 'Country': 'India'},
	{'Row': 2, 'Name': 'Ben', 'Country': 'USA'},
	{'Row': 3, 'Name': 'Shri Ram', 'Country': 'India'},
	{'Row': 4, 'Name': 'Smith', 'Country': 'USA'},
	{'Row': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    ]

currentPath = os.getcwd()
csv_file = currentPath + "/csv/Names.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)

ReadCSVasDict(csv_file)

  