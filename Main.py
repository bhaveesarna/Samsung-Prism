from cc_generator import CCGenerator
from Parse import *
from Test_Model import *
import os
import config

path_str=""
input_file_or_dir = input("File/Directory to be parsed: ")
pf_names = []
if os.path.isdir(input_file_or_dir):
    pf_names = os.listdir(input_file_or_dir)
    path_str+=input_file_or_dir
    path_str+="/"
elif os.path.isfile(input_file_or_dir):
    pf_names.append(input_file_or_dir)
else:
    print("not a file or directory")
    exit()
config.file_list = pf_names
from Pred import *
for pf_name in pf_names:
    config.current_file = os.path.splitext(pf_name)[0]
    pf_name = path_str + pf_name
    hf_name = pf_name[:-3] + '.h'
    tf_name = pf_name[:-3] + '_UNITTEST.cc'
    gen = CCGenerator(tf_name)
    gen.write_header(hf_name,pf_name)
    time_limit = input("Time limit for test cases: ")
    gen.write_Quicktest(time_limit, hf_name)

    funcs = gen.get_functions(pf_name)
    cases = addPredictedCases(funcs)
    for case in cases:
        gen.write_test(case)


    gen.end()