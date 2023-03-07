#include<pybind11/pybind11.h>

int operate(int mode) {
  int a = 10;
  int b = 5;
  int result;
  switch (mode) {
      case 0:
        result = a+b;
        break;
      case 1:
        result = a-b;
        break;
      case 2:
        result = a*b;
        break;
      case 3:
        result = a/b;
        break;
      default:
          break;
  }
  return result;
}

PYBIND11_MODULE(sample3, handle){
    handle.def("operate", &operate);
}