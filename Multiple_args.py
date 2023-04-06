import re
import string
import random
import itertools

TOKENS = [':','\(','\)','/','{','}','<','>','==','<=','>=','\s']
TOKEN_SPLITTER = "|".join(TOKENS)

class Multiple_args:
	def __init__(self,func):
		self.func = func
	
	def num_case(self,func):
		nums = []
		conditions = []
		loops = []
		switches = []
		lines = func.content.split(';')
		for idx in range(len(lines)):
			if 'if' in lines[idx]:
				conditions.append(lines[idx])
			if 'for' in lines[idx]:
				loops.append(lines[idx])
			if 'while' in lines[idx]:
				loops.append(lines[idx])
			if 'case' in lines[idx]:
				switches.append(lines[idx])
		for i in conditions:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and j.isdigit() and (i.index('if') < i.index(j)):
					nums.append(int(j)-1)
					nums.append(int(j))
					nums.append(int(j)+1)
		for i in loops:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and j.isdigit():
					nums.append(int(j)-1)
					nums.append(int(j))
					nums.append(int(j)+1)
		
		for i in switches:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and j.isdigit():
					nums.append(int(j))

		nums.append(random.randint(0,100))
		nums.append(random.randint(-1*100,0))
		nums.append(0)
		nums = list(set(nums))
		return nums

	def string_case(self):
		strs = []
		ip_string = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5,10)))
		strs.append(ip_string)
		ip_string = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))
		strs.append(ip_string)
		ip_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5,10)))
		strs.append(ip_string)
		return strs

	def char_case(self,func):
		chars = []
		conditions = []
		lines = func.content.split(';')
		for idx in range(len(lines)):
			if 'if' in lines[idx]:
				conditions.append(lines[idx])
		for i in conditions:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and (i.index('if') < i.index(j)) and re.match("'.'",j) and not j.isdigit():
					j = j.strip("'")
					chars.append(j)
					chars.append(chr(ord(j)-1))
					chars.append(chr(ord(j)+1))
		chars.append(chr(random.randint(97,122)))
		chars = list(set(chars))
		return chars
		
		
	def float_case(self,func):
		def is_float(string):
			try:
				float(string)
				return True
			except ValueError:
				return False
		
		floats = []
		conditions = []
		loops = []
		switches = []
		lines = func.content.split(';')
		for idx in range(len(lines)):
			if 'if' in lines[idx]:
				conditions.append(lines[idx])
			if 'for' in lines[idx]:
				loops.append(lines[idx])
			if 'while' in lines[idx]:
				loops.append(lines[idx])
			if 'case' in lines[idx]:
				switches.append(lines[idx])
		for i in conditions:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and is_float(j) and (i.index('if') < i.index(j)):
					floats.append(float(j)-random.random())
					floats.append(float(j))
					floats.append(float(j)+random.random())
		for i in loops:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and is_float(j):
					floats.append(float(j)-random.random())
					floats.append(float(j))
					floats.append(float(j)+random.random())
		
		for i in switches:
			for j in re.split(TOKEN_SPLITTER,i):
				if j and is_float(j):
					floats.append(float(j))

		floats.append(random.random()*100)
		floats.append(random.random()*-100)
		floats.append(0.0)
		floats = list(set(floats))
		return floats
	
	def cases(self):
		ip_lists = []
		for arg in self.func.args_list:
			if arg[0] == "int":
				ip_lists.append(self.num_case(self.func))
			elif arg[0].lower() == "string":
				ip_lists.append(self.string_case())
			elif arg[0] == "char":
				ip_lists.append(self.char_case(self.func))
			elif arg[0].lower() == "float":
				ip_lists.append(self.float_case(self.func))
			else:
				ip_lists.append([" "])


		product = []       
		for item in itertools.product(*ip_lists):
			product.append(item)
		
		cases_to_add = []
		i=0
		for p in product:
			i+=1
			cases_to_add.append((("MultiArgs",f"Autotest_{i}",self.func,p)))
		
		return cases_to_add