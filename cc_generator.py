from Test_Model import Test
from Parse import *

class CCGenerator:
    def __init__(self,file_name) -> None:
        self.file = file_name
    
    def write_test(self,test: Test):
        f = open(f'{self.file}','a+')
        f.write('\n')
        f.write(test.serialize())
    
    def write_Quicktest(self,time,hfile):
        f = open(f'{self.file}','w+')
        f.write('#include "'+ hfile +'"\n#include "gtest/gtest.h"\nnamespace {\nclass QuickTest : public testing::Test {\nprotected:\nvoid SetUp() override { start_time_ = time(nullptr); }\nvoid TearDown() override {\n\tconst time_t end_time = time(nullptr);\nEXPECT_TRUE(end_time - start_time_ <= ' + str(time) + ') << "The test took too long.";\n}\n};')

    def write_header(self,hfile,pfile):
        f = open(f'{hfile}','w+')
        hfile = hfile[:-2]
        f.write(f'#ifndef {hfile}_H \n#define {hfile}_H\n')
        p = parser(pfile)
        funcs = p.get_functions()
        for func in funcs:
            f.write(func.head_serialize())
            f.write('\n')
        f.write('#endif')
    
    def get_functions(self,pfile):
        p = parser(pfile)
        funcs = p.get_functions()
        return funcs



    def end(self):
        f = open(f'{self.file}','a+')
        f.write('\n}')




