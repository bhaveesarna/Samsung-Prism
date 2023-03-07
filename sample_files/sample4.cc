#include<pybind11/pybind11.h>

// Returns sum of numbers upto n
bool find_while(int n) {
  int i = 0;
  while(i <= 10) {
    if(i == n) {
        return true;
    }
    i++;
  }
  return false;
}



PYBIND11_MODULE(sample4, handle){
    handle.def("find_while", &find_while);
}
