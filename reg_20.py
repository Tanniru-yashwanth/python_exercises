"""20.	How would you write a regex that matches a number with commas for every three digits?
It must match the following:
 	142'
 	'1,234'
 	'6,368, 745 '
 	but not the following:
 12, 34, 567' (which has only two digits between the commas)
 	' 1234' (which lacks commas)
"""
A: regex_object = re.compile(r'\d{3}+,\d{3}+,\d{3}+')
