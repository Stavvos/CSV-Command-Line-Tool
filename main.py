class Records:
	def __init__(self, firstname, lastname, date, division, points, summary):
		self.firstname = firstname
		self.lastname = lastname 
		self.date = date 
		self.division = int(division) 
		self.points = int(points)
		self.summary = summary
	
	def __str__(self):
		return '- name: {self.firstname} {self.lastname} \n  details: In division {self.division} from {self.date} performing {self.summary}'.format(self = self) 

test_object = Records("Liam", "Henry", "2021-11-24", 10, 76, "Programming") 
print (test_object) 