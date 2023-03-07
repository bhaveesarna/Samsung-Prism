from Test_Model import *
from Parse import *
import random
import os
buildpath = "build."
if os.name == 'nt':
    buildpath = buildpath+"Release."
import importlib
import config
for file in config.file_list:
    mod = importlib.__import__(buildpath+os.path.splitext(file)[0], globals=globals(), locals=locals(), fromlist="*")
    globals()[os.path.splitext(file)[0]] = mod
    del mod
print(globals().keys())
import string
import re

TOKENS = [':','\(','\)','/','{','}','<','>','==','<=','>=','\s']
TOKEN_SPLITTER = "|".join(TOKENS)





def checkDuplicate(cases_to_add,func,j):
    for case in cases_to_add:
        if case[2].name == func.name and int(case[3])== int(j):
            return False
    return True

def predictCaseVals(func:function):
    cases_to_add = []
    if "int" in func.args or "float" in func.args:
        # if len(func.args["int"]) > 1:
        #     for i in func.content:
        #         if  i.isdigit():
        #             cases_to_add.append(("Content","Autotest",func,[[int(i)-1,int(i),int(i)+1]*len(func.args["int"])]))
        # else:
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
                    cases_to_add.append(("BVA","Autotest",func,int(j)-1))
                    cases_to_add.append(("BVA","Autotest",func,int(j)))
                    cases_to_add.append(("BVA","Autotest",func,int(j)+1))
        for i in loops:
            for j in re.split(TOKEN_SPLITTER,i):
                if j and j.isdigit() and checkDuplicate(cases_to_add,func,j):
                    cases_to_add.append(("loop","Autotest",func,int(j)-1))
                    cases_to_add.append(("loop","Autotest",func,int(j)))
                    cases_to_add.append(("loop","Autotest",func,int(j)+1))
        
        for i in switches:
            for j in re.split(TOKEN_SPLITTER,i):
                if j and j.isdigit() and checkDuplicate(cases_to_add,func,j):
                    cases_to_add.append(("switchcase","Autotest",func,int(j)))

        cases_to_add.append(("Positive","Autotest",func,random.randint(0,10)))
        cases_to_add.append(("Negative","Autotest",func,random.randint(-1*10,0)))
        if checkDuplicate(cases_to_add,func,0):
            cases_to_add.append(("Zero","Autotest",func,0))

    elif "string" in  func.args:
        ip_string = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5,10)))
        cases_to_add.append(("Upper","Autotest",func,ip_string))
        ip_string = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))
        cases_to_add.append(("Lower","Autotest",func,ip_string))
        ip_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5,10)))
        cases_to_add.append(("Mixed","Autotest",func,ip_string))

    return cases_to_add



def createCases(func):
    cases_to_add = predictCaseVals(func)
    case_objs = []
    for case in cases_to_add:
        t = Test(case[0],case[1])
        func = case[2]
        ip = case[3]
        if(func.ret == "bool"):
            print("For function",func.name, "returning ",func.ret)
            param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
            if param == 'True':
                ass = "EXPECT_TRUE"
            else:
                ass = "EXPECT_FALSE"
            print(f"input = {ip} assertion = {ass} and test case parameter = {param}")
            t.add_assertion(ass,[f'{func.name}({ip})'])
        elif(func.ret == "string"):
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
            print(f"input = {ip} assertion = {ass} and test case parameter = {param}")
            t.add_assertion(ass,[param,f'{func.name}({ip})'])
        else:
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
            print(f"input = {ip} assertion = {ass} and test case parameter = {param}")
            t.add_assertion(ass,[param,f'{func.name}({ip})'])
            
        # if isinstance(ip, int):
        #     print("For function",func.name, "returning ",func.ret)
        #     ass = "EXPECT_EQ"
        #     param = input(f"Enter output parameter for {ass}: ")
        #     t.add_assertion(ass,[param,f'{func.name}({ip})'])
        case_objs.append(t)
    return case_objs

def addPredictedCases(funcs):
    cases = []
    for func in funcs:
        cases.extend(createCases(func))
    return cases


