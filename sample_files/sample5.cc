#include<pybind11/pybind11.h>

int add_nums(float n, int m) {
  if (n == 3.3f){
    return 0;
  }
  else if(m == 3){
    return 3;
  }
  else return m+m;
}

char return_greater_character(char n) {
  switch(n){
    case 'a':
      return 'b';
    case 'b':
      return 'a';
  }
  return 'c';
}


PYBIND11_MODULE(sample5, handle){
    handle.def("add_nums", &add_nums);
    handle.def("return_greater_character", &return_greater_character);
}