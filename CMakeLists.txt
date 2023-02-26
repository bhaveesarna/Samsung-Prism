cmake_minimum_required(VERSION 3.4)
project(Samsung-Prism)
add_subdirectory(pybind11)
pybind11_add_module(module_name sample1.cc)