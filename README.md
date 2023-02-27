Steps to Generate test cases:

git clone https://github.com/bhaveesarna/Samsung-Prism.git
cd Samsung-Prism
git clone https://github.com/pybind/pybind11.git
mkdir build
cd build && cmake .. && make
cd ..
python -u Main.py
