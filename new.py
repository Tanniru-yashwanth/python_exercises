class Name:
	def __init__(self, fn, domain):
		self.domain = None
		self.first_name = fn
		self.domain = domain

	@property
	def email(self):
		return f'{self.first_name}@{self.domain}.com'


inst = Name('test_name', 'google')
print(inst.first_name)
print(inst.email)
