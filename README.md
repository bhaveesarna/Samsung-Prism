Steps to Generate test cases:

for windows(64 bit):
git clone https://github.com/bhaveesarna/Samsung-Prism.git
cd Samsung-Prism
git clone https://github.com/pybind/pybind11.git
mkdir build
cd build && cmake -A x64 .. && cmake --build . --config Release
cd ..
python -u Main.py

Note: for building on windows, visual studio 2019 or newer is required


for linux:
git clone https://github.com/bhaveesarna/Samsung-Prism.git
cd Samsung-Prism
git clone https://github.com/pybind/pybind11.git
mkdir build
cd build && cmake .. && make
cd ..
python -u Main.py
