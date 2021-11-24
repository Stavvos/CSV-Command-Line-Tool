import csv 

class Records:
	def __init__(self, firstname, lastname, date, division, points, summary):
		self.firstname = firstname
		self.lastname = lastname 
		self.date = date 
		self.division = int(division) 
		self.points = int(points)
		self.summary = summary
	
	#A function that formats the output of a Records object to the desired YAML formatting. 
	def __str__(self):
		return '- name: {self.firstname} {self.lastname} \n  details: In division {self.division} from {self.date} performing {self.summary}'.format(self = self) 

#A function that reads a CSV file, Assigns values to Records object attributes,
#stores Records objects into an array, and returns the array filled with Records objects
def CSV(array):
	
	with open ('F:/CSV_Tool/CSV.txt') as CSVfile:  #place file path of CSV.txt inbetween the parenthesis 
		reader = csv.reader(CSVfile, delimiter=',') 
			
		line_count = 0 
			
		for row in reader: 
			if line_count > 0:
				array.append(Records(row[0],row[1],row[2],int(row[3]),int(row[4]),row[5])) 
				
			if line_count == 10:
				break
				
			line_count =+ 1
	#note that the 'with' keyword handles closing the CSV file
	return array

array = []
array = CSV(array)
print(array[0])