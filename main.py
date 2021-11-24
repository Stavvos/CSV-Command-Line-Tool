#Written by Liam Henry 24/11/2021
import csv 

class Record:
	def __init__(self, firstname, lastname, date, division, points, summary):
		self.firstname = firstname
		self.lastname = lastname 
		self.date = date 
		self.division = int(division) 
		self.points = int(points)
		self.summary = summary
	
	#A function that formats the command line output of a Record object to the desired YAML formatting. 
	def __str__(self):
		return '- name: {self.firstname} {self.lastname} \n  details: In division {self.division} from {self.date} performing {self.summary}'.format(self = self) 

#A function that reads a CSV file, assigns values to Record object attributes,
#stores Record objects into an array, and returns the array filled with Record objects
def CSV(array):
	
	with open ('F:/CSV_Tool/CSV.txt') as CSVfile:  #Place file path of CSV.txt inbetween the parenthesis 
		reader = csv.reader(CSVfile, delimiter=',') 
			
		line_count = 0 
			
		for row in reader: 
			if line_count > 0: 
				array.append(Record(row[0],row[1],row[2],int(row[3]),int(row[4]),row[5])) 
				
			if line_count == 10:
				break
				
			line_count =+ 1
	#Note that the 'with' keyword handles closing the CSV file
	return array

#A function that sorts a given array's objects to the required ordering.  
def sortArray(array):
	array = sorted(array, key = lambda x: (x.division, -x.points))
	return array 

#A function that displays the top 3 indices within the given array. 
def display (array):
	for i in range(3):
		print (array[i])

array = [] #Create array
array = CSV(array) #Populate array with objects
array = sortArray(array) #Sort the array
display(array) #Display top 3 objects of the array 

