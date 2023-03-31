#include<pybind11/pybind11.h>

int add_nums(int n, int m) {
  return m+n;
}



PYBIND11_MODULE(sample5, handle){
    handle.def("add_nums", &add_nums);
}