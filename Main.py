from cc_generator import CCGenerator
from Parse import *
from Test_Model import *
from Pred import *
import os

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

for pf_name in pf_names:
    pf_name = path_str + pf_name
    hf_name = pf_name[:-3] + '.h'
    tf_name = pf_name[:-3] + '_UNITTEST.cc'
    gen = CCGenerator(tf_name)
    gen.write_header(hf_name,pf_name)
    time_limit = input("Time limit for test cases: ")
    gen.write_Quicktest(time_limit, hf_name)


    t = Test('Positive','FactorialTest')
    t.add_assertion("EXPECT_EQ",['120','Factorial(5)'])
    t.add_assertion("EXPECT_EQ",['24','Factorial(4)'])
    t.add_assertion("EXPECT_EQ",['6','Factorial(3)'])
    t.add_assertion("EXPECT_EQ",['40320','Factorial(8)'])
    gen.write_test(t)


    t2 = Test('PrimeTest1','IsPrimeTestSuite')
    t2.add_assertion("EXPECT_EQ",['false','IsPrime(10)'])
    t2.add_assertion("EXPECT_EQ",['true','IsPrime(3)'])
    gen.write_test(t2)

    funcs = gen.get_functions(pf_name)
    cases = addPredictedCases(funcs)
    for case in cases:
        gen.write_test(case)


    gen.end()