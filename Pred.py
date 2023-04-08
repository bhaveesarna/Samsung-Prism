from Multiple_args import Multiple_args
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
# print(globals().keys())
import string
import re

TOKENS = [':','\(','\)','/','{','}','<','>','==','<=','>=','\s']
TOKEN_SPLITTER = "|".join(TOKENS)

def predictCaseVals(func:function):
    if len(func.args_list) == 1:
        cases_to_add = []
        if func.args_list[0][0] == "int":
            nums_done = set()
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
                        if int(j)-1 not in nums_done:
                            cases_to_add.append(("BVA","BVA_less",func,int(j)-1)) 
                            nums_done.add(int(j)-1)
                        if int(j) not in nums_done:
                            cases_to_add.append(("BVA","BVA_equal",func,int(j)))
                            nums_done.add(int(j))
                        if int(j)+1 not in nums_done:
                            cases_to_add.append(("BVA","BVA_greater",func,int(j)+1))
                            nums_done.add(int(j)+1)
            for i in loops:
                for j in re.split(TOKEN_SPLITTER,i):
                    if j and j.isdigit():
                        if int(j)-1 not in nums_done:
                            cases_to_add.append(("loop","loop_less",func,int(j)-1))
                            nums_done.add(int(j)-1)
                        if int(j) not in nums_done:
                            cases_to_add.append(("loop","loop_equal",func,int(j)))
                            nums_done.add(int(j))
                        if int(j)+1 not in nums_done:
                            cases_to_add.append(("loop","loop_greater",func,int(j)+1))
                            nums_done.add(int(j)+1)
            
            for i in switches:
                for j in re.split(TOKEN_SPLITTER,i):
                    if j and j.isdigit():
                        cases_to_add.append(("switchcase",f"case_{str(j)}",func,int(j)))

            cases_to_add.append(("Autotest","Positive",func,random.randint(0,100)))
            cases_to_add.append(("Autotest","Negative",func,random.randint(-1*100,0)))
            if 0 not in nums_done:
                cases_to_add.append(("Zero","Autotest",func,0))

        elif func.args_list[0][0] == "string":
            ip_string = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5,10)))
            cases_to_add.append(("Autotest","Upper",func,ip_string))
            ip_string = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))
            cases_to_add.append(("Autotest","Lower",func,ip_string))
            ip_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5,10)))
            cases_to_add.append(("Autotest","Mixed",func,ip_string))

        elif func.args_list[0][0] == "char":
            chars_done = set()
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
                    if j and (i.index('if') < i.index(j)) and len(j.strip("'")) == 1 and not j.isdigit():
                        j = j.strip("'")
                        cases_to_add.append(("BVA","BVA_char",func,f"'{j}'"))
                        cases_to_add.append(("BVA","BVA_more_char",func,f"'{chr(ord(j)+1)}'"))   
                        cases_to_add.append(("BVA","BVA_less_char",func,f"'{chr(ord(j)-1)}'"))
            for i in loops:
                for j in re.split(TOKEN_SPLITTER,i):
                    if j and j.isdigit():
                        if int(j)-1 not in chars_done:
                            cases_to_add.append(("loop","loop_less",func,f"'{chr(ord(j)-1)}'"))
                            chars_done.add(int(j)-1)
                        if int(j) not in chars_done:
                            cases_to_add.append(("loop","loop_equal",func,f"'{chr(ord(j))}'"))
                            chars_done.add(int(j))
                        if int(j)+1 not in chars_done:
                            cases_to_add.append(("loop","loop_greater",func,f"'{chr(ord(j)+1)}'"))
                            chars_done.add(int(j)+1)
            for i in switches:
                for j in re.split(TOKEN_SPLITTER,i):
                    if j and (i.index('case') < i.index(j)) and len(j.strip("'")) == 1 and not j.isdigit():
                        j = j.strip("'")
                        cases_to_add.append(("switchcase",f"case_{chr(ord(j))}",func,f"'{chr(ord(j))}'"))
                
            cases_to_add.append(("switchcase","Random_char",func,f"'{chr(random.randint(97,122))}'"))
                
                         
        elif func.args_list[0][0] == "float":
            def is_float(string):
                try:
                    float(string)
                    return True
                except ValueError:
                    return False
            
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
                        cases_to_add.append(("BVA","BVA_less",func,float(j)-random.random())) 
                        cases_to_add.append(("BVA","BVA_equal",func,float(j)))
                        cases_to_add.append(("BVA","BVA_greater",func,float(j)+random.random()))
            for i in loops:
                for j in re.split(TOKEN_SPLITTER,i):
                    if j and j.isdigit():
                        if int(j)-1 not in nums_done:
                            cases_to_add.append(("loop","loop_less",func,float(j)-random.random()))
                            nums_done.add(int(j)-1)
                        if int(j) not in nums_done:
                            cases_to_add.append(("loop","loop_equal",func,float(j)))
                            nums_done.add(int(j))
                        if int(j)+1 not in nums_done:
                            cases_to_add.append(("loop","loop_greater",func,float(j)+random.random()))
                            nums_done.add(int(j)+1)
            
            for i in switches:
                for j in re.split(TOKEN_SPLITTER,i):
                    if j and j.isdigit():
                        cases_to_add.append(("switchcase",f"case_{str(j)}",func,float(j)))

            cases_to_add.append(("Autotest","Positive",func,random.random()*100))
            cases_to_add.append(("Autotest","Negative",func,random.random()*-100))
            if 0 not in nums_done:
                cases_to_add.append(("Autotest","Zero",func,0.0))

    else:
        mc = Multiple_args(func)
        cases_to_add = mc.cases()

    return cases_to_add


