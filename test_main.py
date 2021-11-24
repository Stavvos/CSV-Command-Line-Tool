import unittest
from main import CSV
from main import Records
from main import sortArray
test_array = []

#A test to verify the CSV function has added objects of the type Records into the array
class Test_main_Functions(unittest.TestCase):	
	def test_CSV(self): 
		CSV(test_array)
		for i in range(len(test_array)):
			self.assertIsInstance(test_array[i], Records)
	
#A test to verify the array of objects is in the correct order
	def test_sortArray(self): 
		expected_array = sorted(test_array, key = lambda x: (x.division, -x.points))
		self.assertEqual(sortArray(test_array), expected_array) 