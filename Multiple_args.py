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
    
    def cases(self):
        ip_lists = []
        for arg in self.func.args_list:
            if arg[0] == "int" or arg[0] == "float":
                ip_lists.append(self.num_case(self.func))
            else:
                ip_lists.append(self.string_case())
        product = []       
        for item in itertools.product(*ip_lists):
	        product.append(item)
        
        cases_to_add = []
        for p in product:
            cases_to_add.append((("MultiArgs","Autotest",self.func,(p))))
        
        return cases_to_add

        
        

        

