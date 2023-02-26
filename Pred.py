from Test_Model import *
from Parse import *
import random
import sys
from build.module_name import *
import string



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
        lines = func.content.split(';')
        for idx in range(len(lines)):
            if 'if' in lines[idx]:
                conditions.append(lines[idx])
        for i in conditions:
            for j in i.split():
                if j.isdigit() and (i.index('if') < i.index(j)) and checkDuplicate(cases_to_add,func,j):
                    cases_to_add.append(("BVA","Autotest",func,int(j)-1))
                    cases_to_add.append(("BVA","Autotest",func,int(j)))
                    cases_to_add.append(("BVA","Autotest",func,int(j)+1))

        cases_to_add.append(("Positive","Autotest",func,random.randint(0,100)))
        cases_to_add.append(("Negative","Autotest",func,random.randint(-1*100,0)))
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
            param = param = str(globals()[func.name.strip()](ip))
            if param == 'True':
                ass = "EXPECT_TRUE"
            else:
                ass = "EXPECT_FALSE"
            t.add_assertion(ass,[f'{func.name}({ip})'])
        elif(func.ret == "string"):
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            param = input(f"Enter output parameter for {ass}: ")
            t.add_assertion(ass,[param,f'{func.name}({ip})'])
        else:
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            param = input(f"Enter output parameter for {ass}: ")
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


