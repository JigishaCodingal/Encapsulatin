class myClass:

	# private variable
	__a = 27;

	# private method
	def __f1(self):
		print("I'm inside class myClass")

	# Function to print value of private variable
	def hello(self):
		print("Private Variable value: ",myClass.__a)
		self.__f1()

foo = myClass()
foo.hello()
#foo.__f1()