def createCases(func):
    cases_to_add = predictCaseVals(func)
    # print(cases_to_add)
    case_objs = []
    for case in cases_to_add:
        t = Test(case[0],case[1])
        func = case[2]
        ip = case[3]
        if(func.ret == "bool"):
            print("For function",func.name, "returning ",func.ret)
            if type(ip) is tuple:
                param = str(getattr(globals()[config.current_file], func.name.strip())(*ip))
            else:
                if isinstance(ip, str):
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip.strip("'")))
                else:
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
            
            if param == 'True':
                ass = "EXPECT_TRUE"
            else:
                ass = "EXPECT_FALSE"
            print(f"input = {ip} assertion = {ass} and test case parameter = {param}")
            print("testing:", str(ip).strip("(").strip(")"))
            t.add_assertion(ass,[f'{func.name}({str(ip).strip("(").strip(")")})'])
        elif(func.ret == "string"):
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            if type(ip) is tuple:
                param = str(getattr(globals()[config.current_file], func.name.strip())(*ip))
            else:
                if isinstance(ip, str):
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip.strip("'")))
                else:
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
            print(f"input = {ip} assertion = {ass} and test case parameter = \"{param}\"")
            t.add_assertion(ass,[f"\"{param}\"", f'{func.name}({str(ip).strip("(").strip(")")})'])
        elif(func.ret == "char"):
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            if type(ip) is tuple:
                param = str(getattr(globals()[config.current_file], func.name.strip())(*ip))
            else:
                if isinstance(ip, str):
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip.strip("'")))
                else:
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
            print(f"input = {ip} assertion = {ass} and test case parameter = \'{param}\'")
            t.add_assertion(ass,[f"\'{param}\'", f'{func.name}({str(ip).strip("(").strip(")")})'])
        else:
            print("For function",func.name, "returning ",func.ret)
            ass = "EXPECT_EQ"
            if type(ip) is tuple:
                param = str(getattr(globals()[config.current_file], func.name.strip())(*ip))
            else:
                if isinstance(ip, str):
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip.strip("'")))
                else:
                    param = str(getattr(globals()[config.current_file], func.name.strip())(ip))
                
            print(f"input = {ip} assertion = {ass} and test case parameter = {param}")
            t.add_assertion(ass,[param, f'{func.name}({str(ip).strip("(").strip(")")})'])
            
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


