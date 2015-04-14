import csv
import os

def ReadCSVasList(csv_file):
	try:
		with open(csv_file) as csvfile:
		    reader = csv.reader(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
		    datalist = []
		    datalist = list(reader)
		    return datalist
	except IOError as (errno, strerror):
	        print("I/O error({0}): {1}".format(errno, strerror)) 	
	return

def WriteListToCSV(csv_file,csv_columns,data_list):
	try:
		with open(csv_file, 'w') as csvfile:
		    writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
		    writer.writerow(csv_columns)
		    for data in data_list:
		    	writer.writerow(data)
	except IOError as (errno, strerror):
	        print("I/O error({0}): {1}".format(errno, strerror)) 	
	return  	        

csv_columns = ['Row','Name','Country']

currentPath = os.getcwd()
csv_file = currentPath + "/csv/Names.csv"

csv_data_list = ReadCSVasList(csv_file)
print csv_data_list

# To Ignore 1st Row (Headers)          
csv_data_list.pop(0)
print csv_data_list

# append to list
csv_data_list.append(['6', 'Suresh', 'India'])

print csv_data_list


WriteListToCSV(csv_file,csv_columns,csv_data_list)

  