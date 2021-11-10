import sys
import os


for _ in sys.path:
    print(_)

list = sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
# sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
print(15*"_")
for _ in sys.path:
    print(_)
